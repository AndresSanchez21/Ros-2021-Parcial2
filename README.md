# Ros-2021-1 Parcial 2 corte 
**Ejercicio desarrolado:**
Este ejercicio basado en la utilizacion y comunicacion de nodos de ros, 8 nodos los cuales reciben y envian informacion(con dos nodos principales A:que es el que envia la primera informacion y H:que es el que recibe la ultima informacion y da respuesta), ejercicio dividido en tres ramas de nodos la primera que trabajara un boleano A-B-E-F-H, la segunda A-C-F-H y la tercera A-D-G-H, donde el nodo A enviara el valor correspondiente a cada nodo siguiente(B, C, D), estos tres seran encargados de darle el porcentaje de alto-medio-bajo al valor que llega del nodo A, para posteriormente enviar un texto a los nodos E-F-G quienes determinaran si el valor esta bajo, medio o alto y enviar al nodo h la inicial(a-b-c), donde el nodo h le enviara la decision al nodo a de bajar, mantener o subir el valor del dato.
# Secuencia de pasos para compilar
1.Compilar Roscore
```
roscore
```
