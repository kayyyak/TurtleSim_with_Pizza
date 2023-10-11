from launch import LaunchDescription, LaunchContext
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os
import yaml
from io import StringIO
import numpy as np
import os

def modify_config_namespace(path:str, new_path:str, namespace:str) -> None:
    with open(path, 'r') as file:
        data = yaml.load(file, Loader=yaml.SafeLoader)
    new_data = {namespace: data}
    with open(new_path, 'w') as file:
        yaml.dump(new_data, file)

def modify_via_point(path, letter):
    x_values = []
    y_values = []
        
    coordinates = alphabet(letter)

    if coordinates is None:
        print(f"Letter {letter} is not supported.")
    else:
        for coord_pair in coordinates:
            scaling_factor = 3
            scaled_x, scaled_y = scale_points(*coord_pair, scaling_factor)
            x_values.extend(scaled_x)
            y_values.extend(scaled_y)

        if letter == 'F':
            num = 1
        elif letter == 'I':
            num = 2
        elif letter == 'B':
            num = 3
        else:
            num = 4
        offset_x = (num * 2.5) - 1.5 
        offset_y = 5

        x_values = [x + offset_x for x in x_values]
        y_values = [y + offset_y for y in y_values]
        
        x_values.append(10)
        y_values.append(10)

        output_string = StringIO()
        print("via_point:", file = output_string)
        for k in range(0, len(x_values)):
            print(f"  - - {x_values[k]:.2f}", file = output_string)
            print(f"    - {y_values[k]:.2f}", file = output_string)

        with open(path, 'w') as yaml_file:
            yaml_file.write(output_string.getvalue())

def alphabet(letter):
    if (letter == 'F'):
        alphabet_coordinates = [
            (np.full(11, 0), np.linspace(0, 1, 11)),
            (np.linspace(0.1, 0.5, 5), np.full(5, 1)),
            (np.linspace(0.1, 0.4, 4), np.full(4, 0.5))
        ]
    elif (letter == 'I'):
        alphabet_coordinates = [
            (np.linspace(0, 0.4, 5), np.full(5, 0)),
            (np.full(10, 0.2), np.linspace(0, 0.9, 10)),
            (np.linspace(0, 0.4, 5), np.full(5, 1))
        ]
    elif (letter == 'B'):
        alphabet_coordinates = [
            (np.full(5, 0), np.linspace(0, 0.8, 5)),
            (np.linspace(0, 0.4, 3), np.full(3, 1)),
            (np.full(2, 0.4), np.linspace(0.8, 0.6, 2)),
            (np.linspace(0.4, 0, 3), np.full(3, 0.6)),
            (np.full(3, 0.4), np.linspace(0.4, 0, 3)),
            (np.linspace(0.4, 0, 3), np.full(3, 0))
        ]
    elif (letter == 'O'):
        alphabet_coordinates = [
            (np.full(7, 0), np.linspace(0.15, 0.85, 7)),
            (np.linspace(0.1, 0.3, 3), np.full(3, 1)),
            (np.full(7, 0.4), np.linspace(0.85, 0.15, 7)),
            (np.linspace(0.3, 0.1, 3), np.full(3, 0))
        ]
    else:
        return None
    return alphabet_coordinates

def scale_points(x, y, scaling_factor):
    scaled_x = x * scaling_factor
    scaled_y = y * scaling_factor
    return scaled_x, scaled_y

def render_node(
        context:LaunchContext,
        launch_description:LaunchDescription,
        pkg:str,
        execute:str,
        name:LaunchConfiguration,
        param,
        arg,
        letter
) -> None:
    node_pkg = get_package_share_directory(pkg)
    name_str = context.perform_substitution(name)
    if type(arg) == LaunchConfiguration:
        letter_str = context.perform_substitution(letter)
        arg_str = context.perform_substitution(arg)
        sprit_arg = arg_str.split('.')
        arg_path = os.path.join(node_pkg, 'via_point',sprit_arg[0] + '_' + name_str + '.yaml')
        modify_via_point(arg_path, letter_str)
    else:
        arg_path = ''
        
    param_path = ''
    if type(param)  == LaunchConfiguration:
        param_str = context.perform_substitution(param)
    else:
        param_str = param
    if len(param_str):
        sprit_param = param_str.split('.')
        config_param_path = os.path.join(node_pkg,'config', param_str)
        param_path = os.path.join(node_pkg, sprit_param[0] + '_' + name_str + '.yaml')
        modify_config_namespace(config_param_path, param_path, name_str)

    node = Node(
        package=pkg,
        executable=execute,
        namespace=name,
        parameters=[param_path],
        arguments=['-f', arg_path]
    )
    launch_description.add_action(node)

def generate_launch_description():
    name_launch_arg  = DeclareLaunchArgument('name')
    file_launch_arg = DeclareLaunchArgument('file')
    role_launch_arg = DeclareLaunchArgument('role')
    letter_launch_arg = DeclareLaunchArgument('letter')

    name = LaunchConfiguration('name')
    file = LaunchConfiguration('file')
    role = LaunchConfiguration('role')
    letter = LaunchConfiguration('letter')

    launch_description = LaunchDescription()

    controller_opaque = OpaqueFunction(
        function=render_node,
        args=[launch_description,
              'controller',
              'controller.py',
              name,
              'controller_config.yaml',
              '',
              '']
    )

    scheduler_opaque = OpaqueFunction(
        function=render_node,
        args=[launch_description,
              'controller',
              'scheduler.py',
              name,
              role,
              file,
              letter]
    )
    
    launch_description.add_action(name_launch_arg)
    launch_description.add_action(file_launch_arg)
    launch_description.add_action(role_launch_arg)
    launch_description.add_action(letter_launch_arg)
    launch_description.add_action(controller_opaque)
    launch_description.add_action(scheduler_opaque)
    return launch_description

