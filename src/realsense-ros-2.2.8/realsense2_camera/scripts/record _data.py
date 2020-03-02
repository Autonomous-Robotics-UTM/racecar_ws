#!/usr/bin/env python
import rospy
import tf
from sensor_msgs.msg import Image
from sensor_msgs.msg import Joy
from geometry_msgs.msg import TwistStamped
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
from ackermann_msgs.msg import AckermannDriveStamped


counter = 50000
saved_timestamp = 0
frame = 0
class ImageSaver:

	def __init__(self):
		rospy.init_node("image_saver", anonymous=True)
  		self.bridge = CvBridge()
		#Subscribe to the image output of the camera
		self.image_stream = message_filters.Subscriber("/camera/color/image_raw", Image)

		# collect joystick data
		self.control_stream = message_filters.Subscriber("/joy",Joy)
		# ts = message_filters.ApproximateTimeSynchronizer([self.image_stream, self.control_stream], 1, 1)
		# ts.registerCallback(self.syncCallBack)

		# collect pid angle data
		self.pid_stream = message_filters.Subscriber("/ackermann_cmd_mux/input/default", AckermannDriveStamped, queue_size=10)
		ts = message_filters.ApproximateTimeSynchronizer([self.image_stream, self.pid_stream,self.control_stream], 1, 1)
		ts.registerCallback(self.syncCallBackPid)

		self.file = open("labels.txt","w")




	def syncCallBack(self, image_msg, joy_msg):
		global counter
		global saved_timestamp
		global frame
		print(counter)
		try:
			cv_image = self.bridge.imgmsg_to_cv2(image_msg, "bgr8")
			path = os.getenv("HOME") + "/images/"
			if counter > 0 and joy_msg.buttons[5]:
				current_timestamp = str(image_msg.header.stamp.secs) + str(image_msg.header.stamp.nsecs) 
				if(saved_timestamp != current_timestamp):
					save_image(path, current_timestamp, cv_image)
					self.file.write(current_timestamp+" "+str(joy_msg.axes[3])+"\n")
					saved_timestamp = current_timestamp
					frame = 0
				else:
					frame += 1
					save_image(path, current_timestamp+" ({})".format(frame), cv_image)
					self.file.write(current_timestamp+" "+str(joy_msg.axes[3])+"\n")
				counter-=1
			if counter == 0 or counter % 200 == 0:
				self.file.close()
				self.file = open("labels.txt","a")
					
		except CvBridgeError as e:
			print(e)
	
	def syncCallBackPid(self, image_msg, drive_msg, joy_msg):
		global counter
		global saved_timestamp
		global frame
		print(counter)
		try:

			steer = drive_msg.drive.steering_angle

			cv_image = self.bridge.imgmsg_to_cv2(image_msg, "bgr8")
			path = os.getenv("HOME") + "/images/"
			if counter > 0 and joy_msg.buttons[5]:
				current_timestamp = str(image_msg.header.stamp.secs) + str(image_msg.header.stamp.nsecs) 
				if(saved_timestamp != current_timestamp):
					save_image(path, current_timestamp, cv_image)
					self.file.write(current_timestamp+" "+str(steer)+"\n")
					saved_timestamp = current_timestamp
					frame = 0
				else:
					frame += 1
					save_image(path, current_timestamp+" ({})".format(frame), cv_image)
					self.file.write(current_timestamp+" "+str(steer)+"\n")
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
