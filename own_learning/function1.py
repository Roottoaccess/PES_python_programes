"""Solving the beginner-level Questions"""
# def sum(a , b):
#     return a + b

# def main():
#     x = int(input("What's x? "))
#     y = int(input("What's y? "))

#     print(f"The result for adding the elements {sum(x,y)}")

# # Calling the main function
# if __name__ == "__main__":
#     main()

"""Factorial of a given number"""
# def factorial(n):
#     fact = 1
#     for _ in range(1, n + 1):
#         fact *= _
#     return fact

# # creating the main function
# def main():
#     x = int(input("What's x? "))
#     print(f"The factorial result: {factorial(x)}")

# # Calling the main funcion
# if __name__ == "__main__":
#     main()

"""Even Odd"""
# def even_odd_check(num):
#     if num % 2 == 0: print(f"{num} is Even")
#     else: print(f"{num} is Odd")
#     return num

# def main():
#     n = int(input("What's n? "))
#     even_odd_check(n)

# if __name__ == "__main__":
#     main()

"""Reverse a String"""

# def rev_string(value):
#     return reversed(value)

# def main():
#     st = input("What's your string? ")
#     # print(f"{rev_string(st)}")
#     for i in rev_string(st):
#         print(i,end=" ")

# if __name__ == "__main__":
#     main()

"""Demo function"""

def recur(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * recur(num - 1)

def main():
    num = int(input("What's num? "))
    print(f"The result of recursion {recur(num)}")

# Calling the main function
if __name__ == "__main__":
    main()