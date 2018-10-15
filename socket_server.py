import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 7000))
server.listen(10)
socket, addr = server.accept()
data = socket.recv(1024)
print(data.decode('utf-8'))
socket.send('nihao, I get your messenger {}'.format(data.decode('utf-8')).encode('utf-8'))
server.close()
socket.close()
