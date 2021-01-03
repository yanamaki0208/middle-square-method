#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('count1')
pub = rospy.Publisher('count_up1', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0
while not rospy.is_shutdown():
        n+= 1
        pub.publish(n)
        rate.sleep()
