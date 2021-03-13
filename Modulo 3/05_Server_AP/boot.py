#imports
import esp
esp.osdebug(None)

import gc
gc.collect()

#----------------------
import network

ssid = 'mi board'
password = 'PasswordSeguro'

ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)

ap_if.config(essid=ssid, password=password)

if ap_if.active():
  print('Conectate a esta direccion: ',ap_if.ifconfig())