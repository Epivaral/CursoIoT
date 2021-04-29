#https://github.com/Azure-Samples/IoTMQTTSample/tree/master/src/MicroPython

#------------------------------------------------
#Parametros a definir para tu subscripcion

#El connection string de tu suscripcion de azure IoT hub, puedes obtenerla
#desde el portal de Azure o VSCode con la extension IoT Hub
ConnString_Azure = "HostName=<TuHub>.azure-devices.net;DeviceId=<TuDispositivo>;SharedAccessKey=<TuKey>"

#SAS token puede ser creado desde VSCode con la extension IoT Hub
#Nota: este token tiene expiracion asi que debe de ser cambiado cada vez que se use
sas_token_str = "<TuSAS>"
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
#...................................................................


# Creando cliente MQTT
mqtt_client = create_mqtt_client(client_id=device_id, hostname=hostname, username=username, password=sas_token_str, port=8883, keepalive=120, ssl=True)

#conectando a Azure IoT
print("conectando")
mqtt_client.reconnect()

#Definiendo publicacion
print("Publicando")
topic = get_telemetry_topic(device_id)

## Enviar telemetria
while True:
    messages = ["Agua", "Barco", "Casa", "Dama", "Elefante", "Gota", "Huerto", "Imponente",  "Juego" , "Kilo", "Lugar"]
    for i in range(0, len(messages)):
        print("Enviando " + str(i))
        mqtt_client.publish(topic=topic, msg=messages[i])
        utime.sleep(2)
        
    gc.collect()


