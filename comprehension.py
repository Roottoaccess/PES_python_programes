"""This is a comprehension in python programming"""

# List comprehension..generating a list.

# creating a list without using the list function....
# simple list comprehension
l1 = ['hello' for _ in range(5)]

print(l1)

"""[<expr] for [variable] in [iterable]"""

l2 = [ x * x for x in range(5)]
print(l2, type(l2)) 

# given a list of string use list comprehension to create another list which has the length of the 4 string..

ls = ['python', 'is', 'a', 'programming', 'language']

# This is the logic 
lls = [len(_) for _ in ls]

print(lls)

llc = (x.upper() for x in (ls))
for items in llc:
    print(items)

"""new_list = [expression for variable in iterable if condition == True]"""
# Conditional statement
numbers = [1,2,3,4,5,6,7,8,9,10]
square_of_evens = [x**2 for x in numbers if x % 2 == 0]
print(square_of_evens)

ext_ll = [x.upper() for x in ls if len(x) % 2 == 0]
print(ext_ll)

l = [1,3,2,5,4]

l1 = ["Even" if x % 2 == 0 else "Odd" for x in l]
print(l1)

# Given a list of numbers create a new list of odd numbers divisible by 5
# Given a list of srings, create a list of vowel in the string
# consonant
# given a list of strings, generate a new list of all strings having 5 and more characters..
# given a string , create a list with all vowels in upper case and all the conconant in lower case..
# first question
llo =  [x for x in l if x % 2 != 0 and x % 5 == 0]
print(llo)

# second question
lss = ['hello', 'world']
# x1 = [x for x in lss if any(vowel in x for vowel in 'aeiou')]
# llss = [x1.append(x) for x in lss if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' ]

vowel = [char for word in lss for char in word if char in 'aeiou']
print(vowel)

# Third question
cons = [char for word in lss for char in word if char not in 'aeiou']
print(cons)

# fourth question
char = ['this', 'is', 'a', 'demo', 'string']
new_char = [x for x in char if len(x) >= 5]
print(new_char)

# fifth question
