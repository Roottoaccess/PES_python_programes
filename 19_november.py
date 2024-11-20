# def unpack_values():
#     a, b, c = packed_tuples
#     print("Unpacked values")

# study about pack and unpack

def pack_values(*args):
    print("packed values:",type(args))

# Packing values
pack_values(1,2,3,4,5)

# a,b = [10,20,30] # Too many values to unpack....
a,b = [12,34,44,66], [66,44]; print(a,b)

# This is the packing and unpacking value error.....