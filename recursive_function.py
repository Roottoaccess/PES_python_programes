# This is a recursive function in python..
# Recursion is the process of defination something in terms of itself..

# The function that calls itself is know as a recursive function..
# Write a recursive function to sum n numbers....

# get the value of n from the user
# def rec_sum(num):
#     # rec_sum(num) = 0 + rec_sum(num - 1)

#     if num == 1:
#         return 1
#     return num + rec_sum(num - 1)

# num = int(input("What's num? "))
# res = rec_sum(num)

# print(f"The sum of {num} numbers is {res}")

# num = 5
# print(f"Result {num}")

# Stack oveflow issue....

# Factorial number in resursion 
# def rec_fact(num):
#     if num < 0:
#         return -1
#     elif num == 0:
#         return 1
#     return num * rec_fact(num - 1)

# num = int(input("What's num? "))

# result = rec_fact(num)

# print(f"The factorial for {num} is {result}")

# Gcd number checking in python
# GCD number checking in Python
# def rec_gcd(x, y):
#     if y == 0:
#         return x
#     else:
#         return rec_gcd(y, x % y)

# # Testing the function
# checking = rec_gcd(45, 3)

# print(f"The GCD is {checking}")

"""
    Experincial Learning..
    1. Using recursion find the fibonacci sum ?
    2. using recursion do fibonacci series
    3. using resursion do x^y
    4. using recursion do 1^2 + 2^2 + ......x^2
    4. using recursion do 1^3 + 2^3 + ......x^3
"""
# first program....

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# def fibonacci_sum(n):
#     if n <= 0:
#         return 0
#     return fibonacci(n) + fibonacci_sum(n - 1)

# n = int(input("What's n? "))

# result = fibonacci_sum(n)

# print(f"The sum of first {n} result is {result}")


# second program....
# def fibonnaci(n):
#     if n <= 1:
#         return n
#     return fibonnaci(n - 1) + fibonnaci(n - 2)

# def print_fibonacci_series(n , current = 0):
#     if current < n:
#         print(fibonnaci(current), end=" ")
#         print_fibonacci_series(n, current + 1)

# n = int(input("What's n? "))
# print(f"First {n} terms of the Fibonacci series are: ")
# print_fibonacci_series(n)

# third program..
# #import math
# def rec_power(x, y):
#     if y == 0:
#         return 1
#     # else:
#     #     return pow(x, y)
#     return x * rec_power(x, y - 1)

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# res = rec_power(x, y)

# print(f"{y} power of {x} is {res}")

# Fourth program
# def sum_of_square(n):
#     if n == 0 or n < 0:
#         return 0
#     return n**2 + sum_of_square(n - 1)

# n = int(input("What's n? "))
# res = sum_of_square(n)

# print(f"The result of square from 1 to {n} is {res}")

# Fifth program
def sum_of_cube(n):
    if n == 0 or n < 0:
        return 0
    return n**3 + sum_of_cube(n - 1)

n = int(input("What's n? "))
res = sum_of_cube(n)

print(f"The result of square from 1 to {n} is {res}")