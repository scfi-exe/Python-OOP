# The __init__ method we've been using is a special method in Python classes, also known as a CONSTRUCTOR
# It's job is to initialize the attributes of a new object when it gets created.

# The __init__ method in Python is technically not a Constructor, but it is often referred to as one.
# The __new__ method is the actual Constructor in Python


class SuperHero:
    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power


# The __init__ method is automatically called when we create a new object from our class. It sets up the initial state of the object.
# In the above code, __init__ is responsible for setting the Name and Power of the SuperHero we create.


# Challenge: The below code is (was) missing it's __init__ function, therefore nothing happens when the strings at the bottom are called.
# Build the __init__ function to utilize the print statements at the bottom.
class Pet:
    # TODO: Implement the __init__ method here
    def __init__(self, name=str, species=str, age=int):
        self.name = name
        self.species = species
        self.age = age


# Don't modify the code below this line
fluffy = Pet("Fluffy", "cat", 3)
buddy = Pet("Buddy", "dog", 2)

print(f"{fluffy.name} is a {fluffy.age} year old {fluffy.species}.")
print(f"{buddy.name} is a {buddy.age} year old {buddy.species}.")
