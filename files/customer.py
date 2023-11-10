#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def speak():
    
    rospy.init_node("customerNode")

    pub=rospy.Publisher("/problem",String,queue_size=10)
    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
        msg=String()
        msg.data="Hello, I am facing this problem!!"
        pub.publish(msg)
        rate.sleep()

if __name__=="__main__":
    speak()