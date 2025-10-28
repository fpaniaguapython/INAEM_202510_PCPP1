import socket
host = '127.0.0.1'#Dirección IP del servidor (localhost)
puerto = 8021#Puerto
socker_servidor= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socker_servidor.bind((host, puerto))
socker_servidor.listen()
print(f"Servidor arrancado. Host: {host}. IP: {puerto}")
socket_cliente, direccion_cliente= socker_servidor.accept()
print(f"Se ha recibido una petición desde {direccion_cliente}")
data = socket_cliente.recv(1024)
print(f"Datos recibidos del cliente: {data.decode('utf-8')}")
mensaje = "Hola, cliente. Todo bien por aquí."
socket_cliente.sendall(mensaje.encode('utf-8'))
print(f"Datos enviados al cliente: {mensaje}")
socket_cliente.close()
socker_servidor.close()