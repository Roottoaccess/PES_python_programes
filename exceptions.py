# This is the progam where we are learning who to handle the exception

# Writing the code with handelling the error.....

# when I use else that means that this things are mutually exclude
def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

# Calling the function
main()