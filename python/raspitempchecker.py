#!/bin/python3 
#The script when run in the teminal will povide RaspberryPi temperature update every 1sec.

import time
import subprocess

i = 1
while i > 0: #Infinite loop.
    s = str(subprocess.getstatusoutput('sudo /opt/vc/bin/vcgencmd measure_temp'))

    print(s[5:-2]) #String has to be cut to povide just the temperature without aaditional information.
    time.sleep(1) #Wait 1sec before running the loop again.
