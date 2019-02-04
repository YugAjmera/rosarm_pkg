#! /usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg



moveit_commander.roscpp_initialize(sys.argv)

rospy.init_node('planning_node', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("manipulator")

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

pose_target = geometry_msgs.msg.Pose()

pose_target.orientation.x =-0.228774278247
pose_target.orientation.y = -0.619422375218
pose_target.orientation.z = 0.175240006344
pose_target.orientation.w = 0.730252826676

pose_target.position.x = 0.0918593523015
pose_target.position.y = 0.816905790045
pose_target.position.z = 0.903761804189


group.set_pose_target(pose_target)

plan1 = group.plan()

rospy.sleep(5)

moveit_commander.roscpp_shutdown()
