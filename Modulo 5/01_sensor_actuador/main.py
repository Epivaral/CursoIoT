#https://github.com/Azure-Samples/IoTMQTTSample/tree/master/src/MicroPython

#...................................................................

#control de Servos
from machine import Pin, PWM
import time


ph = Pin(12)
servo = PWM(ph,freq=50,duty=78)


def setpos(p):
    # Convertimos de grados a PWM, para este servo:
    #   0 grados = 1ms --> 52 (10 bits)
    # 180 grados = 2ms --> 105 (10 bits)
    # x = ((105-52)*pos/180)+52 = pos*0.29+52
    
    a= (0.29*p)+52
    
    servo.duty(int(a))
    time.sleep_ms(500)

#Control ADC
import machine
adc = machine.ADC(0)


#...................................................................




#------------------------------------------------
#Parametros a definir para tu subscripcion

#El connection string de tu suscripcion de azure IoT hub, puedes obtenerla
#desde el portal de Azure o VSCode con la extension IoT Hub
ConnString_Azure = "HostName=ioTStudyYourData.azure-devices.net;DeviceId=ESP8266Demo;SharedAccessKey=00KquEJ1hz5FJdbz1vBGSIvtRaWzK/Ayb7sfMxt7NGY="


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
    response = urequests.post('https://sasiotgenerador.azurewebsites.net/api/GetSAS?code=n7ZawVbcc/p5lbgqji00axQsHgK2PzPYR3McW7t2ikhKrGawFpfwTw==', data=payload)
    
    return response.text

sas_token_str = getsas(hostname,device_id,shared_access_key)

# Creando cliente MQTT
mqtt_client = create_mqtt_client(client_id=device_id, hostname=hostname, username=username, password=sas_token_str, port=8883, keepalive=120, ssl=True)

#conectando a Azure IoT
print("conectando")
mqtt_client.reconnect()

#Definiendo publicacion
print("Publicando")
topic = get_telemetry_topic(device_id)


#Funcion encargada de manejar el mensaje recibido
def callback_handler(topic, message_receive):
    print(message_receive)
    msg = str(message_receive).replace("b'","").replace("'","")

    setpos(int(msg))
    
    


#nos suscribimos al IoT hub para poder recibir mensajes
subscribe_topic =  get_c2d_topic(device_id)
#definimos la funcion que manejara los mensajes recibidos
mqtt_client.set_callback(callback_handler)
t = mqtt_client.subscribe(topic=subscribe_topic) #se realiza la suscripcion



## Recibir comandos
while True:
    lectura = str(adc.read())
    mqtt_client.publish(topic=topic, msg=lectura)
    
    print("Esperando Mensaje...")
    mqtt_client.wait_msg()
    
    utime.sleep(1)
    gc.collect()








