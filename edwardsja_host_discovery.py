#Name: Jake Edwards
#Date: 2/14/2019
#Professor: Dr. Glendowne
#Class: CSC 435-001

import socket
import ipaddress
import sys

port = 55123 #random high level port

choice = int(input("Enter 0 to search a network or Enter 1 to search a specific address: "))
if choice == 0: #Network
    CIDR = input("Enter a CIDR (ex. 123.123.123.123/16): ")
    network = ipaddress.ip_network(CIDR, strict=False)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        for addr in network.hosts():
            client.connect((str(addr), port))
            msg = "Jake was here"
            client.send(msg.encode())
            print("sent to " + str(addr))

elif choice == 1: #Specific Address
    IPaddr = input("Enter IP address (ex. 45.33.32.156): ")

    #Create socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        #Attempt to connect
        client.connect((IPaddr, port))

        msg = "Test message from Jake"
        client.send(msg.encode())
        print("Message sent")
