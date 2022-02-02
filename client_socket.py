import socket

def create_client_sock():
	sock = socket.create_connection(("127.0.0.1",9999))
	return sock

sock = create_client_sock()

if(sock == None):
	print("Can't create client socket")
else:
	print("Connected to server")

	data = bytearray(b'Echo msg\n')
	
	sendedCount = 0
	while(sendedCount < len(data)):
		sendedCount += sock.send(data[sendedCount:])
		print("Sended ", sendedCount, " bytes")

