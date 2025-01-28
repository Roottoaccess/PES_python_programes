# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name":"Draco", "house": "slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"}
# ]

student = ["Hermione", "Harry", "Ron"]

# gryff = []

# for i in student:
#     gryff.append({'name':i , "house": "Gryffindor"})

# gryff = [{"name": s, "house": "Gryffindor"} for s in student]

gryff = {s: "Gryffindor" for s in student}
# This is the proper dictionary !!
print(gryff)