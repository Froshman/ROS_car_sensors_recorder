#!/usr/bin/env python 

# handle bag and pointcloud2 msg type + numpy version of ros
import ros_numpy as rnp #if missing, to install via shell: sudo apt install ros-melodic-ros-numpy
import rosbag

import sys

from datetime import datetime
import rospy

# check for 1 arg 
if len(sys.argv) != 2:
    exit(-1)
# bagfile name as an argument, for example 'test2.bag'
bag=rosbag.Bag(sys.argv[1]) 

# printing in a loop over all the msgs in the bag file, that are related to the lidar points cloud.
for topic,message,timestamp in bag.read_messages(topics=['/velodyne_points']):

    lidar_arr = rnp.point_cloud2.pointcloud2_to_xyz_array(message) #,remove_nans=True)
    time_date = datetime.fromtimestamp(timestamp.to_time())
    print(time_date)
    print(lidar_arr)
    print(lidar_arr.shape)
    print(type(lidar_arr))

