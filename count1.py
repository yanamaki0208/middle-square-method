#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('count1')
pub = rospy.Publisher('count_up1', Int32, queue_size=1)
rate = rospy.Rate(1)

n = 60
o = 0

while not rospy.is_shutdown():
	n -= 1
	o += 1
	pub.publish(n)
	rate.sleep()
	pub.publish(o)
	rate.sleep()
