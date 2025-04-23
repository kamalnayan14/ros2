import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class ClearClient(Node):
    def __init__(self):
        super().__init__('clear_client')
        self.client = self.create_client(Empty, '/clear')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /clear service...')
        self.call_clear_service()

    def call_clear_service(self):
        req = Empty.Request()
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        self.get_logger().info('Turtle path cleared!')

def main(args=None):
    rclpy.init(args=args)
    node = ClearClient()
    node.destroy_node()
    rclpy.shutdown()
