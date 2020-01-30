#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage

import message_filters
import os

import time

# timestamp -> { image_data, pid_data }
dataFileName = ""

def syncCallBack(image, compImage):
	
	timeStamp = str(image.header.stamp.secs) + str(image.header.stamp.nsecs) 
	print("time:",timeStamp)	
	print("img header")
	print(image.header)
	print("")
	print("Comp image format:")
	print(compImage.format)
	print("")
	print("")
	
	f = open(dataFileName, "a")
	f.write(timeStamp)
	f.write("\n")
	f.close()

	time.sleep(1)
	

def imageListener(topics, dataFileName):
#def imageListener():
	'''
	
	rospy.Subscriber('/camera/color/image_raw', Image, callback)
	rospy.Subscriber('/camera/color/image_raw/compressed', CompressedImage, compressedCallback)


	#rospy.spin()
	while True:
		imageData.append
	'''
	rospy.init_node('listener',anonymous=True)

	image_sub = message_filters.Subscriber(topics[0], Image)
	comp_image_sub = message_filters.Subscriber(topics[1], CompressedImage)


#	image_sub = message_filters.Subscriber('/camera/color/image_raw', Image)
#	comp_image_sub = message_filters.Subscriber('/camera/color/image_raw/compressed', CompressedImage)

	
	ts = message_filters.TimeSynchronizer([image_sub, comp_image_sub], 1)
	ts.registerCallback(syncCallBack)

	rospy.spin()

if __name__ == '__main__':
	print("Starting listener")
	
	topics = []
	val = str(raw_input("Add Topic Name: "))
	while(val != "q"):		
		topics.append(val)
		val = str(raw_input("Add Topic Name: "))

	
	if (len(topics) == 0):
		print("Add atleast one topics")
		os.exit(1)
	
	dataFileName = str(raw_input("Enter fileName for Data: "))

	
	imageListener(topics, dataFileName)
	print("hello")

	
