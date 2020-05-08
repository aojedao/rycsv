#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('kobuki_trajectory', anonymous=True)
    velocity_publisher = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    vel_msg = Twist()
    
    rate = rospy.Rate(10) #10hz


    #Since we are moving just in x-axis
    vel_msg.linear.x = -2.5
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    #Force the robot to stop
    velocity_publisher.publish(vel_msg)

    #Since we are moving just in x-axis
    #velocity='[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'

    #Force the robot to stop
    #velocity_publisher.publish(velocity)

    while not rospy.is_shutdown():
	    vel_msg.linear.x = -2.5
	    vel_msg.linear.y = 0
	    vel_msg.linear.z = 0
	    vel_msg.angular.x = 0
	    vel_msg.angular.y = 0
	    vel_msg.angular.z = 0
	    #rospy.loginfo()
	    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
