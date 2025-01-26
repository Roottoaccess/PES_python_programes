ss = {1,2.2,2222, 102, 4, 8}

print(f"sum of all the value in the set: {sum(ss)}") # Sum all the values !!

print(f"max element from the set {max(ss)}")

even = {2,4,6,8,10}
odd = {1,3,5,7,9,11, 4, 8}

# Applying the union function

uni_set = even.union(odd)
print(uni_set)

# Applying the intersection function
ini_set = even.intersection(odd)

print(ini_set)

# Difference from the two set !!

diff_set = even - odd
print(f"Difference from the two sets is: {diff_set}")

# Symmetric didderene !!
sym_diff = even ^ odd # With out the common part !!
print(f"The symmetric difference is: {sym_diff}")

# Is subset ?
print(f"Is odd is a subset of even ? {even.issubset(odd)}")

# Operations
even.add(1000)
print(even) # Adding an element

even.discard(1000)
print(even) # Discarding an element 

even.pop()
print(even) # Poping an element