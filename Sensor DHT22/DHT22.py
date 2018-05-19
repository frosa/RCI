# Implementar el sensor en el proyecto

# Incluimos las librerías específicas de control del sensor y de configuración de pines del módulo

import dht
import machine
import time # Incluimos la función time para establecer los dos segundos de refresco establecidos por el fabricante para obtener los datos de la medición.
sensor = dht.DHT22(machine.Pin(4)) # De esta manera indicamos que el sensor está conectado al pin 4 del módulo.

# Dentro del Loop Main y cada vez que se necesite adquirir los valores de humedad y temperatura se deben de usar las siguientes instrucciones

# En este caso, se incluye un ejemplo de loop (bucle for) donde se toman los datos de temperatura y humedad 10 veces y se muestra a través de print.

for i in range(10):
    sensor.measure()
    time.sleep_ms(2000)
    print('temperatura grados celsius:', end=' ')
    print(sensor.temperature(), end=' ')
    print('Humedad reativa %:', end=' ')
    print(sensor.humidity(), end=' ')
   
# En vez de mostrar a través de la instrucción print se puede enviar a través el protocolo de comunicación los datos obtenidos por el sensor y las
# instrucciones sensor.temperature() sensor.humidity() y sensor.measure().

# Más información en: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/dht.html?highlight=dht
