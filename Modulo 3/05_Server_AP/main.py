import usocket

f = open("pagina1.html", "r")
pagina = f.read()
f.close()

# tomado de la documentacion
# https://docs.micropython.org/en/latest/library/usocket.html#usocket.socket
s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
s.bind(('', 80)) #la direccion 
s.listen(1)

while True:
    conn, addr = s.accept()
    
    request = conn.recv(1024)
   
    conn.sendall(pagina)
    conn.close()
    gc.collect()
