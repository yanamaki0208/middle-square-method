#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 1234

def cb(message):
	global n
	n = message.data

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('twice', Int32, queue_size=1)
rate = rospy.Rate(0.5)
while not rospy.is_shutdown():
	pub.publish(n)
	rate.sleep()
