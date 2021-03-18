#ejemplo de angular tomado de: https://www.w3schools.com/angular/default.asp

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

while True:
    conn, addr = s.accept()
    
    request = conn.recv(1024)
    
    conn.send(header)
    
    conn.sendall(pagina)
    conn.close()
    gc.collect()


