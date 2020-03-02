#!/usr/bin/env python
import rospy
import tf
from sensor_msgs.msg import PointCloud2, PointField
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
        
class DepthReader:
    def __init__(self):
        rospy.init_node('depth_node', anonymous=True)
        self.hz = 50
        self.depth_points = rospy.Subscriber("/camera/depth/color/points", PointCloud2, self.depth_callback)
        self.ready = False
        fig = plt.figure()
        self.data = np.zeros((300, 300))
        self.im = plt.imshow(self.data,  cmap='gray', vmin=0, vmax=255)
        anim = animation.FuncAnimation(fig, self.animate, init_func=self.init, frames=30,
                               interval=250)
        plt.show()

    def init(self):
        self.im.set_data(np.zeros((1000,1000)))
    
    
    def animate(self,i):
        if self.ready:
            self.im.set_data(self.data)	
    
        self.data = np.zeros((300, 300))
        self.ready = False	
        return self.im

        
    def depth_callback(self, point_cloud):
        #min_x = 0
        #min_y = 0
        #max_x = 0
        #max_y = 0
        
        #pointcloud2_array = list(pc2.read_points(point_cloud,field_names=("x","y","z"),skip_nans=True))

        #print(pointcloud2_array)
        """
        for p in pc2.read_points(point_cloud, field_names = ("x", "y", "z", "rgb"), skip_nans=True):
            rgb = p[3]
            r = (rgb & 0x00FF0000)>> 16
            g = (rgb & 0x0000FF00)>> 8
            b = (rgb & 0x000000FF)
            gray = (r + b + g)/3
            self.data[int(150+p[1]*100)][int(150+p[0]*100)] = int(gray*100)
        """
        sensor = ros_numpy.point_cloud2.pointcloud2_to_xyz_array(point_cloud)
        zs = sensor[:,-1:].squeeze()

        xs = sensor[:,0:1].squeeze()
        xs = np.round(xs*100)+150
        xs = xs.astype(int)

        ys = sensor[:,1:2].squeeze()
        ys = np.round(ys*100)+150
        ys = ys.astype(int)
        ys[ys>300] = 299
        ys[ys<0] = 0

        xs[xs>300] = 299
        xs[xs<0] = 0

        self.data[ys,xs] = zs*100
        #print(sensor[:,3])
        print(np.max(self.data))
        
        
        #print " x : %f  y: %f  z: %f" %(p[0],p[1],p[2])
        self.ready = True
        #plt.show()
        #print(min_y)
        #print(max_y)
       
            
    def run(self):
        rate = rospy.Rate(self.hz)
        while not rospy.is_shutdown():
            rate.sleep()

    
if __name__ == '__main__':
    depth = DepthReader()
    depth.run()


