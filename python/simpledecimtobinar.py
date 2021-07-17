#!/bin/env python3

try:
    usr = input("What number would you like to convert into binary?: ")
    num = int(usr)
    b = format(num, "b")
    print('Binary of ' + str(num) + ' is', b)
except:
    print("That's not a number...")
