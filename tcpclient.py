from socket import *


host = '192.168.0.126'
port = 2000
addr = (host,port)

tcpclient = socket(AF_INET, SOCK_STREAM)
tcpclient.connect(addr)

while True:
    data = input('Enter Message to Server   ')
    tcpclient.send(data.encode())
    
    datafromserver = tcpclient.recv(1024)
    print(datafromserver.decode())

tcpclient.close()

