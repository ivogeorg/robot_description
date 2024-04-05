#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

# When the odometry subscriber receives a message
# it calls the supplied callback, passing it in
def odom_callback(msg):
    print("X: ", msg.pose.pose.position.x, ", Y: ", msg.pose.pose.position.y)

def main():
    # Declare pub/sub and initialize rospy    
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    odom_sub = rospy.Subscriber ('/odom', Odometry, odom_callback)
    rospy.init_node('move_display_odom', anonymous=True)

    # Declare Twist velocity message to publish
    cmd = Twist()
    rate = rospy.Rate(10)  # for sleeping

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