#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

def move():
    # Starts a new node
    rospy.init_node('kobuki_trajectory', anonymous=True)
    velocity_publisher = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
    vel_msg = Twist()
    
    rate = rospy.Rate(10) #10hz


    #Since we are moving just in x-axis
    vel_msg.linear.x = -2.6
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    #Force the robot to stop
    for x in range(2) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)
    #turn    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = -2.5
    for x in range(1) :
		velocity_publisher.publish(vel_msg)		
		rospy.sleep(1)

    #Advance
    vel_msg.linear.x = -2.7
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(2) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)

    #turn    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = -2.8
    for x in range(1) :
		velocity_publisher.publish(vel_msg)		
		rospy.sleep(1)

    #Advance
    vel_msg.linear.x = -2.6
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(2) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)	

    #turn    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = -2.7
    for x in range(1) :
		velocity_publisher.publish(vel_msg)		
		rospy.sleep(1)
    #Advance
    vel_msg.linear.x = -2.5
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(2) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)
    #Advance
    vel_msg.linear.x = -2
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(2) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)

    #turn    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 1.7
    for x in range(1) :
		velocity_publisher.publish(vel_msg)		
		rospy.sleep(1)

    #Advance
    vel_msg.linear.x = -2.5
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(1) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)

    #turn    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = -2.5
    for x in range(1) :
		velocity_publisher.publish(vel_msg)		
		rospy.sleep(1)

    #Advance
    vel_msg.linear.x = -2.8
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(3) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)

    #turn    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = -2.8
    for x in range(1) :
		velocity_publisher.publish(vel_msg)		
		rospy.sleep(1)

    #Advance
    vel_msg.linear.x = -2.5
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(4) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)

    #turn    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = -2.8
    for x in range(1) :
		velocity_publisher.publish(vel_msg)		
		rospy.sleep(1)

    #Advance
    vel_msg.linear.x = -2
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(2) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)

    #turn    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = -2.8
    for x in range(1) :
		velocity_publisher.publish(vel_msg)		
		rospy.sleep(1)

    #Advance
    vel_msg.linear.x = -2
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(3) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)

    #turn    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 2.5
    for x in range(1) :
		velocity_publisher.publish(vel_msg)		
		rospy.sleep(1)

    #Advance
    vel_msg.linear.x = -2.2
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(1) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)

    #turn    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 2.5
    for x in range(1) :
		velocity_publisher.publish(vel_msg)		
		rospy.sleep(1)

    #Advance
    vel_msg.linear.x = -2.5
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    for x in range(1) :
	    velocity_publisher.publish(vel_msg)
	    rospy.sleep(1)


if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
