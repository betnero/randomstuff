#!/bin/env python3

""" The script will create as many files as indicated in the n variable
(in this case 10 files). File names will be named with random numbers.
 WARNING! : creating too many files on your computer may fill up your
 disk space and crash the computer. Use at your own risk."""

# For additional features research: from unicodedata import name
import random

i = 0
n = 10
while i < n:
    name = str(random.randrange(1, 100)) + ".txt"
    f = open(name, "w+")
    i += 1
