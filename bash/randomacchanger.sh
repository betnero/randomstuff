#1/bin/bash
service NetworkManager stop
ifconfig eth0 down
macchanger -r eth0
ifconfig eth0 up
ifconfig wlan0 down
macchanger -r wlan0
ifconfig wlan0 up
service NetworkManager start
