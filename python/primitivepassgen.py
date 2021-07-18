#!/bin/python3
'''------------------------
!ATTNETION!
I wrote this code some time ago basing on various tutorials and examples available on the internet. 
It is suppose to be one of the very first attempts to learn Python by creating a password generator. 
Nevertheless I still decided to keep it here for educational purposes. 
For details please see comments.
------------------------'''

import random #"Random" should not be used for any security application. Python has a module called "secrets" for that.

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}[]|:;\'\\"~`<>?.,/-=_+' 
#You can write out all the characters manually but it's a lot of work and isn't very elegnat.
#Why not just sum strings like this: "string.ascii_letters + string.digits + string.punctuation"

length = input('Password length?: ')
length = int(length) #This could be written out in a single line

howmany = input('How many passwords?: ')
howmany = int(howmany) #This could be written out in a single line

for p in range(howmany):
    password = ''

    for i in range(length):
        password += random.choice(chars)
    print(password)
