# Redes de Comunicación Industrial

Proyecto de comunicaciones entre nodos basados en el circuito integrado ESP8266.

[Administrador del proyecto](https://github.com/frosa)

## Objetivos del proyecto

Se trata de diseñar y poner en funcionamiento un prototipo de red industrial basada en ESP8266 y microphyton. 
La red industrial constará con un protocolo propio que identificará cada nodo de manera inequívoca. 


## Definición del protocolo de comunicaciones

El paquete de datos constará de la siguiente información:

Petición de datos:

    Nodo de destino | Número de variables solicitadas | Variables solicitadas |  CRC
    
    | .... | Variable n | Datos de la variable n 
Entrega de datos:

    Nodo de origen|Variable 1 | Datos de la variable 1 | Variable 2 | Datos de la variable 2 | .... | Variable n | Datos de la variable n | CRC 
    

