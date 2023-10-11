from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    x_launch_arg = DeclareLaunchArgument('x', default_value='0.0')
    y_launch_arg = DeclareLaunchArgument('y', default_value='0.0')
    name_launch_arg = DeclareLaunchArgument('name')

    x = LaunchConfiguration('x')
    y = LaunchConfiguration('y')
    name = LaunchConfiguration('name')

    kill_turtle = ExecuteProcess(cmd= ["ros2 service call /remove_turtle turtlesim/srv/Kill \"{name: 'turtle1'}\""], shell=True)

    spawn_cmd = LaunchConfiguration('cmd', default=[
        'ros2 service call /spawn_turtle turtlesim/srv/Spawn "{x: ',
        x,
        ', y: ',
        y,
        ', theta: 0.0, name: \'',
        name,
        '\'}"'
    ])
    spawn_turtle = ExecuteProcess(cmd= [[spawn_cmd]], shell=True)

    launch_description = LaunchDescription()
    launch_description.add_action(x_launch_arg)
    launch_description.add_action(y_launch_arg)
    launch_description.add_action(name_launch_arg)
    launch_description.add_action(kill_turtle)
    launch_description.add_action(spawn_turtle)
    return launch_description