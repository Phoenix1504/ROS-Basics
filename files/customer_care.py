#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def msg_callback(msg):

    rospy.loginfo(msg.data)
    pub=rospy.Publisher("/solution",String,queue_size=10)
    pub.publish("Here is solution <="+ msg.data )
    
    
if __name__=="__main__":

    rospy.init_node("customerCareNode")

    rospy.Subscriber("/problem",String,msg_callback)
    rospy.spin()
