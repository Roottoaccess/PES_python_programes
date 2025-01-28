# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")

def total(galleons, sickles, knuts): # function signature !
    return(galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(coins[0], coins[1], coins[2]), "knuts")

# Using the unpacking technique !
# print(total(*coins), "Knuts")

# {*coins} will do the unpacking

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

print(total(**coins), "Knuts") # this ** for dictionary unpacking