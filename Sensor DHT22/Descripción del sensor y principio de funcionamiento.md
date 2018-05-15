## Sensor utilizado y características básicas

El sensor utilizado en el proyecto es el DTH22, se trata de un sensor de temperatura y humedad que dispone de librería específica para su control con MicroPhyton.

En el siguiente enlace se dipone una descripción más detalla de este sensor:
<http://www.adafruit.com/products/385>

 - ***Características eléctricas***
 
 EL DTH22 dispone de tres pines físicos de conexión distribuidos tal y como se describe en la siguiente [imagen](https://hackster.imgix.net/uploads/attachments/267054/dht22-pinout_2P1AgF3wPs.png?auto=compress%2Cformat&w=680&h=510&fit=max)
 
 Las necesidades eléctricas del sensor son:
 
 | Parámetro | Unidades |
 |--------------------|--------------------|
 Voltaje | 3,3-5,5V
 Potencia máxima de consumo | 0,5 mA usando 5V como alimentación
 Muestreo | 2s
 
 - ***Rendimiento sensor***
 
 **Temperatura**
 
 | Parámetro | Condición | Min | Typ | Máx | Unidades |
 |----------|----------|---------|----------|-----------|----------|
 | Resolución |  |  | 0,1 |  | ºC |
 | Resolución |  |  | 16 |  | bit |
 | Precisión |  |  | +-0,5 | +-1 | ºC |
 | Rango |  | -40 |  | 80 | ºC |
 
 **Humedad**
 
 | Parámetro | Condición | Min | Typ | Máx | Unidades |
 |----------|----------|---------|----------|-----------|----------|
 | Resolución |  |  | 0,1 |  | %RH |
 | Precisión | 25ºC |  | +-2 |  | %RH |
 | Rango |  | 0 |  | 99,9 | %RH |
 
 

## Principio de funcionamiento y acondicionamiento de señal

El DHT22 es un sensor del tipo *1-wire device*. Teniendo en cuenta esta condición, el acondicionamiento de señal es mínimo. No obstante, el fabricante recomienda incluir interporner una resistencia pull-up entre el pin de comunicaciones del sensor y la alimenctación Vcc. De esta manera aseguramos un valor alto en la entrada del microprocesador en el caso de que el sensor esté en modo IDLE.

El sensor entrega los valores de humedad y temperatura en binario por lo que el módulo no requiere incluir un conversor analógico digital para comprender los valores. Además, la librería DHT y MACHINE contienen funciones directas que permiten leer y convertir los valores directamente en humedad relativa y grados celsius.

### Uso final en el proyecto

En el proyecto este sensor se conecta...
