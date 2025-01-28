students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name":"Draco", "house": "slytherin"}
]



# gryffindor = [x["name"] for x in students if x["house"] == "Gryffindor"]

# print(*gryffindor) # Using the Unpacking technique!

# for _ in sorted(gryffindor):
#     print(_)

gry = filter(lambda s: s["house"] == "Gryffindor", students)

for g in sorted(gry, key = lambda s: s["name"]):
    print(g["name"])