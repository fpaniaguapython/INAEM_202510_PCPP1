import socket
host = '127.0.0.1'#Dirección IP del servidor (localhost)
puerto = 8021#Puerto
socket_cliente= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect((host, puerto))
print(f"Conectado al servidor en {host}:{puerto}")
mensaje = "Hola, servidor. ¿Cómo estás?"
socket_cliente.sendall(mensaje.encode('utf-8'))
print(f"Datos enviados al servidor: {mensaje}")
datos = socket_cliente.recv(1024)
print(f"Datos recibidos del servidor: {datos.decode('utf-8')}")
socket_cliente.close()