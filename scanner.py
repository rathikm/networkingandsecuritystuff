from scapy.all import *
import scapy.all as scapy

arprequest = scapy.ARP()
arprequest.pdst = "192.168.1.1/24" #This is where the IP range is defined, in the format of address/mask
broadcastrequest = scapy.Ether()
broadcastrequest.dst = "ff:ff:ff:ff:ff:ff"
combinedframe = broadcastrequest / arprequest
response, _ = scapy.srp(combinedframe, timeout=1)
for sent, received in response:
    print(received.summary())
