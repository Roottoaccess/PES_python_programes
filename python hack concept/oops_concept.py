# This is a oops _concepts in python programming

# class Student:
#     name = "bro code"

# s1 = Student()

# print(s1.name)

# s2 = Student()
# print(s2.name)


# Factory to create cars
# class Car:
#     color = "blue"
#     brand = "marcedies"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# Constructor in the class
class Student:
    # collage name will not change so we are defining outside the constructor....
    collage_name = "ABC collage"

    # default constructor
    def __init__(self):
        print("This is a default constructor")

    # parameterized constructor
    def __init__(self, fullname, marks):
        # self.name = every body has unique name instance attribute.....
        self.fullname = fullname
        self.marks = marks
        # it will initialize automatic
        print("creating new student in Database..")

    # creating a method
    def welcome(self):
        print("welcome student,", self.fullname)

    def get_marks(self):
        return self.marks

s1 = Student("karan", 98)
# print(f"Name: {s1.fullname} and marks: {s1.marks}")
s1.welcome()
print(s1.get_marks())


# s2 = Student("Bro code", 88)
# print(f"Name: {s2.fullname} and marks: {s2.marks}")

# print(s2.collage_name)

# attributes -> data; variables

