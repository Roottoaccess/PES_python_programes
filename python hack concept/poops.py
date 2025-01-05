# Creating basic classes and objects
# class Car: # Created the class
#     color = "blue"

# car1 = Car()
# print(f"The color of car1 is {car1.color}")

# class Student: # Creating the student class
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding the student information in the database..")

# stud = Student("Jeet",98) # Only creating the object of the student class ->
# print(stud.name); print(stud.marks)

# stud1 = Student("Hrithik", 88) # Only creating the object of the student class ->
# print(stud1.name); print(stud1.marks)

# class Student: # Creating the student class ....
#     def __init__(self, name, maths, physics, computer):
#         self.name = name
#         self.maths = maths
#         self.physics = physics
#         self.computer = computer

#     def average(self):
#         avg = (self.maths + self.physics + self.computer) / 3

#         print(f"The average of the student {self.name} is {avg:.2f}")

# stu1 = Student("Jeet", 88, 82, 84)
# stu1.average()


class Student: # Created the Class
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def greetings():
        print("Welcome to the Student Potal !")

    def average(self):
        sum = 0
        for _ in self.marks:
            sum += _
        print(f"The marks for {self.name} is {sum / 3:.2f}")

stud = Student("Hrithik Roshan", [2, 4, 6, 8]) # Creating the Object of the Class
stud.greetings()
stud.average()