#! /usr/bin/env python
import sys
import rospy
import moveit_commander

moveit_commander.roscpp_initialize(sys.argv)

rospy.init_node('get_Pose')

group = moveit_commander.MoveGroupCommander("manipulator")

print "Current Pose:"
print group.get_current_pose()

moveit_commander.roscpp_shutdown()
