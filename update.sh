#!/bin/bash

#Ornamental part used across the script
star="************************************"


#Check what's thedistr and put it in a variable
os=$(cat /etc/os-release | grep ID= | tr -d ID= | head -n 1)

if [[ $os="Manjaro" || $os="manjaro" ]]
	then
	pckg_manager="pamac"
	updt="sudo $pckg_manager update"

elif [[ $os="Arch" || $os="arch" ]]
	then 
	pckg_manager="pacman"

elif [[ $os="Debian" || $os="debian" || $os="Ubuntu" || $os="ubuntu" || $os="Kali" || $os="kali" ]]
        then 
        pckg_manager="apt"

elif [[ $os="Arch" || $os="arch" ]]
        then 
        pckg_manager="pacman"

fi

echo "$star"
echo "Your are on $os."
echo "Your package manager is $pckg_manager"
echo "$star"
($updt)
