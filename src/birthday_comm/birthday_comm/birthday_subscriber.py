import rclpy
from rclpy.node import Node
from birthday_msgs.msg import Birthday

class BirthdaySubscriber(Node):
    def __init__(self):
        super().__init__('birthday_subscriber')
        self.subscription = self.create_subscription(Birthday, 'birthday', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'I heard: {msg.year}-{msg.month}-{msg.day}')

def main(args=None):
    rclpy.init(args=args)
    node = BirthdaySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
