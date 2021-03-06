import network
# authmode
# 0 – open
# 1 – WEP
# 2 – WPA-PSK
# 3 – WPA2-PSK
# 4 – WPA/WPA2-PSK

authmode_ls = ['open','WEP','WPA-PSK','WPA2-PSK','WPA/WPA2-PSK']

# Hidden
# 0 – visible
# 1 – hidden

hidden_ls =['visible','hidden']


wlan = network.WLAN(network.STA_IF) 
wlan.active(True)       


listado = wlan.scan()

print('Redes detectadas: ', len(listado))

# parametros obtenidos de scan:
# https://docs.micropython.org/en/latest/library/network.html#network.AbstractNIC.scan
for ssid, bssid, channel, RSSI, authmode, hidden in listado:
    print('---------------------')
    print('ssid: ', ssid)
    print('bssid: ', bssid)
    print('channel: ', channel)
    print('RSSI: ', RSSI)
    print('authmode: ',authmode_ls[authmode])
    print('hidden: ',hidden_ls[hidden])


gc.collect()