# Robotic Arm based on ROS - ROSARM

1. Create a folder named **rosarm_pkg** in catkin_ws/src
2. Clone this repository in it
3. `cd catkin_ws/`
4. `catkin_make`
5. `source ./devel/setup.bash`

To view the model in RVIZ (using joint_state_publisher gui): `roslaunch rosarm_pkg urdf_rviz_view.launch`

To launch the model with controllers in Gazebo : `roslaunch rosarm_pkg urdf_trajectory_controller.launch `
