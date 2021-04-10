#Datasheet servo para obtener informacion de PWM:
#http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf

import usocket



header = "HTTP/1.1 200 OK\n"
header += "Content-Type: text/html\n"
header += "Connection: close\n\n"

f = open("pagina1.html", "r")
pagina = f.read()
f.close()

# tomado de la documentacion
# https://docs.micropython.org/en/latest/library/usocket.html#usocket.socket
s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
s.bind(('', 8080)) #la direccion 
s.listen(10)

#control de Servos
from machine import Pin, PWM
import time

pv = Pin(14)
servoV = PWM(pv,freq=50,duty=78)

ph = Pin(12)
servoH = PWM(ph,freq=50,duty=78)

def setpos(H,V):
    # Convertimos de grados a PWM, para este servo:
    #   0 grados = 1ms --> 52 (10 bits)
    # 180 grados = 2ms --> 105 (10 bits)
    # x = ((105-52)*pos/180)+52 = pos*0.29+52
    
    a= (0.29*H)+52
    b= (0.29*V)+52
    
    servoH.duty(int(a))
    servoV.duty(int(b))
    time.sleep_ms(500)




while True:
    conn, addr = s.accept()
    
    request = conn.recv(1024)
    
    #Leemos el request del cliente
    request = str(request)
    
    #Obtenemos los parametros y movemos el servo
    if (request.find("servoPOSH=",0)>0):
        posH = request[request.find("servoPOSH=",0)+10:request.find("servoPOSV=",0)-1]
        posV = request[request.find("servoPOSV=",0)+10:request.find("end=0",0)-1]
        print(posH)
        print(posV)
        setpos(int(posH),int(posV))
    
    
    # Mandamos el header y pagina web
    conn.send(header)
    conn.sendall(pagina)
    
    conn.close()
    gc.collect()




