# This is the functions lecture practising the lecture

def printme(name, age = 40):
    "This prints a passed string into this function"

    print(name, age)

"""Required Arguiments"""

# printme("Jeet", 24)

# So what will happen if we give only one input when we are calling the function...
"""so this will give us an error it will say only one arguiment has passed"""
# printme("Jeet")

"""Keyword Arguments"""
# printme(age = 24, name = "Jeet")

# Again if we pass 1 arguiment it will throw as error

"""Default Arguiments"""
# def printme(name, age = 40):

# printme("Jeet")

# Variable length Arguments
"""Variable length Arguments can take n numbers of arguiments"""
def multiplier(*num):
    prod = 1
    for _ in num:
        prod *= _
    print(f"Product {prod}")
# Calling the multiplier function..
multiplier(3,5,15,55)

# Lets create some another function regarding the concept of variable length arguiments

def sum(*numb):
    sum = 0
    for _ in numb:
        sum += _
    print(f"Addition Result is {sum}")
# Calling the function
sum(3,4,5,6,7,8)