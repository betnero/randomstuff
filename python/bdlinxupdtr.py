#!/bin/env python3
# This script is suppose to update
# and upgrade Linux but is slow.
# Done purely as a PoC.
# Better off doing updates manually or use a bash script.

from subprocess import call


call(["sudo", "apt-get", "update"])
print("\n")
print("-."*50)
print('                         ***  UPDATE DONE...  ***')
print("-."*50)
print("\n")
print("-."*50)
call(["sudo", "apt-get", "upgrade", "-y"])
print("-."*50)
print("\n")
print("-."*50)
print('                         ***  UPGRADE DONE...  ***')
print("-."*50)
print("\n")
