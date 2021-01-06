#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('count2')
pub = rospy.Publisher('count_up2', Int32, queue_size=1)
rate = rospy.Rate(1)
o = 0
while not rospy.is_shutdown():
        o+= 1
        pub.publish(o)
        rate.sleep()
