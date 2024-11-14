# This is the dictionary where we can store more informations about hogwarts

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "gryffindor","patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]


for student in students:
    print(student["name"], student["house"], sep = ", ")