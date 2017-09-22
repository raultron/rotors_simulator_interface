#!/usr/bin/env python
import rospy
#from std_msgs.msg import UInt16
#from sensor_msgs.msg import Imu
#from sensor_msgs.msg import Joy
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped




# Relevant Firefly topics:
# Command to list all the topics (with rotors already running):
# rostopic list
#
# you can find info about a particular topic using this command:
# rostopic info /NAME_OF_THE_TOPIC
#
# Example of topics were you can publish commands:
# /firefly/command/pose Type: geometry_msgs/PoseStamped
# /firefly/command/motor_speed Type: mav_msgs/Actuators
# /firefly/command/trajectory Type: trajectory_msgs/MultiDOFJointTrajectory
#
# Example of topics were you can subscribe:
#
# /firefly/ground_truth/pose Type: geometry_msgs/Pose


pub_command_pose = rospy.Publisher('/firefly/command/pose', PoseStamped, queue_size=100)

#Callback function, it is called each time that a message is published in its associated topic
def ground_truth_pose_cb(data):
    # We read first the position data
    x = data.position.x
    y = data.position.y
    z = data.position.z

    # Now the orientation quaternion
    qx = data.orientation.x
    qy = data.orientation.y
    qz = data.orientation.z
    qw = data.orientation.w

    # Do something with the data
    ##
    ##
    ##
    ##

    #Publish a new pose command for the quadcopter
    #The format is pose stamped
    pose_msg = PoseStamped()
    pose_msg.pose.position.x = 2.0
    pose_msg.pose.position.y = 0.0
    pose_msg.pose.position.z = 3.0

    pose_msg.pose.orientation.x = qx
    pose_msg.pose.orientation.y = qy
    pose_msg.pose.orientation.z = qz
    pose_msg.pose.orientation.w = qw

    pub_command_pose.publish(pose_msg)


if __name__ == '__main__':
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('rotors_simulator_interface', anonymous=True)
    rospy.Subscriber("/firefly/ground_truth/pose", Pose, ground_truth_pose_cb)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
