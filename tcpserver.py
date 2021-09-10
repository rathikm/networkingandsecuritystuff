import socket, threading

shost = "localhost"
sport = 9999

tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpserver.bind((shost, sport))
tcpserver.listen(5) #5 is the max number of connections that can be queued

def clienthandler(clientsocket):
    tcpclientreq = clientsocket.recv(1024)
    print("Received a request with the following data: " + tcpclientreq.decode('UTF-8'))
    clientsocket.send(b'Connection successful')
    clientsocket.close()

while True:
    tcpclient, tcpclientaddr = tcpserver.accept()
    print(f'Accepted connection from: {tcpclientaddr[0]}:{tcpclientaddr[1]}')
    handlerthread = threading.Thread(target=clienthandler,args=(tcpclient,))
    handlerthread.start()