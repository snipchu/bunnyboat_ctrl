import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class keyboardlistener(Node):

    def __init__(self):
        super().__init__('keyboard_ctrl')
        self.subscription = self.create_subscription(
            Int32,
            '/keyboard/keypress',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        match msg.data:
            case 87: #w
                self.get_logger().info('move forward')
            case 65: #a
                self.get_logger().info('move left')
            case 83: #s
                self.get_logger().info('move backward')
            case 68: #d
                self.get_logger().info('move backward')


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = keyboardlistener()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


