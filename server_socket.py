import socket
import os

def create_server_sock():
	sock = socket.socket()
	sock.bind(("",9999))
	return sock

def wait_clients(serverSock):
	finishWait = False
	sock.listen(0)

	while(not finishWait):
		clientConn = sock.accept()
		
		if(clientConn != None):
			print("Client connection accepted: addr  ", clientConn[1])
			process_client_conn(clientConn)


def process_client_conn(clientConn):
    
	#childProcess = os.fork()
	#if(childProcess == 0):
     
	clientSock = clientConn[0]
  
	while(True):
      
		recvData = bytearray()
		while((b'\n' not in recvData)):
			recvData = clientSock.recv(4096)
			if(len(recvData)):
				print("Recv data: ", recvData, ". EOF: ", recvData, ". From client: ", clientConn[1])
	
		#sendedData = 0
		#while(sendedData < len(recvData)):
		#	sendedData += clientSock.send(recvData[sendedData])
		
		#print("Data send finish")
	#else:
	#	print("New process ", childProcess)
   

sock = create_server_sock()

if(sock == None):
	print("Listen socket create failed")

wait_clients(sock)

print("Program finish")




