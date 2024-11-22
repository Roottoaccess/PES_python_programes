# This is the understanding off all the complex concept in python....

"""Creating the normal functions"""

# def double(x):
#     return x ** 2;

# Calling the function (Anonymous functions....)
# double = lambda x: x ** 2
# print(double(5))

# Its also capable for givin the output of the average value....
# avg = lambda x,y: (x + y) / 2; print(avg(3,5))

# we can pass the function of a function....
# def appl(fx, value):
#     return 6 + fx(value)

# print(appl(double, 4))

# learning the map, filter, reduce function in python....
# def cube(x):
#     return x ** 3

# print(cube(125))

l = [1,2,3,4,5,6,7,8]

# newl = []

# for _ in l:
#     newl.append(cube(_))

newl = list(map(lambda x: x**3, l))
print(newl)

# Filter function....
# def filter_function(a):
#     return a > 4

newnewl = list(filter(lambda x: x > 4, l))
print("This are the elements which are greater than 4..",newnewl)

"""Map , filter, reduce are the higher order functions...."""


# This is the reduce function
from functools import reduce
number = [1,2,3,4,5]

sum = reduce(lambda x, y: x + y, number)

print(sum)