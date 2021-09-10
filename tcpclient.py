import socket
thost = "localhost"
tport = 9999

tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpclient.connect((thost, tport))
tcpclient.send(b'Requesting connection')
res = tcpclient.recv(100)
print(res)
tcpclient.close()

"""This is a very basic TCP client. Essentially, this sets up a socket (or connection)
with the target host and port of choice. Here, we are sending a GET HTTP request over the
HTTP protocol (hence port 80). We are then receiving the data, but only storing a certain
buffer of the response (in this case, 100). Lastly, we print."""