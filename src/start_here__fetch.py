#! /usr/bin/env python3

# fetch.urdf needs to be in <ros_workspace>/urdfs
urdf_file_name = 'fetch.urdf'
fixed_frame = 'base_link'
info_file_name = 'fetch_info.yaml'
# Verify the urdf looks good: 'roslaunch relaxed_ik urdf_viewer.launch'

joint_names = [ 
	[
            "torso_lift_joint",
            "shoulder_pan_joint",
            "shoulder_lift_joint",
            "upperarm_roll_joint",  # continuous
            "elbow_flex_joint",
            "forearm_roll_joint",  # continuous
            "wrist_flex_joint",
            "wrist_roll_joint",  # continous
    ]
]
joint_ordering =  [
    "torso_lift_joint",
    "shoulder_pan_joint",
    "shoulder_lift_joint",
    "upperarm_roll_joint",  # continuous
    "elbow_flex_joint",
    "forearm_roll_joint",  # continuous
    "wrist_flex_joint",
    "wrist_roll_joint",  # continous
]
ee_fixed_joints = [ 'gripper_axis' ]
starting_config = [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]

from sensor_msgs.msg import JointState
def joint_state_define(x):
	return None

# Run 'roslaunch relaxed_ik urdf_viewer.launch'. Add non-colliding joint states (they are printed to the terminal) to 
# 'collision_example_fetch.yaml'. Also add collision objects.
collision_file_name = 'collision_example_fetch.yaml'


# Generate info_file: 'roslaunch relaxed_ik generate_info_file.launch'
# Load info_file: 'roslaunch relaxed_ik load_info_file.launch info_file_name:=fetch_info.yaml'
# Test collision file: 'rosrun relaxed_ik urdf_viewer_with_collision_info.py'
# Generate self-collision nn training dataset: 'rosrun relaxed_ik generate_input_and_output_pairs.py'
# Train a self-collision nn in julia: 'roslaunch relaxed_ik preprocessing_julia.launch'

# Test that the solver is working. In three separate terminals:
# $ roslaunch relaxed_ik rviz_viewer.launch
# $ roslaunch relaxed_ik relaxed_ik_julia.launch
# $ rosrun relaxed_ik keyboard_ikgoal_driver.py
