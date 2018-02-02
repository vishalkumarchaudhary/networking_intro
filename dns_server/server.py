from socket import *
import sys


def main():

	servername ='127.0.0.1'
	serverPort = 53
	
	#creating udp server which is binded to port 53
	serverSocket = socket(AF_INET, SOCK_DGRAM)
	serverSocket.bind((servername, serverPort))
	print ("The server is ready to receive")
	
	 
	while 1:
		data, clientAddress = serverSocket.recvfrom(512)
	
		dns_res = get_dns_response(data)
		y=serverSocket.sendto(dns_res,  clientAddress )

	 
		
		


### creating dns response 
def get_dns_response(data):
	domain_names={'jamesbond.com' : '12.12.12.12'}
	
	header = get_header(data[:12])
	domain , typ , clas ,dname_b = get_query(data[12:])
	type_ = (1).to_bytes(2,byteorder='big')
	class_ = (1).to_bytes(2,byteorder='big')

	ttl = (400).to_bytes(4,byteorder='big')
	rdlength = (4).to_bytes(2,byteorder='big')
	if(domain[0]+'.'+domain[1] =='jamesbond.com'):
		
	
	
		rdata = (12).to_bytes(1,byteorder='big')+(12).to_bytes(1,byteorder='big')+(12).to_bytes(1,byteorder='big')+(12).to_bytes(1,byteorder='big')
	
	
		return header  + dname_b  +type_ +class_ +b'\xc0\x0c' + type_ +class_ + ttl + rdlength+rdata
	else :
		header = get_header(data[:12],'101')
		domain , typ , clas ,dname_b = get_query(data[12:])
		
		return header  + dname_b  +type_ +class_
	
		
	

## creating header for the packet
def get_header(data,error ='000'):
	# extracting transaction id for the request
	transaction_id= data[:2]
	
	#setting flag (2-byte long)
	flag = set_flag(error)

	QDCount = (1).to_bytes(2,byteorder='big')
	ANCount = (1).to_bytes(2,byteorder='big')
	NSCount = (0).to_bytes(2,byteorder='big')
	ARCount = (0).to_bytes(2,byteorder='big')
	
	
	
	return transaction_id + flag + QDCount + ANCount  + NSCount + ARCount
	
	
##creating  flags
def set_flag(error):
	
	QR ='1'	# Response(1)  query(0)
	OPCODE ='0000'  # standard query
	AA ='0'
	TC ='0'	#	truncation if packet is long
	RD='0'
	RA ='0'
	Z='000'
	RCODE = '0'+error
	
	# 2 -Byte flag 
	return int(QR+OPCODE+ AA + TC + RD + RA + Z + RCODE,2).to_bytes(2,byteorder='big')
	
##extracting the domain form the query
def get_query(data):
	
	domain=[]
	tmp=''
	length=0
	left_data_to_parse=0
	for i in data:
	
		left_data_to_parse= left_data_to_parse+1
		if(length !=0):
			 
			tmp =tmp+(chr(i))
			length =length -1
		else :	
			domain.append(tmp)
			tmp=''
			length =int(i)
			
			##end of domain name
			if(int(i)==0):
				
				break
				
	
	domain = domain[1:]		
	print(left_data_to_parse)
	type_ = data[left_data_to_parse:left_data_to_parse+2]
	left_data_to_parse =left_data_to_parse + 2
	class_ = data[left_data_to_parse:left_data_to_parse+2]
	
	return (domain,type_ ,class_ ,data[:left_data_to_parse-2])
	
	

## main function call 
if __name__=="__main__":
	
	main()
	



		
		
		
		
		
		
		
		
		
		
		
		
		
