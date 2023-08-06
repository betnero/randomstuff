#!/bin/env python3

import subprocess
import socket
# from time import sleep

# create a file to write scan results to
f = open("echoscan.txt", "w+")


# ping IPs wthin a given range
for ping in range(1, 256):  # IP range

    address = "111.111.111." + str(ping)  # First 3 octets + an IP from range
    res = subprocess.call(['ping', '-c', '1', address])  # Ping sweep

    # sleep 1 sec to avoid FW alerts (optional;
    # shouldn't work if the FW is properly configured). OPTIONAL.
    # sleep(1)

    # if an IP is active (status 0) inform the user that the host is up.
    if res == 0:
        print("-" * 50)
        print("PING TO: ", address, "!!!!!!!!!HOST IS UP!!!!!!!!!")
        print("-" * 50)

        # write the IP to a file
        f = open("echoscan.txt", "a")
        f.write(address)
        f.write(' ')

        # find hostname and write it to a file next to the IP
        hostName = socket.gethostname()
        hostIP = socket.gethostbyname(hostName)
        f.write(hostName)
        f.write('\n')
        f.close()
'''
TO DO:
 - make the IP range a user input
 - make the "address" variable a user input
 - make sleep time adjustable by the user
 - consider putting active IPs in one file
  and active hosts with IP in a different file
 - provide a user to perform some predifined
  nmap scans once the ping sweep is done
  and put results in a different file
 - add threading to speed the scanning up
 - add argparse to introduce flags for each
  feature (i.e. user to specify the IP (first 3 octets),
  full scan of all hosts within a network,
 sleep for a specific time between each IP scan,
  specify upper and lower IP range)'''
