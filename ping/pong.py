from socket import *
import sys
from struct import *

 

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
def getip_header(source_ip='10.64.12.230' ,dest_ip='10.64.12.230'):
    #source_ip = '10.64.12.230'
    #source_ip ='127.0.0.1'
    #dest_ip = '172.217.26.174' 
    #dest_ip = '127.0.0.1'
     
    # ip header fields
    ip_ver = 4
    ip_ihl = 5
    ip_tos = 0
    ip_tot_len = 0   
    ip_id = 123   
    ip_frag_off = 0
    ip_ttl = 255
    ip_proto = 17
    ip_check = 0  
    ip_saddr = inet_aton ( source_ip )   
    ip_daddr = inet_aton ( dest_ip )
     
    ip_ihl_ver = (ip_ver << 4) + ip_ihl
     

    ip_header = pack('!BBHHHBBH4s4s' , ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)
    return ip_header
                                                                                                                                                                                                                
def udp_header(udp_src = 8000 ,udp_dest = 8000 , data = "pong"):
     
                                        
    udp_checksum =0                                                                                                                                                     
    udp_data = data
    udp_len = 12 #len(udp_data)


    udp_header = pack('!HHH4s' ,udp_src , udp_dest , udp_len ,bytes(udp_data ,'utf-8')  )
     
    psh = udp_header ;
     
    checksum_part = checksum(psh)

    udp_header = pack('!HHHH4s' ,udp_src , udp_dest , udp_len ,0  ,bytes(udp_data ,'utf-8') )
    return udp_header


 
recv_sock = socket(AF_INET, SOCK_DGRAM)
recv_sock.bind(('127.0.0.1', 8000))

print ("The server is now listening...")
while True:
    print("data_Before rec")
    data , addr = recv_sock.recvfrom(8000)
    print(data)

    packet = getip_header('127.0.0.1',dest_ip='127.0.0.1') + udp_header(8000 ,udp_dest =addr[1]) 
    
    #data, addr = sock1.recvfrom(1024)
    print("data sent 'pong' ") 
    x =s.sendto(packet, ('',8000 ))
    print("=============================")



		
		
		
		
		
		
		
		
		
		
		
		