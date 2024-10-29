# bunnyboat_ctrl
Launch files, navigation scripts, and more!
## how to use:
1. run `git clone git@github.com:snipchu/bunnyboat_ctrl.git` in your src directory
2. in your root directory, run `colcon build`
3. run nodes with `ros2 run bunnyboat_ctrl {node_name_here}`
4. run launch files with `ros2 launch bunnyboat_ctrl {launch_file_name_here}`

## nodes:
- keyboard_ctrl: WASD Keyboard controller for Gazebo

## launch files:
- gazebo.launch.py - launches gazebo and keyboard bridges, a combination of:
	- `ros2 launch vrx_gz competition.launch.py` - Gazebo launcher
	- `ros2 run ros_gz_bridge parameter_bridge /keyboard/keypress@std_msgs/msg/Int32@gz.msgs.Int32` - Ros/Gazebo bridge for handling keyboard input
	- `ros2 run bunnyboat_ctrl keyboard_ctrl`
