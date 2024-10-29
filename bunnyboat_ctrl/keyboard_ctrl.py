import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32 # msg type of /keyboard/keypress topic
from std_msgs.msg import Float64 # msg type of /wamv/thrusters/[left/right]/thrust topic

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

    # runs every time a new keypress is detected
    def listener_callback(self, msg):
        # initialize return values to 0
        leftspeed=Float64()
        rightspeed=Float64()
        leftspeed.data=0.0
        rightspeed.data=0.0
        # keyboard input
        match msg.data:
            case 87: #w key
                self.get_logger().info('move forward')
                leftspeed.data=5500.0;
                rightspeed.data=5500.0;
            case 65: #a key
                self.get_logger().info('move left')
                rightspeed.data=5500.0;
            case 83: #s key
                self.get_logger().info('move backward')
                leftspeed.data=-5500.0;
                rightspeed.data=-5500.0;
            case 68: #d key
                self.get_logger().info('move right')
                leftspeed.data=5500.0;
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
