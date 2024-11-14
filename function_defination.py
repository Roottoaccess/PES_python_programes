# This is the defination about the function in class

# creating a function
def Demo_function(name, age):
    print(name, age)

# calling the function
Demo_function(24, "Jeet")


# This is the variable length arguments
# def mul(* num):
#     prod = 1
#     for i in num:
#         prod = prod * i
#         print("product: ",prod)

# mul(3, 5)


# This is another example of the function
def display(name, age):
    age += 10
    print(f"{name} will be aged {age} years after 10 years")

display("BBB", 30)

# display(30, "BBB") required arguiment were the number is important

# Keywords Arguments
def dis(name, age):
    age += 10
    print(f"{name} will be aged {age} years in 2034")

dis(age = 45, name = "BBB")

# testing.....
# dis(age = 45 , "BBB") is giving and error.....
# dis("BBB", age = 45) working fine !


# Default arguiments
def display1(name, age= 45):
    age += 10
    print(f"{name} has aged to {age} in 10 years")
display1("JJJ")

display1("JJJ", 34) # changing the age as 34

display1(age = 88, name = "AAA") # working fine !

# display1(67, name = "BBB") this is not working ! error

# variable length arguments
def sum(*input):
    s = input[0]
    # print(type(input))
    for _ in input[1:]:
        s += _
    return s
s1 = sum(10, 20)
s2 = sum(4)
s3 = sum(1,2,3,4,5,6,7,8,9,10)
s4 = sum("Python"," ","Programming")
s5 = sum([1,2,3,4],[5,6,7,8])


print(s1, s2, s3, s4, s5)

def dis1(name, age, *marks):
    print(f"{name} of age {age} has scored {marks, type(marks)}")

dis1("Biswarup", 22, 88, 85, 92, 98)

dis1(age = 16, name = "BBB", marks= (90, 92))