import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class WallAvoider(Node):
    def __init__(self):
        super().__init__('wall_avoider')
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose = None
        self.timer = self.create_timer(0.2, self.control_loop)

    def pose_callback(self, msg):
        self.pose = msg

    def control_loop(self):
        if self.pose is None:
            return

        msg = Twist()

        # Avoid wall: boundary range [0.5, 10.5] for turtlesim
        if self.pose.x < 1.0 or self.pose.x > 10.0 or self.pose.y < 1.0 or self.pose.y > 10.0:
            msg.linear.x = 0.0
            msg.angular.z = 2.0  # Turn
        else:
            msg.linear.x = 2.0
            msg.angular.z = 0.0  # Go straight

        self.vel_pub.publish(msg)
        self.get_logger().info(f'Moving with x: {msg.linear.x}, z: {msg.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = WallAvoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
