# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:34:22 2018

@author: Roberto

Código de los esclavos

El esclavo (servidor) recibe la petición del maestro (cliente) y devuelve
los datos solicitados
"""

#importamos el modulo socket
import socket

#Identificación de cada nodo esclavo
ID_esclavo = "01"
 
#Instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
#Con el metodo bind le indicamos la dirección y puerto de escucha
#Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind(("localhost", 30000))
 
#Aceptamos conexiones entrantes con el metodo listen, y especificamos
#El numero de conexiones que vamos a aceptar
s.listen(1)
 
#El método accept devuelve un objeto sc (socket cliente) para recibir datos, 
#y otro que representa una tupla con los datos de conexion IP y puerto
sc, addr = s.accept()

 
while True:
 
    #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro 
    #la cantidad de bytes para recibir
    recibido = sc.recv(2048)
    #Se decodifican los datos recibidos en formato binario a string
    string = recibido.decode("UTF-8")
    
    #Si se reciben datos nos muestra la IP y el mensaje recibido
    print ("Recibido:", string, "desde:" + str(addr[0]))
    
    #Enviamos los datos al cliente 
    #(Ejemplo de protocolo: ID_esclavo,ID_variable1,Datos_variable1,ID_variable2,...)
    datos="01,TC,20,HR,56"
    
    #Si la petición es para este esclavo, se envían los datos
    if string[0:2] == ID_esclavo:
        
        tam = sc.send(bytes(datos,encoding="UTF-8"))
        print("Enviada respuesta:", datos, "con tamaño:", tam)
 
    #Si el mensaje recibido es la palabra close se cierra el socket
    if recibido == b'close':
        break
 
    
    if recibido == b'':
        break
    
print ("Conexión terminada por el cliente")
 
#Cerramos la instancia del socket cliente y servidor
sc.close()
s.close()
