from socket import *
from threading import *

 

serverName = "127.0.0.1"
serverPort = 12006

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while 1 :
	sentence = bytes(input('Input lowercase sentence:'),'utf-8')
	
	clientSocket.send(sentence)
	if(sentence == b'bye'):
		break
	modifiedSentence = clientSocket.recv(1024)
	print ('From Server:', modifiedSentence)

	
clientSocket.close()