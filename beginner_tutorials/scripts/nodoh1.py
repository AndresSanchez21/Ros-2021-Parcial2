#!/usr/bin/env python

import rospy
from std_msgs.msg import String

#VARIABLES A UTILIZAR
c=0   
enviar= None

def callback(msg):
    #DEFINIMOS VARIABLE SGLOBALES
    global enviar    #VARIABLE A ENVIAR AL SGTE NODO STRING
    global c         #CONTADOR INT
    global boleano   #VARIABLE DE LA PRIMERA RAMA DE NODOS
    global entero    #VARIABLE DE LA SEGUNDA RAMA DE NODOS
    global flotante  #VARIALE DE LA TERCERA RAMA DE NODOS
    c=c+1   
    d=msg.data       #VARIABLE DATO
    if c==1:
        boleano=d    #GUARDAMOS EL PRIMER DATO EN LA VARIABLE BOLEANO
    if c==2:
        entero=d     #GUARDAMOS EL SEGUNDO DATO EN LA VARIABLE ENTERO
    if c==3:
        flotante=d   #GUARADMOS EL TERCER DATO EN LA VARIABLE FLOTANTE
        c=0          #VOLVEMOS EL CONTADOR CERO
        #REALIAMOS EL ARBOL DE TOMA DE DECISIONES DONDE COMPARAMOS LAS TRES ENTRADAS BOLEANA ENTERA Y FLOTANTE SI NOS LLEGAN EN ALTA MEDIA O BAJA O DECIDIMOS SI BAJAR MANTENER O SUBIR LAS RPM DEL MOTOR
        if boleano=="b":
            if entero=="b":
                if flotante=="b":
                    enviar="subir rpm del motor"
                if flotante=="m":
                    enviar="subir rpm del motor"
                if flotante=="a":
                    enviar="subir rpm del motor"
            if entero=="m": 
                if flotante=="b":
                    enviar="subir rpm del motor"
                if flotante=="m":
                    enviar="mantener rpm del motor"
                if flotante=="a":
                    enviar="mantener rpm del motor"  
            if entero=="a": 
                if flotante=="b":
                    enviar="subir rpm del motor"
                if flotante=="m":
                    enviar="mantener rpm del motor"
                if flotante=="a":
                    enviar="bajar rpm del motor"
        if boleano=="a":
            if entero=="b":
                if flotante=="b":
                    enviar="subir rpm del motor"
                if flotante=="m":
                    enviar="mantener rpm del motor"
                if flotante=="a":
                    enviar="bajar rpm del motor"
            if entero=="m": 
                if flotante=="b":
                    enviar="mantener rpm del motor"
                if flotante=="m":
                    enviar="mantener rpm del motor"
                if flotante=="a":
                    enviar="bajar rpm del motor"  
            if entero=="a": 
                if flotante=="b":
                    enviar="bajar rpm del motor"
                if flotante=="m":
                    enviar="bajar rpm del motor"
                if flotante=="a":
                    enviar="bajar rpm del motor"
        rospy.loginfo(enviar)
    

def listener():
    pub = rospy.Publisher('respuesta', String, queue_size=10)
    rospy.init_node('listener', anonymous=True)    #INICIALIZAMOS EL NODO
    rate = rospy.Rate(0.2) # 0.2hz
    #DECLARAMOS LOS SUBSCRIPTORES CON NOMBRE DE MENSAJE, TIPO DE DATO Y LLAMAMOS LA FUNCION CALLBACK EN LA CUAL TOMAMOS EL DATO QUE NOS LLEGA Y LO PROCESAMOS A NUESTRA NECESIDAD
    rospy.Subscriber('string11', String, callback) #DATO DE LA PRIMERA RAMA
    rospy.Subscriber('string21', String, callback) #DATO DE LA SEGUNDA RAMA
    rospy.Subscriber('string31', String, callback) #DATO DE LA TERCERA RAMA
    while not rospy.is_shutdown():
        enviar_str = enviar
        pub.publish(enviar_str)
        rate.sleep()

if __name__ == '__main__':
    listener()
