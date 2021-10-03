# ROS_car_sensors_recorder
The documentation of my ROS project for TAU

# ROS Car Sensors Recorder Documentation
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

### if you are having trouble with a specific ip address, you add a specific rule to the routing table, for example time server:

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

Reset the mechine...

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


	
	
	
