import socket
SERVER = "127.0.0.1"
PORT = 123
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client",'UTF-8'))
while True:
  in_data =  client.recv(1024)
  out_data = input()
  client.send(bytes(out_data,'UTF-8'))
  if out_data=='bye':
  break
client.close()
