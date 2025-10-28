import socket
BYE_WORD='BYE'
host = input('Host:') #Dirección IP del servidor (localhost)
puerto = input('Port:') #Puerto
socket_cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect((host, puerto))
print(f"Conectado al servidor en {host}:{puerto}")
while True:
    mensaje = input('Introduce un mensaje:')
    if (mensaje==BYE_WORD):
        socket_cliente.close()
        break
    socket_cliente.sendall(mensaje.encode('utf-8'))
    print(f"Datos enviados al servidor: {mensaje}")
    datos = socket_cliente.recv(1024)
    print(f"Datos recibidos del servidor: {datos.decode('utf-8')}")
    if (datos.decode('utf-8')==BYE_WORD):
        socket_cliente.close()
        break    