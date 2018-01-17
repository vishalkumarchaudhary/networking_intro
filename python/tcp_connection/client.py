from socket import *
serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
while 1 :
	sentence = raw_input('Input lowercase sentence:')
	if(sentence=='bye'):
		break
	clientSocket.send(sentence)
	modifiedSentence = clientSocket.recv(1024)
	print 'From Server:', modifiedSentence

clientSocket.close()