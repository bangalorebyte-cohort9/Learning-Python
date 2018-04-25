from socket import *
from time import ctime

host = '192.168.0.126'
port = 2000
addr = (host,port)

# Create a socket python object
tcpservsocket = socket(AF_INET,SOCK_STREAM)

# Bind the socket to the address using bind built in method
tcpservsocket.bind(addr)

# Start listening to the client request 
tcpservsocket.listen(10)

while True:
    #Accept the client connection
    print('Server is ready to accpet client connection')
    tcpclient,tcpaddr = tcpservsocket.accept()
    print('The Client Address', tcpaddr)
    
    while True:
        data = tcpclient.recv(1024)
        if not data:
            break
        datatosend = ctime() + ' ' + data.decode()
        
        tcpclient.send(datatosend.encode())
    tcpclient.close()
    
tcpservsocket.close()