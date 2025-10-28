import socket
server_addr = input("¿A qué servidor te quieres conectar?")
server_port = int(input("¿A qué puerto?"))
# 1. Creación del socket
# socket.AF_INET -> Dirección compuesta por IP + PORT
# socket.SOCK_STREAM -> TCP (socket.SOCK_DGRAM -> UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. Conectar el socket
sock.connect((server_addr, server_port))
# sock.connect((server_addr, 80)) # Servidor web http
# sock.connect((server_addr, 443)) # Servidor web https
# 3. Enviar la solicitud (hay que transformar a bytes la cadena)
sock.send(b"GET / HTTP/1.1\r\nHost: " +
bytes(server_addr, "utf8") +
b"\r\nConnection: close\r\n\r\n")
# 4. Recibir la respuesta
reply = sock.recv(10000) # 10000 es el número de byte máximo
# 5. Cerrar el socket
# socket.SHUT_RD - Notifica que deja de leer
# socket.SHUT_WR - Notifica que deja de escribir
# socket.SHUT_RDWR - Notifica que deja de leer y escribir
sock.shutdown(socket.SHUT_RDWR)
sock.close()
# Tratar los datos
print(repr(reply))