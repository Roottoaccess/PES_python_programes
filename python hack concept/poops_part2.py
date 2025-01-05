# Multilevel inheritance
# Multiple inheritance
# class a:
#     @staticmethod
#     def alert():
#         print(f"This is the first warning !")

# class b:
#     @staticmethod
#     def alert2():
#         print(f"This is the second warning !")

# class c(a, b):
#     @staticmethod
#     def alert3():
#         print(f"This is the third warning !")

# # Creating the object of only the class c
# obj = c()
# obj.alert()
# obj.alert2()
# obj.alert3()

# Using of super keyword in inheritance
class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started !")
    @staticmethod
    def stop():
        print("Car stoped !")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name

obj = ToyotaCar("Priest", "electric")
print(obj.type)