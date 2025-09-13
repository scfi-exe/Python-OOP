# super() is a built-in function in Python that allows you to call methods from a Parent Class
# It is a powerful tool for working with inheritance

# WHY USE SUPER?
# When working with Inheritance, there are often situations where you want to extend rather than completely replace a parent class behavior
# For example:
#   1. You might want to add extra initialization steps while keeping the Parent's core initialization
#   2. You may need to enhance an existing method, while maintaining it's core functionality
#   3. You could need to access parent class properties while also adding news ones


# SYNTAX FOR SUPER() FUNCTION:
# super().parent_method() # Call parent class's instance method
# super().__init__() # Call parent class __init__ method
# super().parent_property # Access parent class property

# CHALLENGE - Given the code for the SuperHero class, complete the following tasks:
#   1. Create an Avenger class that inherits from the SuperHero class
#   2. Override the [__init__] method to add a [team] property to the Avenger class.
#      Avenger should also call the [__init__] method of the SuperHero class to initialize the [name] and [power] properties
#   3. Define the [attack()] method in the Avenger class, which should call the [attack()] method of the SuperHero class


class SuperHero:
    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power

    def attack(self) -> None:
        print(f"{self.name} is attacking with {self.power}")


# TODO: Create a Avenger class that inherits from the SuperHero class
class Avenger(SuperHero):
    # TODO: Override the __init__ method to add a team property to the Avenger class
    def __init__(self, name: str, power: str, team=str):
        super().__init__(name, power)
        self.team = team

    # TODO: Call the attack method of the SuperHero class from the Avenger class
    def attack(self):
        super().attack()


# Don't change the code below
avenger = Avenger("Iron Man", "repulsor beams", "Avengers")
print(avenger.name)
print(avenger.power)
print(avenger.team)
avenger.attack()
