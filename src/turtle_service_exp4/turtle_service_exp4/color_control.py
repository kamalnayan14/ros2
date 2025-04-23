import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from geometry_msgs.msg import Twist

class ColorPenControl(Node):
    def __init__(self):
        super().__init__('color_pen_control')
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pen_client = self.create_client(SetPen, '/turtle1/set_pen')
        self.current_side = None  # 'left' or 'right'
        self.cmd_msg = Twist()
        self.timer = self.create_timer(0.1, self.move_turtle)

        # Initial forward motion
        self.cmd_msg.linear.x = 2.0
        self.cmd_msg.angular.z = 0.0

    def pose_callback(self, pose):
        # Pen color logic
        if pose.x < 5.5 and self.current_side != 'left':
            self.change_pen(0, 255, 0)  # Green
            self.current_side = 'left'
        elif pose.x >= 5.5 and self.current_side != 'right':
            self.change_pen(255, 0, 0)  # Red
            self.current_side = 'right'

        # Edge detection and turning
        if pose.x < 1.0 or pose.x > 10.0 or pose.y < 1.0 or pose.y > 10.0:
            self.cmd_msg.angular.z = 1.5  # Turn to avoid wall
        else:
            self.cmd_msg.angular.z = 0.0  # Go straight

    def move_turtle(self):
        self.cmd_pub.publish(self.cmd_msg)

    def change_pen(self, r, g, b):
        if not self.pen_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().error('SetPen service not available')
            return
        req = SetPen.Request()
        req.r = r
        req.g = g
        req.b = b
        req.width = 2
        req.off = 0
        self.pen_client.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    node = ColorPenControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
