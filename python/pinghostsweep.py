#!/bin/env python3

import subprocess
import socket
from time import sleep

# ping IPs wthin a given range
for ping in range(1, 256): # IP range
    address = "192.168.147." + str(ping) # First 3 octets + an item from IP rnage
    res = subprocess.call(['ping', '-c', '1', address]) # Ping sweep
  
    # sleep 1 sec to avoid FW alerts (optional; shouldn't work if the FW is properly configured).
    sleep(1)

    # if an IP is active (status 0) inform the user that the host is up. Put the IP and the host name in a .txt file
    if res == 0:
        print("-" * 50)
        print( "PING TO: ", address, "!!!!!!!!!HOST IS UP!!!!!!!!!!")
        print("-" * 50)
  
        # write to a file
        f = open("echoscan.txt", "a")
        f.write(address)
        f.write(' ')
        
        # find host name and write to a file with IP
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        f.write(host_name)
        f.write('\n')
        f.close()
 
 ''' 
 TO DO:
 - make the IP range a user input
 - make the "address" variable a user input
 - make sleep time adjustable by the user
 - consider putting active IPs in one file and active hosts with IP in a different file
 - provide a user to perform some predifined nmap scans once the ping sweep is done and put results in a different file
 - add threading to speed the scanning up
 '''
 
