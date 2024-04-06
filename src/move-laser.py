import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from math import inf, isinf


# Laser scan subscriber callback
#
# Rate of readings is in gazebo tag in URDF file (20)
#
# NOTE: min ignores inf
def laser_callback(msg):
    print("Minimum distance is: ", min(msg.ranges))


# Publish velocity
def main():
    # Initialize ROS node
    rospy.init_node('move_laser_distance', anonymous=True)

    # Declare pub/sub
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    laser_sub = rospy.Subscriber('laser/scan', LaserScan, laser_callback)

    cmd = Twist()
    laser_msg = LaserScan()
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        cmd.linear.x = 0.5
        cmd.angular.z = 0.5
        vel_pub.publish(cmd)
        rate.sleep()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass