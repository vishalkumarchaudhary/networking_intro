from socket import *
from threading import *

 

serverName = "127.0.0.1"
serverPort = 12006

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while 1 :
	sentence = raw_input('Input lowercase sentence:')
	
	clientSocket.send(sentence)
	if(sentence == 'bye'):
		break
	modifiedSentence = clientSocket.recv(1024)
	print 'From Server:', modifiedSentence

	
clientSocket.close()