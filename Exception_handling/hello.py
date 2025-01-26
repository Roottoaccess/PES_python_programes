# This is the Exception Handling Logic in python....

# try and except in python !

def get_int(prompt): # Creating the function !
    while True:
        try:
            return int(input(prompt))
            
        except ValueError:
            # print("x is not an integer")
            pass

def main(): # Defining the function !!
    x = get_int("What's x? ")
    print(f"x is {x}")

main() # Calling the function !!

# Raising exceptions in python!!
