#!/bin/python3

import sys,socket
from datetime import datetime


#define our target 
if len(sys.argv)==2:
   target=socket.gethostbyname(sys.argv[1]) #translate host name to ip
else:
     print("invalid arguments")
     print("Syntax: python3 scanner.py <ip>")
#add a banner
print("-" *50)
print("scanning target: "+target)
print("Time started : "+str(datetime.now()))
print("-" *50)

try:
    for port in range(50,85):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result==0:
           print(f"port {port} is open")
           s.close()
           
except KeyboardInterrupt:
       print("\nExitting program.")
       sys.exit()
except socket.gaierror:
       print("hostname could not be resolved.")
       sys.exit()
except socket.error:
       print("could not connect to server .")
       sys.exit()
