# Working with the libraries
# from random import choice

# coin = choice(["heads", "tails"])

# print(coin)

# import random

# number = random.randint(1, 10)
# print(number)

# cards = ["jack", "queen", "king"]
# random.shuffle(cards)

# for card in cards:
#     print(card)

# import statistics

# print(statistics.mean([100, 90]))

import sys
# try:
#     print("hello, my name is",sys.argv[1])
# except IndexError:
#     print("name is missing??")

# we can handle the exception in if else statement also
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is ",sys.argv[1])
