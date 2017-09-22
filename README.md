# rotors_simulator_interface
Python example script to interface with the rotors_simulator ROS package

go to catkin_ws/src

git clone git@github.com:raultron/rotors_simulator_interface.git

to run:

First in a terminal:
roslaunch rotors_gazebo mav_hovering_example.launch mav_name:=firefly world_name:=basic

in another terminal:
rosrun rotors_simulator_interface example.py
