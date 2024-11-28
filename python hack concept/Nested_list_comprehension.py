"""This is a nested list compreension"""

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# flattened = [num for row in matrix for num in row]
# print(flattened)

# even_num = [num for row in matrix for num in row if num%2 == 0]
# print(even_num)

# setences = "The cat in the hat had two sidekicks, things one and thing two."
# words = setences.lower().replace().replace().split()
# {word for word in words if len(word) <= 3}
# print(result)

"""new_set = {expression for variable in iterable if condition == True}"""

"""Why we dont have the concept of tupple comprehension ?"""


"""Dictionary comprehension"""

# {key_expresion: value_expression for item in iterable if condition}

# Dictionary square creation using nested _list_ comprehentions
# square = {x: x**2 for x in range(1,6)}
# print(square)

# uodate = {x:x**2 for x in range(1,11) if x % 2 == 0}
# print(uodate)

# for nested distionary this is the syntax..
"""{outer_key:
        {inner_key: inner_value for inner_key, inner_value in inner_iterable}
            for outer_key, outer_value in outer_iterable}"""

# disct = {'name': "Biswarup", 'age': 22}
# print(disct.items())

# Nested conditional Dictioanry comprehension
# print(1 * 1 % 2 == 0)

# Questions 1....
# limit = int(input("What's the limit? "))
# ul = []

# for _ in range(0, limit):
#     ins_val = int(input("Enter the value: "))

#     ul.append(ins_val)

# print(ul)

# positive number from the list
# pos_list = [x for x in ul if x > 0]
# print(pos_list)

# # negative number from the list
# neg_list = [x for x in ul if x < 0]
# print(neg_list)

# # factors of 5 from the list
# fact_of_five = [x for x in ul if x > 0 if x % 5 == 0]
# print(fact_of_five)

# Question 2......
row = int(input("What's row? "))
col = int(input("What's col? "))

# lis_row = [x for x in row]
# lis_col = [y for y in col]
gen_dict = {row: row * col}

print(gen_dict)

# Question 3
# from collections import Counter
str_giv = "This is question number three"
freq = str_giv.lower().replace(',','').replace('.','').strip()
frequency = {char: str_giv.count(char) for char in freq}
print(frequency)

# Question 4....


# Question 5....
lmt1 = int(input("What's lmt"))
list2 = [lmt1]

upl = []

for i in range(0, lmt1):
    inp_val = int(input("Enter -> "))

    
