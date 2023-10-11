#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from controller_interfaces.srv import SetTarget, Notify
import math

class DummyNode(Node):
    def __init__(self):
        super().__init__('controller')
        self.declare_parameter('linear_gain', 1.0)
        self.declare_parameter('angular_gain', 10.0)
        self.declare_parameter('tolerance', 0.2)

        self.pub_cmdvel = self.create_publisher(Twist, "cmd_vel", 10)
        self.create_subscription(Pose, "pose", self.pose_callback, 10)
        self.create_timer(0.01, self.timer_callback)

        self.create_service(SetTarget, "controller/set_goal", self.set_goal_callback)
        self.notify_client = self.create_client(Notify, "scheduler/notify")

        self.target = [0.0, 0.0]
        self.current_pose = [0.0, 0.0, 0.0]
        self.enable_controller = False

        self.Kp_dis = self.get_parameter('linear_gain').value
        self.Kp_ori = self.get_parameter('angular_gain').value
        self.Max_error = self.get_parameter('tolerance').value

    def notify(self):
        notify_status = Notify.Request()
        if self.enable_controller:
            notify_status.status = False
        else:
            notify_status.status = True
        self.notify_client.call_async(notify_status)

    def set_goal_callback(self, request, response):
        if self.enable_controller:
            response.result = False
        else:
            self.target = [request.target.x, request.target.y]
            self.enable_controller = True
            response.result = True
        return response

    def pose_callback(self, msg):
        self.current_pose = [msg.x, msg.y, msg.theta]

    def cmd_vel(self, vx, w):
        cmd_vel = Twist()
        cmd_vel.linear.x = vx
        cmd_vel.angular.z= w
        self.pub_cmdvel.publish(cmd_vel)

    def timer_callback(self):
        if self.enable_controller:
            dy = self.target[1] - self.current_pose[1]
            dx = self.target[0] - self.current_pose[0]

            e_dis = math.hypot(dx, dy)
            e_ori = math.atan2(dy, dx) - self.current_pose[2]
            e_ori = math.atan2(math.sin(e_ori), math.cos(e_ori))

            u_dis = self.Kp_dis * e_dis
            u_ori = self.Kp_ori * e_ori

            if (abs(dx) < self.Max_error and abs(dy) < self.Max_error):
                self.cmd_vel(0.0, 0.0)
                self.enable_controller = False
                self.notify()
            else:
                self.cmd_vel(u_dis, u_ori)

def main(args=None):
    rclpy.init(args=args)
    node = DummyNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
