# a = list(input("Enter the elements ").split())

# b = tuple(input("Enter the elements ").split())
# # This is a list and list
# zip(a,b)
# print(list(zip(a,b)))

# String and list..
n = "Hello"
n1 = [1,2,3,4,5]

zip(n,n1)
print(list(zip(n,n1)))

# This is the dictionary which is zipping..
d = {
    "Name": "Biswarup"
}

d1 = {
    "Sec": "A"
}

test = zip(d,d1)
print(dict(test))

"""The max function.... This function is used to computer teh maximum of the value passed in its argument and lexigographically largest value if string are passed as arguments"""

ii = 8; ff = 9.8
print(max(ii, ff))

demo = [10,1],[10,2],[10,3]
print(max(demo))

emo = [1,2,3], [5,6], [10,20]
print(max(emo))

rr = 'apple','Apple','APple','aPPle'
print(max(rr))

# dd = {1: 'a', 2: 'b'}, {1: 'A', 2: 'B'}
# print(max(dd)) # Not allowing....

# ddd = {1: 'a'}, {0: 'a'}, {-1, 'A'}
# print(max(ddd)) # This is also not supporting
print("Min-->")

# Min opposite value
ii = 8; ff = 9.8
print(min(ii, ff))

demo = [10,1],[10,2],[10,3]
print(min(demo))

emo = [1,2,3], [5,6], [10,20]
print(min(emo))

rr = 'apple','Apple','APple','aPPle'
print(min(rr))

"""This is the operator learning"""
import operator as o
print("Addition-> ", o.add(45,34))

print("Substraction-> ", o.sub(23,12))

print("Multiple-> ", o.mul(23,45))

print(o.truediv(35, 3))

print(o.floordiv(35,2))

print(o.mod(35,2))

print(o.pow(3,4))

print("Excercise---->")
# Excercise
maximum = lambda x,y: max(x,y)
print(maximum(3,5))

minimum = lambda x,y: min(x,y)
print(minimum(4,44))

# l = [1,2,3,4,5,6,7,8,9]

# factor = lambda x: x % 3 == 0, l
# print(factor)

# Converting from lower case to upper case
str_input = "Python Programming"

upper_case = tuple(map(lambda x: x.upper(), str_input))

print(f"This is the upper case result {upper_case}")

# Max value from the list
ll = [1,2,3,4,5,6,7,8,9,10]

max_ele = max(map(lambda x: x, ll))
print(f"This is the maximum number from the list {max_ele}")

# Sum up all negative numbers in a list
nl = [1,2,3,4,5,-1,-2,-4,6]
sum_neg = sum(filter(lambda x: x < 0, nl))
print(sum_neg)

# count all the positive numbers in the list....
count_pos = len(list(filter(lambda x: x > 0, nl)))
print(count_pos)

# Give a set as input , o/p should consist of relatively prime numbers
ss = {2,3,6,11,13,17,66,48}
ss1 = {3,4,55,6,77,88,23,32}

# Give  set of radius, get the cumference of the circle..


# Factor of 3 in a list.....
