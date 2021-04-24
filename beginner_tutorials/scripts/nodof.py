#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

enviar= None 

def callback(msg):
    global enviar
    d=msg.data
    #REALIZAMOS LO MISMO DEL NODO E PARA PODER PARTIR LA CADENA DE STRING QUE NOS LLEGA CON LA FUNCION SPLIT PERO AHORA SI NECESITAMOS CONOCER LOS TRES VALORES BAJO MEDIO Y ALTO PARA COMPARARLOS Y PODER DECIDIR CUAL DE LOS TRES ESTADOS PREDOMINA DOBRE EL RESTO
    s=d.split()
    b=int(s[1])
    m=int(s[3])
    a=int(s[5])
    rospy.loginfo(d)
    if b>m and b>a:
    	enviar="b"
    if m>b and m>a:
        enviar="m"
    if a>b and a>m:
        enviar="a"
def listener():
    pub = rospy.Publisher('string21', String, queue_size=10)
    rospy.init_node('listener', anonymous=True)
    rate = rospy.Rate(0.5) # 0.5hz
    rospy.Subscriber('string2', String, callback)
    while not rospy.is_shutdown():
        enviar_str = enviar
        pub.publish(enviar_str)
        rate.sleep()

if __name__ == '__main__':
    listener()
