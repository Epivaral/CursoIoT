#https://github.com/Azure-Samples/IoTMQTTSample/tree/master/src/MicroPython

#------------------------------------------------
#Parametros a definir para tu subscripcion

#El connection string de tu suscripcion de azure IoT hub, puedes obtenerla
#desde el portal de Azure o VSCode con la extension IoT Hub
ConnString_Azure = "HostName=<iotHub>.azure-devices.net;DeviceId=ESP8266Demo;SharedAccessKey=00KquEJ1hz5FJdbz1vBGSIvtRaWzK/Ayb7sfMxt7NGY="


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
    response = urequests.post('https://<funcion>.azurewebsites.net/api/GetSAS?code=n7ZawVbcc/p5sbgqji00axQsHgK2PzPYR1McW7t2ikhKrDawFpfwTw==', data=payload)
    
    return response.text

sas_token_str = getsas(hostname,device_id,shared_access_key)

#...................................................................


# Creando cliente MQTT
mqtt_client = create_mqtt_client(client_id=device_id, hostname=hostname, username=username, password=sas_token_str, port=8883, keepalive=120, ssl=True)

#conectando a Azure IoT
print("conectando")
mqtt_client.reconnect()


from machine import Pin
led = Pin(12, Pin.OUT)
led.value(1)
 

def set_led(status):
    if status == '0':
        led.value(1)
    else:
        led.value(0)



#Funcion encargada de manejar el mensaje recibido
def callback_handler(topic, message_receive):
    print(message_receive)
    
    msg = str(message_receive).replace("b'","").replace("'","")
    valores = msg.split(',')

    if valores[0] == 'led':
        set_led(valores[1])


#nos suscribimos al IoT hub para poder recibir mensajes
subscribe_topic =  get_c2d_topic(device_id)
#definimos la funcion que manejara los mensajes recibidos
mqtt_client.set_callback(callback_handler)
t = mqtt_client.subscribe(topic=subscribe_topic) #se realiza la suscripcion



## Recibir comandos
while True:
    print("Esperando Mensaje...")
    mqtt_client.wait_msg()
    utime.sleep(1)
    gc.collect()


