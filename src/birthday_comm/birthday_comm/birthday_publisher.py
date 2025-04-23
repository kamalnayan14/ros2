import rclpy
from rclpy.node import Node
from birthday_msgs.msg import Birthday

class BirthdayPublisher(Node):
    def __init__(self):
        super().__init__('birthday_publisher')
        self.publisher_ = self.create_publisher(Birthday, 'birthday', 10)
        timer_period = 2.0
        self.timer = self.create_timer(timer_period, self.publish_birthday)

    def publish_birthday(self):
        msg = Birthday()
        msg.year = 2000
        msg.month = 12
        msg.day = 25
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.year}-{msg.month}-{msg.day}')

def main(args=None):
    rclpy.init(args=args)
    node = BirthdayPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
