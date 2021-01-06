import socket
import sys
import time
from threading import *


def receiver(ip, port):
    myp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, myp)
    s.bind((ip, port))
    while True:
        x = s.recvfrom(1024)
        print('Received Message : ',x[0].decode())
        time.sleep(0.2)

def sender(ip2, port2):
    myp = socket.SOCK_DGRAM
    afn = socket.AF_INET
    s = socket.socket(afn, myp)
    while True:
        msg = input()
        s.sendto(msg.encode(), (ip2, port2))
        print('Your Message : ', msg)
        time.sleep(0.1)

ip = input("Enter Reciever's IP address: ")
port = int(input("Enter Reciever's port number : "))

ip2 = input("Enter sender's IP address : ")
port2 = int(input("Enter sender's port number : "))

t1 = Thread(target=sender, args=(ip2, port2))
t2 = Thread(target=receiver, args=(ip, port))

t1.start()
t2.start()
