#!/usr/bin/python

# A GUI version of IPchecker.py
# Checks for: your IP, hostname, IPv.
# If instead of "ip_address" variable you manuallu put a range
# of IPs encapsulated with ticks "'" (i.e. '199.99.99.0/24') it
# will also check for:
# hostmask, netmask, number of possible hosts with the IP range.
# TO DO: add GUI interface for the user to enter the IP.

import ipaddress
from tkinter import *
import socket

# Initiate Tk window
root = Tk()

# Root window dimesnions and title
root.geometry("500x550")
root.title("IPcheckerX")

# Placing local IP address and hostname in a variable
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# IP data
ip_version = ipaddress.ip_network(ip_address, strict=False)
'''HERE YOU CAN REPLACE "ip_address" IN THE BRACKETS WITH A RANGE
OF IP ADDRESSES IN CIDR NOTATION TO GET NUMBER OF POSSIBLE HOSTS
WITHIN A GIVEN IP RANGE'''

# nofh == number of hosts as string
nofh = str(ip_version.num_addresses)

# ipver == IP version as string
ipver = str(ip_version.version)

# hostmsk = hostmask as string
hostmsk = str(ip_version.hostmask)

# netmsk = netmsk as string
netmsk = str(ip_version.netmask)

# Labels in TK
label1 = Label(
    root, text="Your Host Name is: \n" + hostname, font = "Helvetica, 15"
    )
label1.pack(pady=10)
label2 = Label(
    root, text="Your IP Address is: \n" + ip_address, font = "Helvetica, 15"
    )
label2.pack(pady=10)
label3 = Label(
    root, text="Number of hosts: \n" + nofh, font = "Helvetica, 15"
    )
label3.pack(pady=10)
label4 = Label(
    root, text="This IP is ver: \n" + ipver, font = "Helvetica, 15"
    )
label4.pack(pady=10)
label5 = Label(
    root, text="Hostmask: \n" + hostmsk, font = "Helvetica, 15"
    )
label5.pack(pady=10)
label6 = Label(
    root, text="Netmask: \n" + netmsk, font = "Helvetica, 15"
    )
label6.pack(pady=10)

# Execute the Tk root window
root.mainloop()
