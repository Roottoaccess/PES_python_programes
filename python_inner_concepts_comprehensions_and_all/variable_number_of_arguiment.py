def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)


f(galleons = 100,sickles =  25,knuts = 55)

# **kwargs convert this to dictionary !!