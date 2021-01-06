#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from googletrans import Translator

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
rate = rospy.Rate(0.2)
src = ""
text = ""
while not rospy.is_shutdown():
        src = input()
        tr = Translator()
        tr = Translator(service_urls=['translate.googleapis.com'])
        while True:
          try:
            text = tr.translate(src, dest="en").text
            break
          except Exception as e:
            tr = Translator()
            tr = Translator(service_urls=['translate.googleapis.com'])
pub.publish(text)
rate.sleep()
