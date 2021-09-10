import socket
thost = "localhost"
tport = 10000

udpclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udpclient.sendto(b'Sample UDP Datagram', (thost, tport))

"""This is very similar to the TCP Client code. The main differences to watch out for are
the lack of a socket.connect() call and the socket.sendto() method. You may have noticed
that the UDP client socket was defined with the SOCK_DGRAM constant rather than 
SOCK_STREAM. Also, socket.connect() was never called. This is because UDP is a 
CONNECTIONLESS protocol. It sends the UDP packet, known as a datagram, without worrying
about whether it reaches its destination or not. To compensate, the socket library has a
sendto() method, which takes in data and a tuple of a target host or port, a.k.a. a socket."""
