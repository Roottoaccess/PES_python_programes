class Student: # Instance variable to object
    def __init__(self, name, house): # Constructor
        self.name  = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

# def get_student(): # This is the get_student function !!
#     student = Student() # Object
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()