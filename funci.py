# def outer_func(who):
#     def inner_func():
#         print(f"Hello {who}")
#     inner_func()
# name = input("Value? ")
# outer_func(name)

# This is a simple example of inner function calling....
# def outer_func():
#     def inner_func():
#         print("Inner function called")
#     inner_func()
# outer_func()

# Outer functions with variables.....
# def outer_func():
#     x = 100
#     def inner_func():
#         print(x)
#     inner_func()
# outer_func()

# Variables inside both the functions.....
"""global and local variables"""
# def outer_func():
#     x = 100
#     def inner_func():
#         x = 10
#         print(id(x), x, sep=",")
#     inner_func()
#     print(id(x), x, sep=",")
# outer_func()

"""Global variables"""
# def outer_func():
#     x = 100
#     print("Inside Outer: ", x, id(x))
#     def inner_func():
#         nonlocal x
#         print("Inside Inner: ",x, id(x))
#         x = 10
#         print("After changing: ", x, id(x))
#     inner_func()
#     print("After call: ", x, id(x))
# outer_func()

"""Passing outer function parameters"""

# def outer_func(x):
#     def inner_func(y):
#         print(f"The value read is {y}")
#     inner_func(55)
#     print(f"The value read is {x}")
# outer_func(45)


# def outer_func(x):
#     def inner_func(x):
#         print(f"The value read is {x}")
#     inner_func(10)
#     print(f"The value read is {x}")
# outer_func(100)

"""HomeWork"""
# Question> Define a function called as even or odd that takes in a parameter x and prints whether the x is even or odd....

# Question> Define a function called as display that takes in 2 values start and end it should display all even numbers between start and end.... if end is laser than the start and make end as start and start as end.....

# def even_odd(x):
#     if x % 2 == 0:
#         print(f"The value of {x} is even....")
#     else:
#         print(f"The value of {x} is odd....")
# even_odd(3)

# def pattern choice....
def choice_menu():
    # Taking the input from the user user to get into the program
    cm = int(input("What's would you like 'press 1' for abstruct pattern and 'press 2' for Number pattern: "))

    if cm == 1:
        def abstructpattern():
            while True:
                cap = int(input("Enter 1 for star pattern and 2 for reverse star pattern: "))
                if cap == 1:
                    print("*\n**\n***\n****")
                    break
                elif cap == 2:
                    print("****\n***\n**\n*")
                    break
                else:
                    pass
        abstructpattern() #calling the abstructpattern......
    elif cm == 2:
        def numberpattern():
            while True:
                npc = int(input("Enter 1 for simple '1s pattern', 2 for 'number increment pattern', 3 for 'another number pattern': "))

                if npc == 1:
                    print("1\n11\n111\n1111")
                    break
                elif npc == 2:
                    print("1\n12\n123\n1234")
                    break
                elif npc == 3:
                    print("1\n11\n121\n1221")
                    break
                else:
                    pass
        numberpattern() # Calling teh numberpattern function.....
choice_menu() #calling the main function.....