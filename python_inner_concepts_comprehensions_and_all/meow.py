# Hardcotting 3
# MEOW = 3

# You can also do this
# MEOW = 4
# for i in range(MEOW): # 3 is hardcoted here
#     print("meow")


# print("This is the class method !")
# Using the class we are doing this
# class Cat:
#     MEOW = 8

#     def meow(self):
#         for _ in range(cat.MEOW):
#             print("meow")


# cat = Cat(); cat.meow()

def meow(x: int) -> str: # : int (this is a type hint)
    # for _ in range(x):
    #     print("meow")

    """:param n: Number of times to meow
        :type n: int
        :raise typeerror: If n is not an int
        :return: A string of n meows, one per line
        :rtype: str
    """

    return "meow\n" * x


number: int = int(input("Number: "))
meows: str = (meow(number))
print(meows, end="")

