import machine
import gc
import os

import network
from time import time

from machine import Pin

gc.collect()

#-------------------------------

# Archivo donde se guarda la data recolectada
try:
    status = os.stat('data.dat')
    #borramos el archivo si es mayor a 1MB
    if int(status[6])> 1000:
        os.remove('data.dat')
        i = open("data.dat", "a")
        i.close()
except:
    i = open("data.dat", "a")
    i.close()


#Archivo donde se guardan las configuraciones que puedan necesitarse
i = open("settings.dat", "a")
i.close()

