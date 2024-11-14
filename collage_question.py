# solving and debugging the following questions from the collage.....
# Python Class - 6 November

# Question 1
s = "foo"; t = "bar"; print("barf" in 2*(s + t))

# Question 2
s = "ProgrammingwithPython" 
print(s[::5])

# Question 3
print(s[0] + s[-1])

# Question 4
print(s[::-5])

# Question 5
print(s[::1][-1] + s[len(s) - 1])

# Question 6
print('$100 $200 $300'.count("$"),
      '$100 $200 $300'.count("$",5,10),
      '$100 $200 $300'.count("$",5))

# Testing myself here....
# s = "Hello, this is a string"
# print(s[4:9:2])

# Question 7
x = ["a",["bb",["ccc","ddd"], "ee", "ff"], "g",["hh", "ii"], "j"]
print(x[1][1][0]) # It will give the result as "ccc"

print(x[4][0]) # It will give the result as "j"
print(x[1][2][0]) # It will give the result as "e"

print(x[2][0]) # Lets see the result....
print(x[3][1]) # Lets see where is it targeting.....

# Debugging some list problems and understanding them....
list1 = [1,2,3,4,5]
list2 = list1
list2[0] = 0
# Here the value is also changing in the original list because we are using asignment operator
print(list1, list2, sep="-->")
# In this case the value is not changing because we are using copy funtion
l1 = [2,44,28,88]
l2 = l1.copy()

l2[0] = 0
print(l1, l2, sep = "-->")

# Ok this is the confusing part lets decode it

y = list(range(100,110))
print(f"Address of the value 105 is {y.index(105)}")