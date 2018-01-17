from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print "The server is ready to receive"

try:
	while 1:
		message, clientAddress = serverSocket.recvfrom(2048)
		x="1";
		for i in range(50):
			x = x +str(i)+' '
		y=serverSocket.sendto(x,  clientAddress ,bufsize=10)
		print(y)
except :
	serverSocket.close()