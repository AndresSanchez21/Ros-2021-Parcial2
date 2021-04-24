#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String

enviar= None

def callback(msg):
    global enviar
    d=msg.data
    #REALIZAMOS EL MISMO PROCESO DEL NODO C PERO AHORA CON FLOTANTE
    rospy.loginfo(d)
    if d<100:
    	enviar=f"bajo: 100 medio: 0 alto: 0"
    if d>=100 and d<=150:
        b=((-(100/150)*d)+160)
        m=(((100*d)/50)-200)
        enviar=f"bajo: {b} medio: {m} alto: 0"
    if d>150 and d<=250:
        b=((-(100/150)*d)+160)
        m=(((-1)*d)+250)
        enviar=f"bajo: {b} medio: {m} alto: 0"
    if d>250 and d<=300:
        a=(((100/50)*d)-500)
        enviar=f"bajo: 0 medio: 0 alto: {a}"
    if d>300:
    	enviar=f"bajo: 0 medio: 0 alto: 100"   
    	
    	

def listener():
    pub = rospy.Publisher('string3', String, queue_size=10)
    rospy.init_node('listener', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    rospy.Subscriber('float', Float32, callback)
    while not rospy.is_shutdown():
        enviar_str = enviar
        pub.publish(enviar_str)
        rate.sleep()

if __name__ == '__main__':
    listener()
