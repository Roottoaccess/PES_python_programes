# This is the concept of nested function in Python Programming

"""Example one"""
def outer_func():
    def inner_func():
        print("Hello",end=", ")
    inner_func()
    print("python!")
outer_func()


"""Example two"""
# Giving the arguments who in the outer function
def outer_func(who):
    def inner_func():
        print(f"Hello {who}")
    # Calling the inner function
    inner_func()
# name = input("Who? ")
# Calling the outer function
# outer_func(name) # Giving the value here


"""Example three"""
def func1():
    s = "Python Programming"
    def func2():
        s = "Programming with python"
        print(s)
    func2()
    print(s)
func1()

"""Example four"""
# def outer_function():
