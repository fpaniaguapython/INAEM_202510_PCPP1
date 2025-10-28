import socket
BYE_WORD='BYE'
host = '127.0.0.1'#Dirección IP del servidor (localhost)
puerto = 8021#Puerto
socker_servidor= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socker_servidor.bind((host, puerto))
socker_servidor.listen()
print(f"Servidor arrancado. Host: {host}. IP: {puerto}")
socket_cliente, direccion_cliente= socker_servidor.accept()
while True:
    print(f"Se ha recibido una petición desde {direccion_cliente}")
    data = socket_cliente.recv(1024)
    print(f"Datos recibidos del cliente: {data.decode('utf-8')}")
    if data.decode('utf-8')==BYE_WORD:
        socket_cliente.close()
        socker_servidor.close()
        break
    mensaje = input('Introduce un mensaje:')
    if mensaje==BYE_WORD:
        socket_cliente.close()
        socker_servidor.close()
        break
    socket_cliente.sendall(mensaje.encode('utf-8'))
    print(f"Datos enviados al cliente: {mensaje}")
    