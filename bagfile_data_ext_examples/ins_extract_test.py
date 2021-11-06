#!/usr/bin/env python 

import rosbag

import sys

from datetime import datetime
import rospy

# check for 1 arg 
if len(sys.argv) != 2:
    exit(-1)
# bagfile name as an argument, for example 'test2.bag'
bag=rosbag.Bag(sys.argv[1]) 
x_acel_array = []
# printing in a loop over all the msgs in the bag file, that are related to the lidar points cloud.

for topic,message,timestamp in bag.read_messages(topics=['/Inertial_Labs/sensor_data']):
    temp_x_accel = message.Accel.x
    print(str(temp_x_accel))

    x_acel_array.append(temp_x_accel)
    time_date = datetime.fromtimestamp(timestamp.to_time())
    print(time_date)


