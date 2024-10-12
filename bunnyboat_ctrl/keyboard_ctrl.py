import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32
from std_msgs.msg import Float64


class keyboardlistener(Node):

    def __init__(self):
        super().__init__('keyboard_ctrl')

        # subscribe to /keyboard/keypress topic
        self.subscription = self.create_subscription(
            Int32,
            '/keyboard/keypress',
            self.listener_callback,
            10)

        # publish to gazebo thrusters topic
        self.leftpub = self.create_publisher(
                Float64,
                '/wamv/thrusters/left/thrust',
                10)
        self.rightpub = self.create_publisher(
                Float64,
                '/wamv/thrusters/right/thrust',
                10)

    def listener_callback(self, msg):
        leftspeed=Float64()
        rightspeed=Float64()
        leftspeed.data=0.0
        rightspeed.data=0.0
        # keyboard input
        match msg.data:
            case 87: #w
                self.get_logger().info('move forward')
                leftspeed.data=1500.0;
                rightspeed.data=1500.0;
            case 65: #a
                self.get_logger().info('move left')
                rightspeed.data=1500.0;
            case 83: #s
                self.get_logger().info('move backward')
                leftspeed.data=-1500.0;
                rightspeed.data=-1500.0;
            case 68: #d
                self.get_logger().info('move right')
                leftspeed.data=1500.0;
        # publish speeds to thruster topics
        self.leftpub.publish(leftspeed)
        self.rightpub.publish(rightspeed)


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


