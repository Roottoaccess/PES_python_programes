# # Creating the main function for the program
# def main():
#     a = int(input().strip())
#     b = int(input().strip())

#     # Calling the function
#     value_result(a,b)
# # Defining another function for the logic

# def value_result(a,b):
#     print(a + b)
#     print(a - b)
#     print(a * b)

# # Calling the main function
# main()


# Creating the main function
# def main():
#     a = int(input().strip())
#     b = int(input().strip())

#     result_logic(a,b)

# # Ceating the result logic
# def result_logic(num , num1):
#     # This is for the integer division
#     print(num // num1)
#     # This is for the floting division
#     print(num / num1)

# # Calling the main function
# main()


# Creating the main function
# def main():
#     n = int(input().strip())

#     Logic(n)

# # creating the Logic function for displaying the output..
# def Logic(num):
#     # Run a for loop for iterating the numbers
#     for _ in range(0, num):
#         print(_*_)

# main()


# # creating the program to find the given year is a leap year or not
# def main():
#     year = int(input().strip())

#     Logic_LeapYear(year)


# def Logic_LeapYear(year):
#     if (year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)):
#         print(True)
#     else:
#         print(False)

# # Calling the main function
# main()

# Solving another problem.....

def main():
    while True:
        try:
            n = int(input("What's n? ").strip())
            concat(n)
        except ValueError:
            print("Please provide integer value....")
        else:
            break
# Creating the concat function
def concat(n):
    # Using the for loop for iterating the values....
    for _ in range(1,n+1):
        print(str(_),end = "")

# Calling the main function
main()