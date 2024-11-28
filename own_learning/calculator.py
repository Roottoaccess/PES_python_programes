# Calculating the square of the number

def main():
    x = int(input("What's x? "))
    print(f"Square of the number {x} is {square(x)}")

def square(n):
    return n + n

# Using this technique for importing our program to another program..
if __name__ == "__main__":
    main()