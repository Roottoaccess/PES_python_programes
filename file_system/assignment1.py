# This is the program where we are solving the questions
with open("assignment.txt", "w") as file:
    file.write("This is the file for solving all the problems in the assignment of file I/O")
count = 0
# with open("assignment.txt", "r") as file:
#     data = file.read()
#     for i in data.split():
#         count += 1
# print(f"Total numbers of words -> {count}")

with open("assignment.txt") as file:
    count = 0
    while True:
        data = file.readline()
        if not data:
            break
        count += 1
print("number of lines we have in the file -> ",count)

with open("assignment.txt") as file:
    data = file.read()
    count = 0
    for i in data:
        if i != " ":
            count += 1
        else:
            pass
print(f"Count of all the character present in the file is -> {count}")

with open("assignment.txt") as file:
    d ={}
    data = file.read()
    for i in data:
        if i in d:
            d += 1
print(d)