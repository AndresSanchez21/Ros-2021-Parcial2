#!/usr/bin/env python3

import rospy

#IMPORTAMOS LOS TIPOS DE VARIABLES QUE SERAN UTILIZADAS
from std_msgs.msg import Bool     #BOLEANA
from std_msgs.msg import Int16    #ENTERA
from std_msgs.msg import Float32  #FLOTANTE
from std_msgs.msg import String   #STRING


boleano= Bool()  #DECLARAMOS DE BOLEANO SERA BOOL
boleano= False   #VALOR BOLEANO A LA VARIABLE A->B
entero=280       #VALOR ENTERO A LA VARIABLE A->C
flotante=320.21  #VALOR FLOTANTE A LA VARIABLE A->D
cambio=100       #VALOR PARA PODER VARIAR EL ENTERO Y EL FLOTANTE


def callback(msg):
    global cambio
    global entero 
    global flotante
    d=msg.data
    s=d.split()  
    b=s[0]          #DE LO QUE NOS LLEGA DE RESPUESTA, SACAMOS LA PRIMERA PALABRA PARA SABER QUE DEBEMOS HACER
    rospy.loginfo(d)
    #PARA HACER EL CAMBIO EN EL VALOR REALIZAMOS UN CAMBIO EN EL PORCENTAJE DE VALOR EN LA VARIABLE CAMBIO 
    if b=="bajar":	    
    	cambio=cambio-(cambio*0.05) 
    if b=="mantener":
    	cambio=cambio 
    if b=="subir":
        cambio=cambio+(cambio*0.05)

def talker():
    #DECLARAMOS EL PUBLICADOR CON EL NOMBRE DEL MENSAJE(TOPIC), TIPO DE VARIABLE Y EL TAMAÑO DE PILA DE ALMACENAMIENTO DE DATOS.
    pub1 = rospy.Publisher('bool', Bool, queue_size=10)     #MENSAJE DE A->B
    pub2 = rospy.Publisher('int', Int16, queue_size=10)     #MENSAJE DE A->C
    pub3 = rospy.Publisher('float', Float32, queue_size=10) #MENSAJE DE A->D
    rospy.init_node('talker', anonymous=True) #INICIALIZAMOS EL NODO
    rate = rospy.Rate(10) # 10hz FRECUENCIA A LA QUE TRABAJA EL NODO
    rospy.Subscriber('respuesta', String, callback)
    while not rospy.is_shutdown():
        rospy.loginfo("Datos enviados:") #MENSAJE PARA MANTENER EL ORDEN
        #HACEMOS ESTAS DOS FUNCIONES PARA NO ENVIAR NUMEROS NEGATIVOS Y PODER HACER EL CAMBIO EN LAS VARIABLES DE ENTERO Y FLOTANTE
        entero1=entero-100+int(cambio)
        flotante1=flotante-100+cambio 
        rospy.loginfo(boleano)           #IMPRIMIMOS LOS DATOS A ENVIAR
        rospy.loginfo(entero1)            
        rospy.loginfo(flotante1)
        pub1.publish(boleano)     #PUBLICAMOS AL SIGUIENTE NODO
        pub2.publish(entero1)
        pub3.publish(flotante1)
        rate.sleep()              #ESPERAMOS A COMPLETAR LA FRECUENCIA

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
