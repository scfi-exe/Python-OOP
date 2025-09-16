# an INTERFACE in Python is just like an abstract class, but with one key difference: it only contains abstract methods
# While abstract classes can mix both concrete and abstract methods, an interface is a "PURE" abstract class
# It only defines a contract of what methods muts be implemented

# INTERFACES vs ABSTRACT CLASSES
# 1. Interfaces only contain PURELY abstract methods
# 2. Abstract classes can mix both concrete and abstract methods
# 3. Abstract classes can have constructors (__init__)
#    While Python allows __init__ methods in interfaces, it's considered bad practice,
#    as interfaces should focus purely on method contracts


# CHALLENGE: CREATE A SUPERHERO INTERFACE
# You are given the code for the Superman and WonderWoman classes
# Both inherit from Superhero, which hasn't been defined yet. Your goal is to:
#   1. Create a Superhero interface
#   2. In the Superhero interface, define abstract methods [fly()] and [use_power()]


from abc import ABC, abstractmethod


# TODO: Create a Superhero interface
class Superhero:
    def __init__(self):
        pass

    @abstractmethod
    def fly(self) -> str:
        pass

    @abstractmethod
    def user_power(self) -> str:
        pass


class Superman(Superhero):
    def fly(self) -> str:
        return "Up, up and away!"

    def use_power(self) -> str:
        return "Using heat vision"


class WonderWoman(Superhero):
    def fly(self) -> str:
        return "Soaring through the clouds!"

    def use_power(self) -> str:
        return "Using lasso of truth"


# Don't modify the code below
superman = Superman()
wonder_woman = WonderWoman()

print(isinstance(superman, Superhero))  # UAT: True
print(isinstance(wonder_woman, Superhero))  # UAT: True
