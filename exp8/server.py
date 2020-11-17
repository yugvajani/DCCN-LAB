import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6000))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f'Connection established with {address}')
	clientsocket.send(bytes('Hello DCCN LAB!', 'utf-8'))
	clientsocket.close()