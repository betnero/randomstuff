#!/bin/env python3

# import sys
import os


def updt():

    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade -y')
    os.system('sudo apt update')
    os.system('sudo apt-get autoremove')
    os.system('sudo apt-get autoclean')
    os.system('sudo apt-get clean')
    os.system('sudo apt-get dist-upgrade')


updt()
