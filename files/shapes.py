#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import pi, sqrt

def move_forward(turtle_pub, distance):
    vel_msg = Twist()
    vel_msg.linear.x = 1.0  # Linear velocity
    distance_moved = 0
    rate = rospy.Rate(10)  # 10 Hz

    while distance_moved < distance:
        turtle_pub.publish(vel_msg)
        rate.sleep()
        distance_moved += abs(vel_msg.linear.x / 10.0)

def rotate(turtle_pub, angle):
    vel_msg = Twist()
    vel_msg.angular.z = 1.0  # Angular velocity
    angular_moved = 0
    rate = rospy.Rate(10)  # 10 Hz

    while angular_moved < angle:
        turtle_pub.publish(vel_msg)
        rate.sleep()
        angular_moved += abs(vel_msg.angular.z / 10.0)

def make_square(turtle_pub):
    for _ in range(4):
        move_forward(turtle_pub, 2.0)  # Move forward 2 units
        rotate(turtle_pub, pi/2)       # Rotate 90 degrees (pi/2 radians)

def make_star(turtle_pub):
    for _ in range(5):
        move_forward(turtle_pub, 2.0)  # Move forward 2 units
        rotate(turtle_pub, 2*pi/5)     # Rotate 144 degrees (2*pi/5 radians)

def make_triangle(turtle_pub):
    for _ in range(3):
        move_forward(turtle_pub, 2.0)  # Move forward 2 units
        rotate(turtle_pub, 2*pi/3)     # Rotate 120 degrees (2*pi/3 radians)

if __name__ == '__main__':
    try:
        rospy.init_node('turtle_shapes', anonymous=True)
        turtle_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        
        # Wait for the turtle simulator to start
        rospy.sleep(1)
        
        # Make a square
        make_square(turtle_pub)
        
        # Pause briefly
        rospy.sleep(1)
        
        # Clear the screen
        turtle_pub.publish(Twist())

        # Move to a new position for the star
        rospy.sleep(1)
        rotate(turtle_pub,3.0)
        move_forward(turtle_pub, 2.0)
        
        # Make a star
        make_star(turtle_pub)

        # Pause briefly
        rospy.sleep(1)

        # Clear the screen
        turtle_pub.publish(Twist())

        # Move to a new position for the triangle
        rospy.sleep(1)
        rotate(turtle_pub,4.0)
        move_forward(turtle_pub, 2.0)

        # Make a triangle
        make_triangle(turtle_pub)

        # Stop the turtle
        turtle_pub.publish(Twist())
        
    except rospy.ROSInterruptException:
        pass