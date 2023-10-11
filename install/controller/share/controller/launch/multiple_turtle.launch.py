from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory


def generate_launch_description():

    turtlesim = Node( 
        package='turtlesim_plus', 
        executable='turtlesim_plus_node.py'
    )

    spawn_Foxy = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('controller')
                        , 'launch', 'via_point_follower.launch.py'),
        ), launch_arguments={
            'name': 'Foxy',
            'file': 'via_point.yaml',
            'role': 'spawner_config.yaml',
            'letter': 'F'
        }.items()
    )

    spawn_Noetic = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('controller')
                        , 'launch', 'via_point_follower.launch.py'),
        ), launch_arguments={
            'name': 'Noetic',
            'file': 'via_point.yaml',
            'role': 'spawner_config.yaml',
            'letter': 'I'
        }.items()
    )

    spawn_Humble = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('controller')
                        , 'launch', 'via_point_follower.launch.py'),
        ), launch_arguments={
            'name': 'Humble',
            'file': 'via_point.yaml',
            'role': 'spawner_config.yaml',
            'letter': 'B'
        }.items()
    )

    spawn_Iron = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('controller')
                        , 'launch', 'via_point_follower.launch.py'),
        ), launch_arguments={
            'name': 'Iron',
            'file': 'via_point.yaml',
            'role': 'spawner_config.yaml',
            'letter': 'O'
        }.items()
    )

    launch_description = LaunchDescription()
    launch_description.add_action(turtlesim)
    launch_description.add_action(spawn_Foxy)
    launch_description.add_action(spawn_Noetic)
    launch_description.add_action(spawn_Humble)
    launch_description.add_action(spawn_Iron)
    return launch_description