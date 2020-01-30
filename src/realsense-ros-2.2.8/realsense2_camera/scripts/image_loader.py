#!/usr/bin/env python
import rospy
import tf
from sensor_msgs.msg import Image
from sensor_msgs.msg import Joy
import sensor_msgs.point_cloud2 as pc2
import numpy
import sys
import struct
import ctypes
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import matplotlib.image as mpimg
import ros_numpy
import numpy as np
import cv2
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
import os
import time
import message_filters


counter = 100
start = 0
class ImageSaver:

	def __init__(self):
		rospy.init_node("image_saver", anonymous=True)
  		self.bridge = CvBridge()
		#Subscribe to the image output of the camera
		self.image_stream = message_filters.Subscriber("/camera/color/image_raw", Image)
		self.control_stream = message_filters.Subscriber("/joy",Joy)
		ts = message_filters.ApproximateTimeSynchronizer([self.image_stream, self.control_stream], 1, 1)
		ts.registerCallback(self.syncCallBack)
		self.file = open("labels.txt","a")


	def syncCallBack(self, image_msg, joy_msg):
		global counter
		global start
		print("callback triggered")
		try:
			cv_image = self.bridge.imgmsg_to_cv2(image_msg, "bgr8")
			path = os.getenv("HOME")
			if counter > 0:
				save_image(path, str(image_msg.header.stamp.secs), cv_image)
				self.file.write(str(joy_msg.header.stamp.secs)+" "+str(joy_msg.axes[3])+"\n") 
				counter-=1
			if counter == 0:
				self.file.close()
					
		except CvBridgeError as e:
			print(e)

	def run(self):
		try:
    			rospy.spin()
  		except KeyboardInterrupt:
    			print("Shutting down")
  		cv2.destroyAllWindows()


def showStream():
	cv2.imshow("Image window", cv_image)
	cv2.waitKey(3)

def save_image(path, name, image):
	cv2.imwrite(os.path.join(path , str(name)+'.jpg'),image)


if __name__ == '__main__':
    	saver = ImageSaver()
    	saver.run()
