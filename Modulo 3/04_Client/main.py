import usocket


url = 'https://www.galileo.edu/' #sitio universidad Galileo

# el underscore _ es usado para ignorar valores de una lista, en este caso usando url.split
# obtenemos Host > www.sitio.com  y Path > /subfolder/
_, _, host, path = url.split('/', 3)

#obtenemos la direccion del sitio
addr = usocket.getaddrinfo(host, 80)[0][-1]

#definimos el socket
s = usocket.socket()


# nos conectamos a la direccion
s.connect(addr)

#mas informacion del comando HTTP GET
#https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET

getRequest = bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8')
print('Comando GET >>> ',getRequest )
print('---------------')

#mandamos el comando GET
s.send(getRequest)

while True:
    data = s.recv(100)
    if data:
        print(str(data, 'utf8'), end='')
    else:
        break
    
# Cerramos el socket    
s.close()
#Garbage collector
gc.collect()
