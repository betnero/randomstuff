#!/bin/env python3
#For reference see: https://docs.python.org/3.9/howto/ipaddress.html

import ipaddress


while True: #Infinite loop for script restart or shutdown                    

          try: #try/except for error control
                    #Prompt the user for IP or IP range and place it in a variable
                    ip = input('Enter a single IP or IP range in CIDR notation (i.e. 192.168.1.0/24): ')

                    #Put network information into a variable. "strict=False" to control ValuError in case the user provides a single IP address instead of an IP range.
                    net = ipaddress.ip_network(ip, strict=False)

                    #Print IPv., no. of hosts, hostmask and netmask.
                    print('This address is IPv', net.version)
                    print('Number of hosts: ', net.num_addresses)                    
                    print('Netmask: ', net.hostmask)
                    print('Hostmask: ', net.netmask)

          except:#Error prompt
                    print('Something went wrong...Please check the IP.')

          go_again = input('Want to do another one?... (y/n)')
          print()
          if go_again != 'y':
                    break
              
