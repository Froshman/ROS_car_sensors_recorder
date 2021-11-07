
# Quick Start Manual

[Sensors Recording System for an Autonomous Vehicle in ROS(tm) - Quick Start Manual - Google Drive link](https://docs.google.com/document/d/1BEWxHOKF9vBZvdGs-j5YQ_qCclS9EgjoTSHT-McFybo/edit?usp=sharing "Quick Start Manual")

# ROS Car Sensors Recorder Documentation

## includes:

    ROS setup
    Network setup
    Prosilica camera
    Velodyne lidar
    Delphi Esr radar
    INS-DL
    Time Server
    rqt plugin creation
    bag file data extraction 

***
## ROS Installation

We chose to install ROS melodic, this version on combatable with ubuntu 18 and works with most packet for our sensors.

ROS melodic installation was based on the tutorial on the ROS site.

based on : http://wiki.ros.org/melodic/Installation/Ubuntu

The following cmds were called in the terminal in order to install ROS:
	
Set up keys:

    	$ sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
	
make sure Debian package index is up-to-date:

    	$ sudo apt update
		
Install: ROS, rqt, rviz, robot-generic libraries, 2D/3D simulators and 2D/3D perception:

    	$ sudo apt install ros-melodic-desktop-full
		
Sourcing paths and Environment:
    
		$ source /opt/ros/melodic/setup.bash
		
Creating a catkin workspace:

		# making a workspace folder
		$ mkdir -p ~/catkin_ws/src
		
		# once inside catkin_ws folder run:
		$ catkin_make
		
		( in order to support python3 for ROS packages, run: $ catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3 )
		( We ran: $ catkin_make )
		
		# in order to easily run installed ROS packages, you need to source the devel folder
		# so each time after a building or making a workspace run:
		$ source devel/setup.bash
		
Edit ~/.bashrc file to include "source ~/catkin_ws/devel/setup.bash":

		$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
		(needed so we could use the installed packets without sourcing each boot)

***
## Network configuration

### How to properly configurative network settings on linux: 

Go to network settings: (based on windows configuration)

interface enp0s31f6: (connects to the velodyne lidar)
	
	Identity:
		pick a recognizable Name for the device
	
	IPv4 setting:
		
		Set to Manual mode and fill the Addresses:
		
		Address			Netmask			Comments	
		192.168.1.101	255.255.255.0	Switch1
		192.168.0.30	255.255.255.0
		10.1.1.101		255.255.0.0
		
		(don't enter Gateways)
		
interface enp1s0: (connects to camera)
	
	Identity:
		pick a recognizable Name for the device
	
	IPv4 setting:
		
		Set to Manual mode and fill the Addresses:
		
		Address			Netmask			Comments	
		192.168.10.100	255.255.255.0	Switch2
		192.168.1.100	255.255.255.0
		132.4.6.100		255.255.255.0
		10.1.1.100		255.255.255.0
		
		(don't enter Gateways)
		
		
For both interfaces keep the IPv6 settings on Automatic

The Network should be working properly after entering these setting,
and you should be able to communicate with the ip/tcP connected sensors.

### in case of emergency, if you are having trouble with a specific ip address,
### you can add a specific rule to the routing table, for example time server:

        $ sudo ip route add 192.168.1.20 via 192.168.1.100 dev enp1s0

### you can also check the ip routing table via:

        $ ip route

***
## Vision Allied - GT1930c Prosilica:


Reference:\
	https://www.alliedvision.com/en/products/software.html#c6444
	https://cdn.alliedvision.com/fileadmin/content/documents/products/software/software/Vimba/appnote/Vimba_installation_under_Linux.pdf
	

Download Vimba: https://www.alliedvision.com/en/products/software.html#c6444
	 
	 unpack: $ tar -xzf ./Vimba_v4.2_Linux.tgz Vimba_4_2/ -C /opt
	
Install VimbaGigeTL:

	# inside ~/Vimba_4_2/VimbaGigETL, run:
	$ sudo ./Install.sh

Reset the machine...

Install the following dependencies:

	sudo add-apt-repository ppa:rock-core/qt4
	sudo apt-get update
	sudo apt-get install libqtcore4
	sudo apt-get install libqt4-network --fix-missing
	sudo apt-get install libqt4-qt3support
	
Add the following line to the ~/bashrc file:

	export GENICAM_GENTL64_PATH=$GENICAM_GENTL64_PATH:"/PATH_TO_VIMBAFOLDER/VimbaGigETL/CTI/x86_64bit/"

To build Vimba:

	sudo apt-get install pkg-config
	sudo apt-get install libqt4-dev
	sudo apt-get install libcanberra-gtk-module

Check if you can reach the camera via VimbaVeiwer:

..not really working for us, but you can view check the camera config via:

		sudo -E ./VimbaViewer
	
Installing ROS packets:

	prosilica_gige_sdk
	prosilica_driver

	
Build your workspace:

	$ cd ~/catkin_ws/ && catkin_make
	$ source devel/setup.bash
	
Installation is complete.

### How to View the Camera Data: 


(First time only) go to prosilica_camera ROS launch folder:

edit the camera ip to: 192.168.10.150 in the following files:

		generic.launch    prosilica.launch  streaming.launch
	
Launch the camera ROS nodes:

		$ roslaunch prosilica_camera generic.launch
		
Now you should view the camera feedback via rqt_image_view or rviz
	
	
### NOTE:  we are interstered in the '/prolica/image_raw' topic to record our data!

***
## Velodyne LP16:

reference:\
 http://wiki.ros.org/velodyne/Tutorials/Getting%20Started%20with%20the%20Velodyne%20VLP16

Check if you can reach the configuration page in the web browser at:\
http://192.168.1.201/
<br/><br/>
Installing ROS dependencies:

    	$ sudo apt-get install ros-melodic-velodyne
	
Installing the VLP16 driver:

	$ cd ~/catkin_ws/src/ && git clone https://github.com/ros-drivers/velodyne.git
	$ rosdep install --from-paths src --ignore-src --rosdistro melodic -y
	
Build your workspace:

	$ cd ~/catkin_ws/ && catkin_make
	$ source devel/setup.bash
	
Installation is complete.
<br/><br/>
### How to View the Lidar Data: 
	
	$ roslaunch velodyne_pointcloud VLP16_points.launch
	
	$ rosrun rviz rviz -f velodyne 
	
to view the points, add the '/velodyne_points' topic to the screen in rviz.

	
### NOTE:  we are interstered in the '/velodyne_points' topic to record our data!
***

## Delphi - ESR 2.5 Radar:

Reference:\
https://scratchrobotics.com/2020/08/17/visualize-delphi-esr-radar-with-ros-rviz-and-autonomousstuff-driver/
https://github.com/ancabilloni/ros-delphi-esr-visualization


Install AutonomousStuff Delphi ESR Driver:

	$ sudo apt update && sudo apt install apt-transport-https
	$ sudo sh -c 'echo "deb [trusted=yes] https://s3.amazonaws.com/autonomoustuff-repo/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/autonomoustuff-public.list'
	$ sudo apt update
	$ sudo apt install ros-$ROS_DISTRO-delphi-esr
	
After installation, you can the launch sample file provided in this driver,	and checkout their list of topics:
	
	$ roslaunch delphi_esr delphi_esr.launch
	$ rostopic list
	
Radar topics list and info:\
	 https://autonomoustuff.atlassian.net/wiki/spaces/RW/pages/17509820/Delphi+ESR
	
To see more detail of the sample launch files, they are located here:

	$ cd /opt/ros/$ROS_DISTRO/share/delphi_esr/
	
Install ROS socketcan_bridge:
	For the convenience of reading raw logged CAN frames,
	socketcan_bridge is a good option because user can assign the CAN interface at launch file.
	
	$ sudo apt install ros-$ROS_DISTRO-socketcan-bridge
	$ sudo apt update

Download the git files:

	$ git clone https://github.com/ancabilloni/ros-delphi-esr-visualization.git
	(i did it inside /opt/ros/melodic/share/delphi_esr/)
	
	# Bring up virtual can interface
	$ sudo ./setup_vcan.sh
	
	# edit master.lauch to include: `"use_socketcan:="true"`
	# I've renamed defualt.rviz (downloaded from the github) to esr.rviz
	# another edit in master.lauch to include:
    
        <node type="rviz" name="rviz" pkg="rviz" args="-d /opt/ros/melodic/share/delphi_esr/launch/esr.rviz" />
    (or anyother path to esr.rviz)
	

 Installation is complete.

### Can Setup:
	
every time you reboot run:

		$ sudo modprobe can
		$ sudo modprobe can_raw
		$ sudo ip link set can0 type can bitrate 500000
		$ sudo ip link set up can0
		
you can create a service in order to avoid running these commands after every boot:
	
	create a script file 'radar_can0_boot_script' in convenient for you location (/home/administrator/):
			
		  radar_can0_boot_script:

			#!/bin/sh
			# setting up lidar settings
			modprobe can
			modprobe can_raw
			ip link set can0 type can bitrate 500000
			ip link set up can0
		  
		  *note: dont used 'sudo' prefix inside the script.
		
	make it executable:

			$ chmod 775 radar_can0_boot_script
		
	navigate to /etc/systemd/system and create there a service file.

			$ cd /etc/systemd/system 
			$ sudo gedit /etc/systemd/system/radar_can0_boot_script.service
			
			  radar_can0_boot_script.service:
				[Unit]
				Description=Setup Network Setting for ROS Radar sensor

				[Service]
				Type=oneshot
				ExecStart=/bin/sh /home/administrator/radar_can0_boot_script

				[Install]
				WantedBy=multi-user.target
			
	    	* Where ExecStart points to run your script with /bin/sh
		
	enable the systemd service:

			$ sudo systemctl enable radar_can0_boot_script.service
			
	Now the radar launch file should work everytime! (even after reboot)

### How to View the Radar Data: 
	
	$ roslaunch delphi_esr master.launch


make you read and understand the launch you just used
	
### NOTE:  we are interstered in the '/as_tx/radar_markers' topic to record our data!
### NOTE:  to view raw cam0 data:

	$ candump can0

***
# Inertiallabs - INS-DL:

Reference: \
https://resources.inertiallabs.com/en-us/knowledge-base/inertial-labs-ros-driver-package
	https://us.inertiallabs.com:31443/projects/INS/repos/inertiallabs-ros-pkgs/browse
	
	
### Install Inertiallabs INS-DL ROS-Packet:
<br/>
get git files and copy to work station and build:
	
		$ cd <your_work_space>/src
		$ git clone https://us.inertiallabs.com:31443/scm/ins/inertiallabs-ros-pkgs.git
		
edit the following line in /catkin_ws/src/inertiallabs-ros-pkgs/inertiallabs_ins/src/il_ins.cpp:
		
		from:

				np.param<std::string>("ins_url", port, "serial:/dev/ttyUSB0:460800");

		to:

				np.param<std::string>("ins_url", port, "serial:/dev/ttyS3:115200");
		
edit the launch file accordingly in the launch folder
		
		$ cd <your_work_space>	
		$ catkin_make
		$ source devel/setup.bash
	

Connection:

	the device is connected to COM4 (physical and also could be seen in windows10).
	in linux(ubuntu) it is ttyS3.
	
	so we should expect to read the searial data via:
		
		/dev/ttyS3
		

Set-up user permissions:
	
	add user to dialout group: (not sure if necessary)
		find out your user:

		    $ whoami
		
	    $ sudo adduser administrator dialout
	    *(administrator is the user)
	
    make sure it worked

	    $ groups administrator
	
		
Set-up user permission for serial connection:
		
	Might need to do this every time system boots
		
		$ sudo chmod 666 /dev/ttyS3

Installation is complete.
<br/><br/>

### How to View the INS Data: 

	To view data:
	
		$ rosrun inertiallabs_ins il_ins
		
	the use rqt or rostopic echo on the relevant topics.
	

### NOTE:  we are interstered in the '/Inertial_Labs/sensor_data' or/and '/Inertial_Labs/ins_data' topic to record our data! (there 2 more topics with data)
***
## TimeMachines - Time Server TM2000A

### make sure your network is cofigured right:

Try to connect to the Time Server config page via: (http) 192.168.1.20

		user: admin
		password: tmachine
	
if you cant connect you can add new route with ip Command;
	
		$ sudo ip route add 192.168.1.20 via 192.168.1.100 dev enp1s0

(might need to do it every reboot or add to bash.sh)
		
We are planning on syncing Time server via crony:
	time server --> crony --> kernal --> ROS master
	
***
# rqt plugin creation
Intro:\
For the gui part of the project we decided to base it on ROS rqt_gui packages, since some of the packages were already useful
and the docking and the save/load presentation features helped very much with its flexebility and time saving.
<br/><br/>


the basic creation proses is based on the next tutorial:

https://www.programmersought.com/article/46843686253/
<br/><br/>

all of the basic code files were copied and some filenames\parameters were renamed to better suit our new rqt plugin purpuse.
The Ui file was edited via qt designer, which turned out to be a great tool.

to better understand PyQT the following youtube tutorial playlist was used:

https://www.youtube.com/playlist?list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj
<br/><br/>
	
Note: the main functionality is similar but were using python packages under a different name (qt_gui.plugin , python_qt_binding).
***
# bag file data extraction

bag file data is saved as a set of messages ordered by time stamps per topic.
there is no one universal way to do it, it's possible to think of many different data structures of csv files for each message type.
<br/><br/>


it is possible to "rosbag play" the bag file from shell and save the output by echoing the wanted topic into a text file.
<br/><br/>


it is also possible to go over the bag file inside a python script, going over the messages in a loop manner while creating any type of file
  or doing any computation or analysis or filtering wanted by the script creator.

there are many types of available scripts/programs/ros-packages to perform such tasks, including matlab libraries to deal with ros and bag files.

for example:\
https://www.mathworks.com/help/ros/ref/rosbag.html


another one of them is rosbag_to_csv by AtsushiSakai, at https://github.com/AtsushiSakai/rosbag_to_csv

<br/>


we installed the rosbag_to_csv ros-package (by following the readme file, but used catkin_make) and tested it on a rosbag file we recorded earlier.\
  (also installed libcanberra-gtk-module libcanberra-gtk3-module via 'sudo apt install libcanberra-gtk-module libcanberra-gtk3-module')\
it created a csv file for each selected topic, the csv format is based on the fields of the message type of the topic.\
it preformed successfully with INS and Radar data, however the lidar message format would require a different approach.

maybe a custom script that would create a csv file in a desired format for pointcould2 type of message (check http://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/PointCloud2.html,\
or use matlab: 
https://www.mathworks.com/help/ros/ref/pointcloud2.html).


