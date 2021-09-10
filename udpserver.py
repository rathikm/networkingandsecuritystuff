import socket
shost = "localhost"
sport = 10000

udpserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpserver.bind((shost, sport))
while True:
    print("Waiting for client connection")
    data, addr = udpserver.recvfrom(4096)
    if data != None:
        print(data)
        break

""" The UDP server allows us to check that our UDP client is working. We use the localhost
address as our target for our UDP connection, so our server must also be binded to the
localhost as seen in the socket.bind() call. The server simply runs in an infinite state
until it receives data, at which point it prints out and ends.
"""