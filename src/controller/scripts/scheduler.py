#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from controller_interfaces.srv import SetTarget, Notify
from turtlesim_plus_interfaces.srv import GivePosition
from std_srvs.srv import Empty
import argparse
import yaml

class DummyNode(Node):
    def __init__(self, file_path: str):
        super().__init__('scheduler')
        self.create_timer(0.01, self.timer_callback)
        self.declare_parameter('storage_size', 20)
        self.declare_parameter('turtle_role', 'spawner')

        self.create_service(Notify, "scheduler/notify", self.notify_callback)
        self.settarget_client = self.create_client(SetTarget, "controller/set_goal")
        self.status = True

        self.spawn_pizza_client = self.create_client(GivePosition, "/spawn_pizza")
        self.eat_pizza_client = self.create_client(Empty, "eat")

        with open(file_path, 'r') as file:
            self.data = yaml.load(file, Loader=yaml.SafeLoader)['via_point']
        self.counter = 0
        self.timer_counter = 0

        self.storage = self.get_parameter('storage_size').value
        self.role = self.get_parameter('turtle_role').value

    def notify_callback(self, request, response):
        if request.status:
            self.status = True
        if self.status:
            if self.role == 'spawner':
                position_request = GivePosition.Request()
                position_request.x = self.data[self.counter][0]
                position_request.y = self.data[self.counter][1]
                self.counter = self.counter + 1
                self.spawn_pizza_client.wait_for_service()
                self.spawn_pizza_client.call_async(position_request)
            else:
                self.eat_pizza_client.call_async(Empty.Request())
        response.result = True
        return response    

    def timer_callback(self):
        if self.status:
            if self.counter < len(self.data) - 1:
                target_request = SetTarget.Request()
                target_request.target.x = self.data[self.counter][0]
                target_request.target.y = self.data[self.counter][1]
                self.settarget_client.call_async(target_request)
                self.status = False
                
            elif self.counter < len(self.data):
                self.timer_counter = self.timer_counter + 0.01
                if self.timer_counter >= 5:
                    target_request = SetTarget.Request()
                    target_request.target.x = self.data[self.counter][0]
                    target_request.target.y = self.data[self.counter][1]
                    self.settarget_client.call_async(target_request)
                    self.status = False

def main(args=None):
    parser = argparse.ArgumentParser(description='schedule via points')
    parser.add_argument('-f', '--file', help='path to the YAML file of via points')
    parser_args, remaining_args = parser.parse_known_args(args=args)

    rclpy.init(args=remaining_args)
    node = DummyNode(parser_args.file)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
