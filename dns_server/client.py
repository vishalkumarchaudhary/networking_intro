

from socket import *


def main():
	server_port = 53
	serverName = '127.0.0.1'
	
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	dns_req = get_packet_req()
	
	clientSocket.sendto(dns_req, ( serverName ,server_port) )
	
	data, server =clientSocket.recvfrom(512)
	ip =get_domain_ip(data[12:])
	 
	for i in ip:
		print(i)
	
	clientSocket.close()
	
		


### creating dns response 
def get_packet_req():
	
	header = get_header()
	domain = 'howcode.org'
	
	encrypt_domain = encr_domain(domain)
	
	
	#rdata = (10).to_bytes(1,byteorder='big')+(10).to_bytes(1,byteorder='big')+(10).to_bytes(1,byteorder='big')+(10).to_bytes(1,byteorder='big')
	
	
	return header  + encrypt_domain 
		
	
def encr_domain(domain):
	encr =b''
	count =0
	
	for i in domain[::-1]:
		if i=='.' :
			encr =  int(count).to_bytes(1,byteorder='big') + encr 
			count = 0
			continue 
		encr = int.from_bytes(i.encode(), byteorder='big').to_bytes(1,byteorder='big') +encr 
		count = count+1 
		
		
	encr =  int(count).to_bytes(1,byteorder='big') +encr 
		
	return encr + b'\x00\x00\x01\x00\x01' ## end of domain name , class and type 

## creating header for the packet
def get_header():
	# extracting transaction id for the request
	transaction_id= (512).to_bytes(2,byteorder='big')
	
	#setting flag (2-byte long)
	flag = set_flag()

	QDCount = (1).to_bytes(2,byteorder='big')
	ANCount = (0).to_bytes(2,byteorder='big')
	NSCount = (0).to_bytes(2,byteorder='big')
	ARCount = (0).to_bytes(2,byteorder='big')
	
	
	
	return transaction_id + flag + QDCount + ANCount  + NSCount + ARCount
	
	
##creating  flags
def set_flag():
	
	QR ='0'	# Response(1)  query(0)
	OPCODE ='0000'  # standard query
	AA ='0'
	TC ='0'	#	truncation if packet is long
	RD='0'
	RA ='0'
	Z='000'
	RCODE = '0000'
	
	# 2 -Byte flag 
	return int(QR+OPCODE+ AA + TC + RD + RA + Z + RCODE,2).to_bytes(2,byteorder='big')
	
##extracting the domain form the query
def get_domain_ip(data):
 
	data = slice_domain(data)
	data = data[4:] #class ,type
 
	##	from answer
	data = slice_domain(data)
	data = data[4:] #class ,type
	 
	data = data[4+2:] ## ttl ,rdlength 
	ip=[]
	tmp =''
	for i in range(4):
		tmp = tmp + str(int.from_bytes(data[i:i+1], byteorder='big'))+'.'
	ip.append( tmp[:-1])
	
	
	
	return ip
	
def slice_domain(data):
	length=0
	left_data_to_parse=0
	for i in data:
		left_data_to_parse= left_data_to_parse+1
		if(length !=0):
			length =length -1
		else :	
			length =int(i)
			
			##end of domain name
			if(int(i)==0):
				
				break
	return data[left_data_to_parse:]

## main function call 
if __name__=="__main__":
	main()
	



		
		
		
		
		
		
		
		
		
		
		
		
		
