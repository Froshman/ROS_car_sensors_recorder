#!/usr/bin/env python 

import cv_bridge
import rosbag

import sys
import os

from datetime import datetime
import rospy

import cv2

from cv_bridge import CvBridge

# check for 1 arg 
if len(sys.argv) != 2:
    exit(-1)
# bagfile name as an argument, for example 'test2.bag'
bag=rosbag.Bag(sys.argv[1]) 

count = 0
bridge = CvBridge()


# printing in a loop over all the msgs in the bag file, that are related to the lidar points cloud.

for topic,message,timestamp in bag.read_messages(topics=['/image_raw']):

    cv_img = bridge.imgmsg_to_cv2(message, desired_encoding="bgr8")

    cv2.imwrite(os.path.join('bag2img', "frame" + str(count) + ".png" ), cv_img)
    print("Wrote image " + str(count))

    count += 1
    time_date = datetime.fromtimestamp(timestamp.to_time())
    print(time_date)