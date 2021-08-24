#!/bin/python3
'''------------------------
!ATTNETION!
This code should NOT be considered secure. 
Use it at your own risk. 
Using "random" for security purpose may introduce vulnerabilities. 
Security applications should be implemented with the use of "secrets" module.

I wrote this code starting out with Python a long time ago and based it on various tutorials and examples available on the internet. 
Nevertheless I still decided to keep it here for educational purposes. 
For details please see comments.
------------------------'''

import random #"Random" module should not be used for security applications. Python has a module called "secrets" for that.

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}[]|:;\'\\"~`<>?.,/-=_+' 
'''You can write out all the characters manually but it's a lot of work and isn't very elegant.
Why not just sum strings like this: "string.ascii_letters + string.digits + string.punctuation'''

length = input('Password length?: ')
length = int(length) #This could be written out in a single line. Repeating is a bad practice.

howmany = input('How many passwords?: ')
howmany = int(howmany) #Repetition again. See previous comment.

for p in range(howmany):
    password = ''

    for i in range(length):
        password += random.choice(chars)
    print(password)
