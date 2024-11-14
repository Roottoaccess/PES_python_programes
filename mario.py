# Creating Mario game

# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")


# def main():
#     print_row(4)
#     print_column(3)


# def print_column(height):

#     print("#\n" * height, end="")
    # for _ in range(height):
    #     print("#")

# creating another function for the row
# def print_row(width):
#     print("?" * width)

# Calling the main function
# main()


# creating the brick of the game >>
def main():
    print_square(3)

def print_square(size):
# for each rows in square
    for i in range(size):
    # for each bricks in square
        for j in range(size):
            # Printing bricks
            print("#", end="")
        print()
# Calling the main function

main()