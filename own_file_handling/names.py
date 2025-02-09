# Using the list comprehension for this approach
# names = [input("what's your name? ") for i in range(3)]
# for name in sorted(names):
#     print(f"Hello, {name}")

# name = input("What's your name? ")

# This is the Write in the file
# file = open("names.txt", "w") # opening the file
# file.write(name) # Writing the content of the file
# file.close() # Closing the file

# this is the append function in the python!!
# file = open("names.txt", "a") # a is use to append
# file.write(f"{name}\n")
# file.close()

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# Reading the file
# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("Hello,",line)
with open("names.txt", "r") as file:
    l = [print("Hello, ",x.rstrip()) for x in sorted(file, reverse=True)]


