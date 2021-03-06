import socket

macAddr = 'b8:27:eb:5b:11:0c'
port = 3
backlog = 1
size = 1024

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((macAddr, port))
s.listen(backlog)
try:
	client, address = s.accept()
	while 1:
		data = client.recv(size)
		if data:
			print(data)
			client.send(data)
except:
	print("Closing socket")
	client.close()
	s.close()
