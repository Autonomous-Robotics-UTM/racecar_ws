#!/usr/bin/env python
import torch
import importlib
import rospy
from cv_bridge import CvBridge, CvBridgeError
import message_filters
from sensor_msgs.msg import Image
from geometry_msgs.msg import TwistStamped
import numpy as np
import torch.nn as nn
from ackermann_msgs.msg import AckermannDriveStamped
import time
from os import listdir
from os.path import isfile, join
import message_filters

PATH = '~/racecar_ws/src/realsense-ros-2.2.8/realsense2_camera/scripts/model.pt'
DIR = "/home/model3/racecar_ws/src/realsense-ros-2.2.8/realsense2_camera/scripts"

class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        img_size = torch.Size([1, 3,480, 640])
        empty = torch.zeros(img_size)
        
        self.conv = nn.Sequential(nn.Conv2d(3, 16, 11, stride=3),
                                  nn.MaxPool2d(2),
                                  nn.ReLU(),
                                  nn.Conv2d(16, 32, 11, stride=3),
                                  nn.MaxPool2d(2),
                                  nn.ReLU(),
                                  nn.Conv2d(32, 64, 7, stride=3),
                                  nn.ReLU()
                                 )
        
        units = self.conv(empty).numel()
        print("units after conv", units)
        
        self.fc = nn.Sequential(nn.Linear(units, units//2),
                                nn.ReLU(),
                                nn.Linear(units//2, units//4),
                                nn.ReLU(),
                                nn.Linear(units//4, 1))
        
        print("conv parameters: ", sum(p.numel() for p in self.conv.parameters()))
        print("fc parameters: ", sum(p.numel() for p in self.fc.parameters()))
    
    def forward(self, x):
        #x: batch, channel, height, width
        batch_size = x.shape[0]
        
        out = self.conv(x)
        out = out.reshape((batch_size,-1))
        out = self.fc(out)
        return out


class NNRunner:

    def __init__(self, device):

        self.ready = False

        # create a ros node
        rospy.init_node("nn_runner", anonymous=True)
        self.device = device

        # initialize image streams
        self.bridge = CvBridge()

        self.image_stream = message_filters.Subscriber("/camera/color/image_raw", Image)
        self.depth_stream = message_filters.Subscriber("/camera/aligned_depth_to_color/image_raw", Image)
        ts = message_filters.ApproximateTimeSynchronizer([self.image_stream, self.depth_stream], 1, 1)
        ts.registerCallback(self.image_stream_callback)

        self.ack_pub = rospy.Publisher("/ackermann_cmd_mux/input/default", AckermannDriveStamped, queue_size=10)

        # onlyfiles = [f for f in listdir(DIR) if isfile(join(DIR, f))]
        # print(onlyfiles)
        # # initialize neural net
        # self.model = ConvNet().to(self.device)
        # self.load(DIR+"/model.pt")
        # print(type(self.model))

        # initialize publishing command variables
        self.cmd_pub = rospy.Publisher('/husky_1/cmd_vel', TwistStamped, queue_size=10)
        self.forward_speed = 1000
        self.hz = 50
        self.now = rospy.get_rostime()
        self.ready = True

    def load(self,path):
        checkpoint = torch.load(path)
        self.model.load_state_dict(checkpoint['model_state_dict'])

    def image_stream_callback(self, image_msg, depth_msg):
        if self.ready:
            try:
                # grab nn output from image stream
                start = time.time()
                
                cv_image = self.bridge.imgmsg_to_cv2(image_msg, "bgr8")
                cv_depth = self.bridge.imgmsg_to_cv2(depth_msg)
                cv_image = np.array([cv_image.transpose((2,0,1))]).squeeze()
                cv_image = np.stack([cv_image[0], cv_image[1], cv_image[2], cv_depth])

                # cv_image = torch.Tensor(cv_image).to(self.device)
                # steer = self.model(cv_image)
                # output = torch.argmax(steer)
                #print(steer.detach().numpy())
                # print(output)
                # publish to /husky_1/cmd_vel
                #cmd = TwistStamped()
                #cmd.twist.linear.x = self.forward_speed
                #cmd.twist.angular.z = model_out
                #cmd.header.stamp.secs = self.now.secs
                #cmd.header.stamp.nsecs = self.now.nsecs
                #self.cmd_pub.publish(cmd)
                """
                if steer > 0.34:
                    steer = 0.34
                if steer < -0.34:
                    steer = -0.34
                """
                steer = 0
                ack_msg = AckermannDriveStamped()
                ack_msg.header.stamp = rospy.Time.now()
                ack_msg.drive.speed = 2
                ack_msg.drive.steering_angle = steer
                #self.ack_pub.publish(ack_msg)
                print(time.time()-start)
                                    
            except CvBridgeError as e:
                print(e)
    
    def run(self):
        rate = rospy.Rate(self.hz)
        while not rospy.is_shutdown():
            rate.sleep()

if __name__ == '__main__':
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    nn = NNRunner(device)
    nn.run()