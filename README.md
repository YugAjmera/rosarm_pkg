# Robotic Arm based on ROS - ROSARM

> `cd catkin_ws/src`
> `catkin_create_pkg rosarm_pkg rospy rviz controller_manager gazebo_ros joint_state_publisher robot_state_publisher urdf`
>  Clone this repo here and replace the files in rosarm_pkg
> `cd ..` (Go back to catkin_ws/)
> `mv src/rosarm_pkg/rosarm_moveit_config src`
> `catkin_make`
> `source ./devel/setup.bash`


1. To view the model in RVIZ (using joint_state_publisher gui): `roslaunch rosarm_pkg urdf_rviz_view.launch`

3. To view the model without controllers in Gazebo : `roslaunch rosarm_pkg urdf_gazebo_view.launch  ` 
   (Note: The links will fall down due to gravity)

4. To launch the model with controllers in Gazebo : `roslaunch rosarm_pkg urdf_trajectory_controller.launch `

5. To control the arm with MoveIt (keep 2 running): `roslaunch rosarm_moveit_config rosarm_planning_execution.launch` 

![](Screenshot%20from%202019-02-02%2022-07-05.png)

6. To display the postion of end effector : `roslaunch rosarm_pkg get_Pose.launch `

7. To make the robot move on a praticular trajectory (keep 2 and 3 running): `roslaunch rosarm_pkg planning.launch `
