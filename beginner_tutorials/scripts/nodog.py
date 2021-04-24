#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

enviar= None 

def callback(msg):
    global enviar
    d=msg.data
    #SE REALIZA EL MISMO PROCESO DEL NODO E TENIENDO ENCUENTA QUE AHORA NUESTRO DATO A TRABAJAR ES UN FLOTANTE
    s=d.split( )
    b=float(s[1])
    m=float(s[3])
    a=float(s[5])
    rospy.loginfo(d)
    if b>m and b>a:
    	enviar="b"
    if m>b and m>a:
        enviar="m"
    if a>b and a>m:
        enviar="a"
def listener():
    pub = rospy.Publisher('string31', String, queue_size=10)
    rospy.init_node('listener', anonymous=True)
    rate = rospy.Rate(0.5) # 0.5hz
    rospy.Subscriber('string3', String, callback)
    while not rospy.is_shutdown():
        enviar_str = enviar
        pub.publish(enviar_str)
        rate.sleep()

if __name__ == '__main__':
    listener()
