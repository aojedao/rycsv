#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2

x = 0.0
y = 0.0
theta = 0.0

def newOdom(msg):
	global x
	global y
	global theta
	
	#Update x,y,theta every cycle
	x=msg.pose.pose.position.x
	y=msg.pose.pose.position.y
	
	#We cannot obtain z orientation angle directly from a quaternion
	#We use a converter to euler angles
	rot_q=msg.pose.pose.orientation
	(roll, pitch, yaw)=euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
	#yaw angle is the same theta that we need
	theta=yaw

rospy.init_node ("speed_controller", disable_signals=True)



rate = rospy.Rate(50)

sub = rospy.Subscriber("/odom", Odometry, newOdom)
pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=5)

###############################################################
#Implementation of Holonomic Control Algorithm:
###############################################################
#Expected to be provided by the user:
linear_vel = 0.8
omega = 2

vel_msg= Twist()

def reachGoal(g_x,g_y):
	goal= Point()
	goal.x = g_x
	goal.y = g_y
	#calculate the position error
	err_x = goal.x - x
	err_y = goal.y - y
	a2goal = atan2(err_y,err_x)
	print(str(a2goal - theta)+';'+str(x)+";"+str(y))
	while (abs(err_x)>0.05) or (abs(err_y)>0.05):
		#calculate the orientation error
		a2goal = atan2(err_y,err_x)
	
		print(str(a2goal - theta)+';'+str(x)+";"+str(y))
	
		#We define our control rule (and a margin)
		if (abs(a2goal - theta) > 0.2):
			#We only want it to rotate
			vel_msg.linear.x = 0.0
			#We rotate with defined angular speed (omega)
			vel_msg.angular.z = omega
		else:
			#We move straigh ahead with constant linear velocity
			vel_msg.linear.x = linear_vel
			#We only want it to advance
			vel_msg.angular.z = 0.0
		pub.publish(vel_msg)
		rospy.sleep(0.1)
	print('Goal Reached')
	
	

if __name__ == '__main__':

	while not rospy.is_shutdown():
		sequence = [[0, 0], [-3.5, 0], [-3.5, 3.5], [1.5, 3.5], [1.5, -1.5], [3.5, -1.5],[3.5, -8.0], [-2.5, -8.0], [-2.5, -5.5], [1.5, -5.5], [1.5, -3.5],[-1.0, -3.5]]
		for i in sequence:
			print(i)
			reachGoal(i[0], i[1])
		rospy.signal_shutdown("Goal reached")
	rospy.spin()
