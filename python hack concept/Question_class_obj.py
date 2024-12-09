# Create student class that takes name & marks of 3 subjects as arguiments in constructor Then create a method to print the average

class student:
    def __init__(self, name, physics, chemistry, computer):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.computer = computer

    def average(self, physics, chemistry, computer):
        avge = (physics + chemistry + computer) / 3
        return avge

s1 = student("job", 98, 88, 92)
print(f"Name: {s1.name} with the average {s1.average(98, 88, 92)}")
