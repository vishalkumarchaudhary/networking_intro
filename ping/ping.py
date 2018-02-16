from socket import *
import sys
from struct import *
from time import time

def checksum(msg):
    s = 0 
    # loop taking 2 characters at a time
    for i in range(0, len(msg), 2):
    	 
    	w = (msg[i]<<8 )+ msg[i+1]
    	 
    	s = s + w
     
    s = (s>>16) + (s & 0xffff);
    s = (s & 0xffff) + (s >> 16);
    
    s = ~s & 0xffff
    return s
    
    
#create a raw socket
s = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)
 
     
# now start constructing the packet
packet = '';
 
source_ip = '10.64.12.230'
#source_ip ='127.0.0.1'
dest_ip = '172.217.26.174' 
#dest_ip = '127.0.0.1'
 
# ip header fields
ip_ver = 4
ip_ihl = 5
ip_tos = 0
ip_tot_len = 0   
ip_id = 123   
ip_frag_off = 0
ip_ttl = 255
ip_proto = 1
ip_check = 0  
ip_saddr = inet_aton ( source_ip )   
ip_daddr = inet_aton ( dest_ip )
 
ip_ihl_ver = (ip_ver << 4) + ip_ihl
 

ip_header = pack('!BBHHHBBH4s4s' , ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)
 

# icmp header fields
icmp_tom = 8

icmp_code = 0
icmp_checksum=0
icmp_hdata=1

icmp_header = pack('!BBHHH' ,icmp_tom , icmp_code  ,icmp_hdata ,icmp_hdata,icmp_hdata)
 
psh = icmp_header ;
 
checksum_part = checksum(psh)

 
icmp_header = pack('!BBHHHH' ,icmp_tom , icmp_code ,checksum_part ,icmp_hdata ,icmp_hdata,icmp_hdata)
print(type(icmp_header))
packet = ip_header + icmp_header  
 
 
hostname = input("host name : ")
while(1):
	x =s.sendto(packet, (hostname,0 )) 
	time_sent = time()
	y = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP)
	data, server =y.recvfrom(2048)
	time_recv = time()
	x =s.sendto(data[4:], ('google.com',0 )) 
	print("ping received ,ttl ",time_recv-time_sent)


## main function call 
if __name__=="__main__":
	print("yes")	
 


		
		
		
		
		
		
		
		
		
		
		
		
