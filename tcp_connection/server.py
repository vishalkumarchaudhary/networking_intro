from socket import *
from threading import *

def send_thread(connectionSocket ,sentence):
	connectionSocket.send(sentence)

def client_thread(connectionSocket ,addr):
	while 1 :
		sentence = connectionSocket.recv(1024)
		print"client send : "+ str(addr) +' : ' +sentence

		if(sentence =='bye'):
			connectionSocket.close()
			exit(1)
		connectionSocket.send(sentence)			
		#threadObj = Thread(target=send_thread, args=[connectionSocket ,sentence])
		#threadObj.start()

	


serverPort = 12006

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))
serverSocket.listen(5)
print 'The server is ready to receive'

while 1:
	connectionSocket, addr = serverSocket.accept()
	threadObj = Thread(target=client_thread, args=[connectionSocket ,addr])
	threadObj.start()

serverSocket.close()
print("halted")