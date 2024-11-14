# This is the program to call the name of an animal

def main(animal):
    if animal == "cat":
        print("meos")
    elif animal == "dog":
        print("bhow")
    else:
        print("who?")

def animal_type():
    # Taking the input from the user
    name = input("What's the name of the animal? ")
    # Giving the value in the function
    main(name)


# Calling the function.....
animal_type()
