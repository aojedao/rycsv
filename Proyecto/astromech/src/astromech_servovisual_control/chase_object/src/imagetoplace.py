
#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import cv2
from cv_bridge import CvBridge
from geometry_msgs.msg import Point
from std_msgs.msg import String
import numpy as np


def callback_detect(ObjectsStamped):

    global coordinates

    if ObjectsStamped != []
	objectWidth = ObjectsStamped[1];
	objectHeight = ObjectsStamped[2];

def Init():

    global pub

    # Define Publisher
    pub = rospy.Publisher('thetaDist', Point, queue_size=1)

    # Subscribe to detectObject
    rospy.Subscriber("Objects", find_object_2d/ObjectsStamped, callback_detect)
    # Initialize node
    rospy.init_node('image_to_place', anonymous=True)

if __name__ == '__main__':
    try:
        Init()
    except rospy.ROSInterruptException:
        pass


while not rospy.is_shutdown():
    if image:
        # print("theta_ball:", theta_ball)

        if lidar:
            if theta_ball != 999:
                theta_ball = theta_ball%360
                # theta_ball_min = (theta_ball -1)%360
                # theta_ball_max = (theta_ball+1)%360
                ball_range = ldata.ranges[theta_ball]  # ball distance in m
                # ball_range_min = ldata.ranges[theta_ball_min]
                # ball_range_max = ldata.ranges[theta_ball_max]
                # ball_range = (1/3)*(ball_range + ball_range_max + ball_range_min)

                # if ball_range < ldata.range_min:
                #     ball_range = 0.120
                # elif ball_range > ldata.range_max:
                #     ball_range = 3.5

                # print("range:", ball_range)

                msg = Point()
                msg.x = ball_range
                msg.y = theta_ball
                # rospy.loginfo(msg)
                pub.publish(msg)

            else:
                msg = Point()
                msg.x=999
                msg.y=999
                # rospy.loginfo(msg)
                pub.publish(msg)

        rate.sleep()




			// Find corners Qt
			QTransform qtHomography(data[i+3], data[i+4], data[i+5],
									data[i+6], data[i+7], data[i+8],
									data[i+9], data[i+10], data[i+11]+11]);

			QPointF qtTopLeft = qtHomography.map(QPointF(0,0));
			QPointF qtTopRight = qtHomography.map(QPointF(objectWidth,0));
			QPointF qtBottomLeft = qtHomography.map(QPointF(0,objectHeight));
			QPointF qtBottomRight = qtHomography.map(QPointF(objectWidth,objectHeight));

			//my test again			
			float xtop=(((qtTopLeft.x()+qtTopRight.x())/2)+((qtBottomLeft.x()+qtBottomRight.x())/2)/2)

			printf("(%f) \n"),
				xtop;
			

			printf("this Object %d detected, Qt corners at (%f,%f) (%f,%f) (%f,%f) (%f,%f)\n",
					id,
					qtTopLeft.x(), qtTopLeft.y(),
					qtTopRight.x(), qtTopRight.y(),
					qtBottomLeft.x(), qtBottomLeft.y(),
					qtBottomRight.x(), qtBottomRight.y());
