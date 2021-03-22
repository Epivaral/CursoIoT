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

#definimos el ADC
import machine
adc = machine.ADC(0)

def LeeTemperatura():
    lectura = adc.read()
    #ecuacion tomada de Modulo 2 Video 13 - I2C
    voltaje = (lectura / 1024.0)*3.3
    temperatura = (voltaje - 0.5) * 100
    return str(temperatura)


while True:
    conn, addr = s.accept()
    
    request = conn.recv(1024)
    
    conn.send(header)
    
    # Reemplazamos el comodin %Temp% en el html con el valor de temperatura
    pagina1 = pagina.replace('%Temp%',LeeTemperatura())
    
    conn.sendall(pagina1)
    conn.close()
    gc.collect()


