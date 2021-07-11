import secrets
import string

#DISCLAIMER
print()
print("-" * 75)
print("DISCLAIMER: ")
print("A password to be considered secure should be at least 12 characters long. It should include special characters, upper- and lowercase letters and digits.")
print("-" * 75)
print("ATTENTION!: ")
print("This password gpassword enrator is a PoC and should not be considered fully secure. It should be treated as an assistive measure only.")
print("The user takes full responsibility of any direct or indirect damage inflicted by propper or inproper use of the software or its parts.")
print("-" * 75)
print()

# Looped to enable the user to run the script again or quit.
while True:
    
    # User input placed in a var
    usr = input("How long do you want the pasword to be? (min.5 characters) ")
    # Turn user input into an integer
    usr = int(usr)
    print()

    # Definition of scope of numbers to be used for password generation
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Looped to generate password with min. requirements being: at least 1 uppercase, 1 lowercasr and 3 digits
    while True:

        # Join all parts of the variable "alphabet" and itterate the number of times indicated by the user
        password = "".join(secrets.choice(alphabet) for i in range(usr))

        # Check if the password meets minimum requirements
        if (any(i.islower() for i in password)
                and any(i.isupper() for i in password)
                and sum(i.isdigit() for i in password) >= 3):
            break

    # Print the result
    print(password)
    print()

    # Ask the user if another password will be generated or quit
    go_again = input("Want to do another one?... (y/n)") 
    if go_again != "y":
        if go_again != "Y":
            break
