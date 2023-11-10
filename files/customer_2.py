#!/usr/bin/env python3


import rospy
from std_msgs.msg import String


def msg_callback(msg):

    rospy.loginfo(msg.data)

def lister_sol():
    
    rospy.init_node("customer_2")

    rospy.Subscriber("/solution",String,msg_callback)
    rospy.spin()

if __name__=="__main__":
    lister_sol()
    