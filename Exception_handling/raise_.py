# This is the {raise} understanding !
# Raising custom error
def age_():

    try:
        age = int(input("How old are you?: "))
        if age < 0 or age > 150:
            raise ValueError("age should be between 1 to 150")
        return f"You are {age} years old !"
        
    except ValueError:
        return "Enter integer number"

print(age_())