# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:34:22 2018

@author: Roberto

Código del maestro

El maestro actúa como cliente y envía sucesivas peticiones de datos a los 
esclavos (servidores)
"""

import socket  


# Se crea el objeto de la clase socket, con los argumentos
# familia y tipo. (Por defecto se utiliza AF_INET y SOCK_STREAM)
s = socket.socket()


# El argumento de connect es una tupla con host y puerto
s.connect(("localhost", 30000))  
  
while True:
    
    #Ejemplo de petición a enviar
    peticion = bytes("01,02,TC,HR",encoding="UTF-8")
 
    #Con el metodo send, enviamos la petición de datos al servidor
    s.send(peticion)
    
    #Recibimos los datos del servidor (esclavo)
    respuesta = s.recv(2048)
    print("Datos recibidos del esclavo i:", respuesta.decode("UTF-8"))
    
    break

# Una vez se ha terminado se cierra el socket 
s.close()
 


 
