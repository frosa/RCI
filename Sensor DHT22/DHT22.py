""" Implementar el sensor en el proyecto """

import dht
import machine
d = dht.DHT22(machine.Pin(4)
