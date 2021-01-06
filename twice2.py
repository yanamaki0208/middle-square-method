#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from googletrans import Translator

src = ""
text = ""
 
def cb(message):
	text = message.data

rospy.init_node('twice2')
sub = rospy.Subscriber('count_up', Int32, cb)
#sub = rospy.Subscriber('count_up2', Int32, cb)
pub = rospy.Publisher('twice2', Int32, queue_size=1)
rate = rospy.Rate(0.2)
while not rospy.is_shutdown():
	pub.publish(text)
	rate.sleep()
