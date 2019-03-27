# Robotic Arm based on ROS - ROSARM

### Getting Started

- `cd catkin_ws/src`
-  Clone this repo here : `git clone "https://github.com/YugAjmera/rosarm_pkg"`
- `cd ..` (Go back to catkin_ws/)
- `catkin_make`
- `source ./devel/setup.bash`
- `source ~/.bashrc`


### Run

1. To view the model in RVIZ (using joint_state_publisher gui): `roslaunch rosarm_pkg urdf_rviz_view.launch`

2. To view the model without controllers in Gazebo : `roslaunch rosarm_pkg urdf_gazebo_view.launch  ` 
   (Note: The links will fall down due to gravity)

3. To launch the model with controllers in Gazebo : `roslaunch rosarm_pkg urdf_trajectory_controller.launch `


4. To control the arm with MoveIt (keep 3 running): `roslaunch rosarm_moveit_config rosarm_planning_execution.launch` 

![](Screenshot%20from%202019-02-02%2022-07-05.png)

5. To display the postion of end effector : `roslaunch rosarm_pkg get_Pose.launch `

6. To make the robot move on a praticular trajectory (keep 2 and 3 running): `roslaunch rosarm_pkg planning.launch `
