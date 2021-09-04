#imports
import esp
esp.osdebug(None)

import gc
gc.collect()

#-------------------------------

import network
from time import time

sta_if = network.WLAN(network.STA_IF) #definimos como Station nuestro board

if sta_if.active() == False: # validamos si STATION esta activado o no
  sta_if.active(True)
  
sta_if.connect('<SSID>', '<PWD>') #Cambiar por tu SSID y Password

print('Conectando...')

t = time()

while sta_if.isconnected() == False:
    if(time()-t)>20: #timeout de n segundos para evitar bloquear el board  
        break

   
if sta_if.active():
  print('Station Activado')
  print('IP Board:', sta_if.ifconfig())

i = open("info.txt", "a")
i.close()
    

