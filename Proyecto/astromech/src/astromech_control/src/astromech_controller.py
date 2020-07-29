#!/usr/bin/env python
import RPi.GPIO as GPIO          
from time import sleep
import __future__ 

#import roslib; roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist
from std_msgs.msg import String
import time

GPIO.setwarnings(False)

in1 = 24
in2 = 23
en1 = 25

in3 =27
#in3 = 11
in4 = 17
#in4 = 13
en2 = 22
#en2 =15

temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p=GPIO.PWM(en1,500)
p2=GPIO.PWM(en2,1000)
p.start(25)
p2.start(25)

p.ChangeDutyCycle(55)
p2.ChangeDutyCycle(75)



processing = False
new_msg = False
msg=Twist()

def callback(data):
    global processing, new_msg, msg
    print("this may work")
    msg = data

def listener():
    global processing, new_msg, msg
    rospy.init_node('AstroListener')
    rospy.Subscriber('cmd_vel', Twist, callback)
    r = rospy.Rate(5)
    
    
    #set processing to True
    
    #simulate a process that take 0.2 seconds
    rospy.loginfo(msg)
    r.sleep()
    print("it aint shit")

    
               
    
if __name__ == '__main__':
    listener()
    while not rospy.is_shutdown():

	if msg.linear.x != 999:
	
		#move forward

		if msg.linear.x > 0 :
		    print("forward")
		    GPIO.output(in1,GPIO.HIGH)
		    GPIO.output(in2,GPIO.LOW)
		    
		    GPIO.output(in3,GPIO.HIGH)
		    GPIO.output(in4,GPIO.LOW)
		    temp1=1
		    

		#move backward
		if msg.linear.x < 0 :
		    print("backward")
		    GPIO.output(in1,GPIO.LOW)
		    GPIO.output(in2,GPIO.HIGH)
		    
		    GPIO.output(in3,GPIO.LOW)
		    GPIO.output(in4,GPIO.HIGH)
		    temp1=0

		#move right
		if msg.angular.z < 0:
		    print("turn right")
		    GPIO.output(in1,GPIO.HIGH)
		    GPIO.output(in2,GPIO.LOW)
		    
		    GPIO.output(in3,GPIO.LOW)
		    GPIO.output(in4,GPIO.HIGH)
		    temp1=0

		#move left
		if msg.angular.z > 0:
		    print("turn left")
		    GPIO.output(in1,GPIO.LOW)
		    GPIO.output(in2,GPIO.HIGH)
		    
		    GPIO.output(in3,GPIO.HIGH)
		    GPIO.output(in4,GPIO.LOW)
		    temp1=0
		    
	else:
		x = 0
		y = 0
		z = 0
		th = 0
