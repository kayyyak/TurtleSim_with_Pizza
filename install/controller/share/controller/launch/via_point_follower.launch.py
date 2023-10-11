from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

def generate_launch_description():

    name_launch_arg  = DeclareLaunchArgument('name')
    file_launch_arg = DeclareLaunchArgument('file')
    role_launch_arg = DeclareLaunchArgument('role')
    letter_launch_arg = DeclareLaunchArgument('letter')

    name = LaunchConfiguration('name')
    file = LaunchConfiguration('file')
    role = LaunchConfiguration('role')
    letter = LaunchConfiguration('letter')

    spawn_turtle = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('controller')
                        , 'launch', 'spawn_turtle.launch.py'),
        ), launch_arguments={
            'x': '0.3',
            'y': '0.3' ,
            'name': name
        }.items()
    )

    controller_scheduler = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('controller')
                        , 'launch', 'controller_scheduler.launch.py'),
        ), launch_arguments={
            'name': name,
            'file': file,
            'role': role,
            'letter': letter
        }.items()
    )

    launch_description = LaunchDescription()
    launch_description.add_action(name_launch_arg)
    launch_description.add_action(file_launch_arg)
    launch_description.add_action(role_launch_arg)
    launch_description.add_action(letter_launch_arg)
    launch_description.add_action(spawn_turtle)
    launch_description.add_action(controller_scheduler)
    return launch_description
