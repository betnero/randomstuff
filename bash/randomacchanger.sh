#/bin/bash

#the script launches macchange and changes MAC of a chosen interface to a random value

echo " "
sepearator="--------------------------------------------"
echo "These are your interfaces: " 
eval "ls /sys/class/net/" #list folders -- their names represent names of the intefaces on the machine

echo $sepearator

read -p "Enter interface name: " intrf # intrf is interface name variable

echo $sepearator

#number of macchanger commands normally entered manually
eval "service NetworkManager stop"
eval "ifconfig $intrf down" 
eval "macchanger -r $intrf"
eval "ifconfig $intrf up"
eval "service NetworkManager start"

echo $sepearator

echo "MAC for $intrf changed..."
echo " "