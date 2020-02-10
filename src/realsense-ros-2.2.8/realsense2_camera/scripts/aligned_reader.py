#!/usr/bin/env python
import rospy
import tf
from sensor_msgs.msg import Image, PointField
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

def save_image(path, name, image):
    cv2.imwrite(os.path.join(path , str(name)+'.jpg'),image)
        
class DepthReader:
    def __init__(self):
        rospy.init_node('depth_node', anonymous=True)
        self.hz = 50
        self.depth_points = rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", Image, self.depth_callback)
        self.ready = False
        self.data = np.zeros((300, 300))
        self.bridge = CvBridge()
        # fig = plt.figure()
        # self.im = plt.imshow(self.data,  cmap='gray', vmin=0, vmax=255)
        # anim = animation.FuncAnimation(fig, self.animate, init_func=self.init, frames=30,
                                # interval=250)
        # plt.show()

    def init(self):
        self.im.set_data(np.zeros((1000,1000)))
    
    
    def animate(self,i):
        if self.ready:
            self.im.set_data(self.data)
        self.ready = False	
        return self.im


        
    def depth_callback(self, image_msg):
        if not self.ready:
            self.data = ros_numpy.numpify(image_msg) / 2^16
            print(np.max(self.data))
            print(np.min(self.data))
            # self.ready = True
            try:
                cv_image = self.bridge.imgmsg_to_cv2(image_msg, "16UC1")
                path = os.getenv("HOME") + "/test/"
                current_timestamp = str(image_msg.header.stamp.secs) + str(image_msg.header.stamp.nsecs) 
				
                save_image(path, current_timestamp, cv_image)
                saved_timestamp = current_timestamp
				
            except CvBridgeError as e:
	            print(e)


       
            
    def run(self):
        rate = rospy.Rate(self.hz)
        while not rospy.is_shutdown():
            rate.sleep()

    
if __name__ == '__main__':
    depth = DepthReader()
    depth.run()


