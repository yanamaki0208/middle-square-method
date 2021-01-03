#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0
o = 0
 
def cb(message):
	global n
	global o
	n = message.data*2
	o = message.data*5

rospy.init_node('twice2')
sub = rospy.Subscriber('count_up1', Int32, cb)
sub = rospy.Subscriber('count_up2', Int32, cb)
pub = rospy.Publisher('twice2', Int32, queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
	pub.publish(n)
	pub.publish(o)
	rate.sleep()
