#!/usr/bin/env python
import rospy
import tf
from sensor_msgs.msg import Image
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
counter = 0
start = 0
class ImageSaver:

	def __init__(self):
		rospy.init_node("image_saver", anonymous=True)
  		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.save_callback)

	def save_callback(self, image_msg):
		limit = 100
		global counter
		global start
		try:
			cv_image = self.bridge.imgmsg_to_cv2(image_msg, "bgr8")
			#cv2.imshow("Image window", cv_image)
    			#cv2.waitKey(3)
			path = os.getenv("HOME")
			if counter == 0:
				start = time.time() 
			if counter < limit:			
				cv2.imwrite(os.path.join(path , 'image'+str(counter)+'.jpg'),cv_image)
					
			counter += 1
			if counter == limit:
				print(time.time() - start)
					
		except CvBridgeError as e:
			print(e)

	def run(self):
		try:
    			rospy.spin()
  		except KeyboardInterrupt:
    			print("Shutting down")
  		cv2.destroyAllWindows()


if __name__ == '__main__':
    	saver = ImageSaver()
    	saver.run()
