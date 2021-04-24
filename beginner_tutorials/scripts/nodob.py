#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
from std_msgs.msg import String

#NODO PUBLICADOR SUBSCRIPTOR

enviar= None

def callback(msg):
    global enviar
    b=msg.data
    rospy.loginfo(msg.data) #IMPRIMIMOS EL DATO QUE NOS LLEGA
    #PREGUNTAMOS SI EL VALOR EL ALTO O BAJO PARA MANDAR AL NODO E LOS PORCENTAJES     
    if b==True:
    	enviar="bajo: 0 medio: 0 alto: 100" #DATO A ENVIAR SI LLEGA ALTO
    if b==False:
    	enviar="bajo: 100 medio: 0 alto: 0" #DATO A ENVIAR SI LLEGA BAJO
    	

def listener():
    #DECLARAMOS EL PUBLICADOR CON EL MISMO NOMBRE A DONDE IRA EL DATO A ENVIAR B->E PRIMERA RAMA
    pub = rospy.Publisher('string1', String, queue_size=10) 
    rospy.init_node('listener', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    rospy.Subscriber('bool', Bool, callback) #SUBSCRIPTOR CON EL MISMO NOMBRE DEL PUBLICADOR DE DONDE LLEGA EL MENSAJE EN ESTE CASO DEL NODO A
    while not rospy.is_shutdown():
        enviar_str = enviar     #GUARDAMOS LA VARIABLE A ENVIAR EN ENVIAR_STR
        pub.publish(enviar_str) #PUBLICAMOS EN EL SIGUIENTE NODO (NODO E)
        rate.sleep()

if __name__ == '__main__':
    listener()
