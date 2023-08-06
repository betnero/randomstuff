#!/bin/env python3

while True:  # The loop together with the go_again variable
    # will enable program restart at users will

    try:  # try: except: mechanism for user input validation
        print()  # Print empty line
        usr = input("What is your number?: ")  # User input
        print('{0:08b}'.format(int(usr)))  # Binary represntation of user input
        print()

        #  Print user input length
        print("Number of digits entered: ")
        print(len(usr))
        print()

        #  Print length of the binary convertion
        print("Number of bits in the number (min.8): ")
        print(len('{0:08b}'.format(int(usr))))
        print()

    except Exception:
        print("That's not a number. Please enter a number.")  # User prompt

    go_again = input("Want to do another one?... (y/n)")
    if go_again != "y":
        break
