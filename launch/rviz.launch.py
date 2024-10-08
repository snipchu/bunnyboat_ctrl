from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('vrx_gazebo'),'launch', 'rviz.launch.py')
            )
        ),
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            remappings=[('keyboard/keypress', 'keyboard/keypress@std_msgs/msg/Int32@gz.msgs.Int32')]
        ),
        Node(
            package='bunnyboat_ctrl',
            executable='keyboard_ctrl'
        )
    ])
