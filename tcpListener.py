#! /usr/bin/python3

import socket

#Define variables to hold info for the TCP/IP address, listen port, 
# buffer size of the data we want to capture from the connecting system.
TCP_IP = "192.168.0.122"
TCP_PORT = 6996
BUFFER_SIZE = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # define the socket
s.bind((TCP_IP, TCP_PORT))                                  # bind the socket to the IP address and port w/ variables
s.listen(1)                                                 # tell the socket to listen using listen() method

# capture the IP address and port of the connecting system using accept() method
# print that info the the screen
conn, addr = s.accept()
print('Connection address: ', addr)

while True:                                                 # keep running loop and checking for data until program is stopped
    
    # place information from connecting system into a buffer, print is, and then close the connection
    data=conn.recv(BUFFER_SIZE)                             
    if not data:
        break
    print("Received data: ", data)
    conn.send(data)                     # echo
    conn.close()