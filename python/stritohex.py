#!/bin/env python3
#script converts strings into hex
"""
ord(x) returns a decimal representation of "x".
hex(x) function converts "x"
"""

#define user input
usr=input("Choose charcters to convert: ")

#transform each item from user input into decimal, than into hex and print it.
for i in usr:
    b=(((hex(ord(i)))))

    print((b).strip("0x"), end='')
    print(f" for {i}")

#take each item and print its hex representation in a single line cutting out all "0x".
for j in usr:
    b=((((hex(ord(j))))))
    print((b).strip('0x'), end='')
