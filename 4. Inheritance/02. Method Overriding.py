# METHOD OVERRIDING allows us to change the behavior of a method in a child class
# This is useful when we want to change the behavior of a method that is inherited from the parent class
# I.e., the parent class, "Character", might move 10 spaces, but the child class, "Rogue", might move 12 spaces

# CHALLENGE: You are given code for the Animal class. Your tasks are:
#   1. Create a Dog class and a Cat class that inherit from the Animal class
#   2. Override the make_sound method in the Dog class to make the dog bark.
#   3. Override the make_sound method in the Cat class to make the cat meow.

# Expected output/UAT:
# Animal makes a sound
# Max is barking
# Luna is meowing


class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> None:
        print("Animal makes a sound")


# TODO: Create a Dog class and a Cat class that inherit from the `Animal` class.
class Dog(Animal):
    def __init__(self, name=str):
        self.name = name

    # TODO: Override the `make_sound` method in the `Dog` class to make the dog bark.
    def make_sound(self) -> None:
        print(f"{self.name} is barking")


class Cat(Animal):
    # TODO: Override the `make_sound` method in the `Cat` class to make the cat meow.
    def __init__(self, name=str):
        self.name = name

    def make_sound(self) -> None:
        print(f"{self.name} is meowing")


# Do not modify the code below
animal = Animal("Cow")
animal.make_sound()  # Output: Animal makes a sound
dog = Dog("Max")
dog.make_sound()  # Output: Max is barking
cat = Cat("Luna")
cat.make_sound()  # Output: Luna is meowing
