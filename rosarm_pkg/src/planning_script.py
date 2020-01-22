#! /usr/bin/env python
import sys
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

pose_target.orientation.x = -0.326891322694
pose_target.orientation.y = 0.649428384936
pose_target.orientation.z = 0.185509239072
pose_target.orientation.w = 0.661037940065

pose_target.position.x = 0.339562359682
pose_target.position.y = 0.096364421399
pose_target.position.z = 1.19932287634

group.set_pose_target(pose_target)

plan1 = group.plan()

group.go(wait=True)

rospy.sleep(5)

moveit_commander.roscpp_shutdown()
