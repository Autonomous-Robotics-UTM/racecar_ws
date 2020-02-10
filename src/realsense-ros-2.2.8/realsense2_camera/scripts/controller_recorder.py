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
import os
import time
import message_filters
from ackermann_msgs.msg import AckermannDriveStamped
import requests
import json

counter = 0
saved_timestamp = 0
frame = 0
class Recorder:

	def __init__(self):
		rospy.init_node("recorder", anonymous=True)
		#Subscribe to the image output of the camera
		#self.image_stream = message_filters.Subscriber("/camera/color/image_raw", Image)

		# collect joystick data
		self.control_stream = message_filters.Subscriber("/joy",Joy)
		# ts = message_filters.ApproximateTimeSynchronizer([self.image_stream, self.control_stream], 1, 1)
		# ts.registerCallback(self.syncCallBack)

		# collect pid angle data
		self.pid_stream = message_filters.Subscriber("/ackermann_cmd_mux/input/default", AckermannDriveStamped, queue_size=10)
		ts = message_filters.ApproximateTimeSynchronizer([self.control_stream], 1, 1)
		ts.registerCallback(self.syncCallBack)

	def syncCallBack(self, joy_msg):
		global counter
		print(counter)
		try:
			if joy_msg.buttons[4]:
				now = str(counter)
				control = str(joy_msg.axes[3])
				print(control)
				url = "http://142.1.44.127:8080/graph"
				#values = json.dumps({'time': now, 'command': control})
				requests.post(url, json= {'time': now, 'command': control})
				counter += 1
		except:
			print("Error happnened")
	
	

	def run(self):
		try:
    			rospy.spin()
  		except KeyboardInterrupt:
    			print("Shutting down")



if __name__ == '__main__':
    	saver = Recorder()
    	saver.run()
