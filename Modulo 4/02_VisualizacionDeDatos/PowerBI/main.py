#https://github.com/Azure-Samples/IoTMQTTSample/tree/master/src/MicroPython

#------------------------------------------------
#Parametros a definir para tu subscripcion

#El connection string de tu suscripcion de azure IoT hub, puedes obtenerla
#desde el portal de Azure o VSCode con la extension IoT Hub
ConnString_Azure = "HostName=ioTStudy-YourData.azure-devices.net;DeviceId=ESP8266Demo;SharedAccessKey=00KquEJ7hz8FJdbz1vBGSTvtRsWzK/Abb7sfMxt1NGY="


#------------------------------------------------



import utime
from util import create_mqtt_client, get_telemetry_topic, get_c2d_topic, parse_connection


#...................................................................
# Obteniendo las distintas partes del connection string de Azure IoT

dict_keys = parse_connection(ConnString_Azure)

HOST_NAME = "HostName"
SHARED_ACCESS_KEY_NAME = "SharedAccessKeyName"
SHARED_ACCESS_KEY = "SharedAccessKey"
SHARED_ACCESS_SIGNATURE = "SharedAccessSignature"
DEVICE_ID = "DeviceId"
MODULE_ID = "ModuleId"
GATEWAY_HOST_NAME = "GatewayHostName"

shared_access_key = dict_keys.get(SHARED_ACCESS_KEY)
shared_access_key_name =  dict_keys.get(SHARED_ACCESS_KEY_NAME)
gateway_hostname = dict_keys.get(GATEWAY_HOST_NAME)
hostname = dict_keys.get(HOST_NAME)
device_id = dict_keys.get(DEVICE_ID)
module_id = dict_keys.get(MODULE_ID)

# username = '<HOSTNAME>/<DEVICE_ID>'
username = hostname + '/' + device_id


#SAS token
#Nota: este token tiene expiracion asi que debe de ser cambiado cada vez que se use
# Codigo tomado de: http://blogs.recneps.org/post/Generating-your-IoT-Hub-Shared-Access-Signature-for-your-ESP-8266-using-Azure-Functions

#Este codigo permite generar el codigo SAS a partir de una funcion de Azure
def getsas(hubname, deviceid, key):
    import urequests
    import ujson
    dict = {}
    dict["resourceUri"] = hubname+'.azure-devices.net/devices/'+deviceid
    dict["key"] = key
    dict["expiryInSeconds"]=86400
    payload = ujson.dumps(dict)
    response = urequests.post('https://sasiot-generador.azurewebsites.net/api/GetSAS?code=n7ZawVbcc/p6lbgqji00cvQsHqK2PzPYR3McW7t2ikhKrGawFpftTw==', data=payload)
    
    return response.text

sas_token_str = getsas(hostname,device_id,shared_access_key)

#...................................................................


# Creando cliente MQTT
mqtt_client = create_mqtt_client(client_id=device_id, hostname=hostname, username=username, password=sas_token_str, port=8883, keepalive=120, ssl=True)

#conectando a Azure IoT
print("conectando")
mqtt_client.reconnect()

#Definiendo publicacion
print("Publicando")
topic = get_telemetry_topic(device_id)

#Definimos nuestro sensor DHT22

import dht
from machine import Pin

sensor = dht.DHT22(Pin(14))

## Enviar telemetria
while True:
    #leemos el sensor
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    
    #convertimos las medidas en un formato JSON
    mensaje = '{"Temperatura":' +str(temp)+ ',"Humedad":'+str(hum)+'}'
    
    print(mensaje)
    
    mqtt_client.publish(topic=topic, msg=mensaje)
    utime.sleep(2)
    gc.collect()



