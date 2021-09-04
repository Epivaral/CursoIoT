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


def GuardaTexto(texto):
    a = open("info.txt", "a")
    a.write(texto+"<br/>")
    a.close()



while True:
    conn, addr = s.accept()
    
    request = conn.recv(1024)
    
    #Leemos el request del cliente
    request = str(request)
    
    
    if (request.find("texto=",0)>0):
        textos = request[request.find("texto=",0)+6:request.find("HTTP/",0)]
        GuardaTexto(textos)
    
    
    # Mandamos el header y pagina web
    conn.send(header)
    
    f = open("info.txt", "r")
    pagina1 = f.read()
    pagina1 += "</body></html>"
    f.close()
    
    conn.sendall(pagina+pagina1)
    
    conn.close()
    gc.collect()




