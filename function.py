# This is the program to build a function for calculating the sum for the given limit of numbers


def main():
    lmt = get_number()

    sum = 0
    for i in range(lmt):
        sum += i
    return sum

def get_number():
    while True:
        num = int(input("What's the limit of num? "))
        if num > 0:
            return num
        else:
            print("Enter a positive number !")

result = main()
print(f"Result of the addition: {result}")