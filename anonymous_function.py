# Anonymous Function
"""
which is called as lambda function...
lambda function are single line function

lambda function is generally used as an arguiment to a higher-order function ..
"""

# x = lambda a : a + 10
# print(x(5))

# This is a lambda function for addition..
# x = lambda a,b: a + b
# print(x(5,15))

# We can use any other function with lambda....

# Need to complete the map and the lambda function
# MAP FUNCTION
"""The function map takes two arguiments - a callable and an iterable.."""

# a = ['apple', 'pineapple', 'fg', 'mangoes']
# b = list(map(len, a))

# print(b)

# take a list apply the map with the lambda function which give the square of every numbers

# num = [1,2,3,4,5] #creating the list
# b = list(map(lambda num : num * num))

# print(b)

# x = list(map(lambda y : y * 5, [1,2,3,4,5,6,7]))

# print(x)

# Using lambda generate table of 5
# table_of_5 = list(map(lambda x: x * 5, range(1, 11)))
# print("Table of 5:", table_of_5)

# filter() function....
"""There are cases where there is a need to remove a few elements of the input iterable , a lazy iterable of 0 to n"""

"""In python laze is a technical term.. """
seq = [0, 1, 2, 3, 5, 8, 13]
# Filter will open and close.....
print(list(filter(lambda x : x % 2 != 0, seq)))

print(list(filter(lambda x : x % 2 == 0, seq)))

# A filter function print negative values in a given list
x = [9, 8, -1, -5, 6, 88]
print(list(filter(lambda y: y < 0, x))) # if the list is not there it will not give you that is known as lazy iterable

# Using map and filter give the squares of even numbers in a list....
y = [3,2,20,28,39,88]

print(list(map(lambda x: x * x, list(filter(lambda x : x % 2 == 0, y)))))


# Reduce function
from functools import reduce
nums = [1,2,3,4]
ans = reduce(lambda x, y: x + y, nums)
print(ans)

# Sum of the square of the odd numbers in a given list??
print(reduce(lambda x,y : x + y, list(map (lambda x: x * x, list(filter(lambda x: x%2 != 0, [1,2,3,4,5,6,7,8,9,10]))))))
