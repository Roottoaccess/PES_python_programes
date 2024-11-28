"""Today the concept of iterator"""
"""__iter__() private method"""
"""__next__() private method"""

"""list tuple string are iterable"""


"""The next() function manually iterates through all the items of an iterator"""

"""Trying the concept"""


"""List iterator"""
my_list = [4,0,7,9]

print(type(my_list))

iter_1 = iter(my_list)
print(type(iter_1))

"""Set iterator"""
t = {1,2,3,4,5,6}
print(type(t))

iter_2 = iter(t)
print(type(iter_2))

"""String iterator"""
s = "Python"
print(type(s))

iter_3 = iter(s)
print(type(iter_3))

"""Tupple iterator"""
t1 = (1,2,3,4,5,6)
print(type(t1))

iter_4 = iter(t1)
print(type(iter_4))

"""Dictionary iterator"""
d = {1: "One",
     2: "Two"}

print(type(d))

print(type(iter(d)))

# It is giving an object
print(iter_1)

print(next(iter_1)) # giving the first element in the list

print(next(iter_1)) # pointing to the second element..
print(type(iter_1.__next__())) # The elements of the list are integer


print(type(iter_3.__next__())) # The elements of the list are string


"""This is the program where we are using the iterator next() function with the exception handeling concepts"""
l_ = [1,2,3,4,5]

l_iterator = iter(l_)

try:
    while True:
        element = next(l_iterator)
        print(element)
except StopIteration:
    pass