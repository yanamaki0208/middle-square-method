#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

#Please enter a 4-digit number in s1
s1= 1234
i = s1

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(0.5)

while not rospy.is_shutdown():
	s2=s1*s1
	s3=str(s2)
	s4=s3.zfill(8)
	n=int(s4[2:6])
	s1= n
	pub.publish(n)
	rate.sleep()
