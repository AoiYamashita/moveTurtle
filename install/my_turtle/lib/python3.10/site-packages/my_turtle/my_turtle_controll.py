import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist

class Controller(Node):
    def __init__(self):
        super().__init__("controller")
        self.publisher = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_timer(1.0, self.cb)
    def cb(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 1.0
        self.publisher.publish(msg)

def main():
    rclpy.init()
    controller = Controller()
    rclpy.spin(controller)

