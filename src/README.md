# FRA501_exam1_6414_6462
turtlesim examination is focused on the DevOps subject and encompasses a study of ROS2 custom packages, demonstrating various fundamental functionalities of ROS2.

# Getting Started with ROS
1. create a folder ```/[your_workspace]```
2. create ```src``` in ```/[your_workspace]```
3. edit ```~/.bashrc```
```
source /opt/ros/humble/setup.bash
source ~/[your_workspace]/install/setup.bash
```
4. in ```/[your_workspace]``` floder, run
```
colcon build
```
5. in```/src``` folder, run (recommend to download asZIP file)
```
git clone https://github.com/pukkuu/FRA501_exam1_6414_6462.git
```
6. build "turtlesim_plus" in your workspace.
```
cd ~/[your_workspace]
colcon build
source install/setup.bash
```

# Testing turtlesim
1. Terminal : Run turtlesim_node
```
ros2 launch controller multiple_turtle.launch.py
```

# Conclusion
![image](https://github.com/kayyyak/FRA501_exam1_6414_6462/assets/61357514/3f40817d-e90f-479b-8ba6-c596f6be5616)
![image](https://github.com/kayyyak/FRA501_exam1_6414_6462/assets/61357514/0586a077-d3d3-4bf8-a4e8-6c027099015d)
This system architecture outlines the operations of 'turtlesim_plus' as follows:

1. **Turtle Spawning:**
   - The system is designed to spawn 4 turtles named 'foxy,' 'noetic,' 'humble,' and 'iron.'

2. **Controller Node:**
   - A dedicated controller node is implemented to handle the configuration of parameters, such as angular gain, linear gain, and tolerance. This node facilitates the effective control of the turtles.

3. **Path Definition viapoints:**
   - Mathematical equations are utilized to define viapoints that form the path for the 4 turtles. These viapoints are then stored in a YAML file, providing a structured and accessible format for the path configuration.

4. **Scheduler Node and Pizza Inventory Management:**
   - The system incorporates a scheduler node responsible for managing various tasks, including the distribution of waypoints to the turtles. Additionally, this node serves as a repository for storing pizza inventory, with a capacity of 20 pieces, ensuring efficient pizza management and distribution for the turtles.
