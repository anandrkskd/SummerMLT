#!/usr/bin/python2

import socket 
from time import sleep as ts
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for i in range(0,7):
	if i//2:
		a="hiiii this is my naeme"
#		b=a.encode('utf-8')
		s.sendto(a,("127.0.0.1",9999))				
		ts(5)
	else:
		a="namesta mera name yahi hai"
#		b=a.encode('utf-8')	
		s.sendto(a,("127.0.0.1",9999))
		ts(5)

