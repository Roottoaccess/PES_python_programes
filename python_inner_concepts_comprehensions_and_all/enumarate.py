l = ["harry", "hermione", "ron"]

# for _ in range(len(l)): # This is the way we can do
#     print(_ + 1 , l[_])

for i , l in enumerate(l):
    print(i + 1, l)