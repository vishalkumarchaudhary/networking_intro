# networking_intro
All of the programs work in python3 version

Dns server is the dummy dns server which work for only one domain resolution name jamesbond.com

To test dns server / client     in /dns_server
```
sudo python3 server.py 
nslookup jamesbond.com 127.0.0.1
python3 client.py jamesbond.com 127.0.0.1
```

To test ping in /ping
```
sudo python3 ping.py
```
then enter ```google.com``` or any other
This is made using raw socket using |icmp|ip| packet with echo request to machine




