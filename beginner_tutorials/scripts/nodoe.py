#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

enviar= None 

def callback(msg):
    global enviar
    d=msg.data
    s=d.split()  #EL DATO NOS LLEGA EN FORMA DE STRING, ESTA FUNCION NOS PERMITE FORMAR UN VECTOR DE STRING LLENANDOLO CADA VEZ QUE EXISTA UN ESPACIO
    # NOS LLEGA bajo: 0 medio: 0 alto: 100
    #LO CONVERTIMOS A s[0]=bajo: s[1]=0 s[2]=medio: s[3]=0 ...
    b=int(s[1])
    rospy.loginfo(d)
    if b==0:	    #EN ESTE CASO SOLO CON SABER EL VALOR DE BAJO SABREMOS SI ESTA BAJO O ALTO YA QUE SOLO TIENE DOS VALORES
    	enviar="a"
    if b==100:
    	enviar="b"
def listener():
    pub = rospy.Publisher('string11', String, queue_size=10)
    rospy.init_node('listener', anonymous=True)
    rate = rospy.Rate(0.5) # 0.5hz
    rospy.Subscriber('string1', String, callback)
    while not rospy.is_shutdown():
        enviar_str = enviar
        pub.publish(enviar_str)
        rate.sleep()

if __name__ == '__main__':
    listener()
