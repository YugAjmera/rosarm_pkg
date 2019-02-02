# Robotic Arm based on ROS - ROSARM

1. `cd catkin_ws/src`
2. `catkin_create_pkg rosarm_pkg rospy rviz controller_manager gazebo_ros joint_state_publisher robot_state_publisher urdf`
3. Clone this repo here and replace the files in rosarm_pkg
3. `cd ..`
4. `catkin_make`
5. `source ./devel/setup.bash`


To view the model in RVIZ (using joint_state_publisher gui): `roslaunch rosarm_pkg urdf_rviz_view.launch`

To launch the model with controllers in Gazebo : `roslaunch rosarm_pkg urdf_trajectory_controller.launch `

To control the arm with MoveIt : `roslaunch rosarm_moveit_config rosarm_planning_execution.launch` 

