# ABSTRACTION is the concept of hiding complex implementation details and only showing necessary features to the outside world
# Think of it like a TV remote - you just press buttons to change channels, you don't need to know how it works inside.

# DATA ABSTRACTION
#   Hides complex data details
#   Achieved in Python through: Private Variables

# BEHAVIORAL ABSTRACTION
#   Hides complex method implementations
#   Achieved in Python through: Abstract Methods


# Here is a simple example:
class TempConverter:
    def __init__(self, celsius):
        self._celsius = celsius  # Hidden internal state

    def get_fahrenheit(self) -> float:
        return (self._celsius * 9 / 5) + 32


temp = TempConverter(25)
print(temp.get_fahrenheit())  # 77.0

# In the above code:
#   get_fahrenheit() is the public interface that *abstracts* away the internal implementation details
#   _celsius is an internal variable that's hidden from users
#   Users don't need to see or understand the conversion formula


# ABSTRACTION vs. ENCAPSULATION
# ABSTRACTION (Hiding Complexity)
#   Is about identifying essential features and hiding unnecessary details
#   Focuses on WHAT an object does at a high level
#   Like a TV remote - you just need to know it can change channels
#   In the TempConverter example we discussed, get_fahrenheit() represents an abstraction bc it converts without showing the formula
#   Purpose: Simplifying the view of complex systems

# ENCAPSULATION (Protecting Data)
#   Is about grouping data and methods that work on that data within a single unit, and restricting access to the internal data
#   Controls HOW the objects data can be accessed and modified
#   Like a medicine capsule - wraps and protects it's contents
#   In the [TempConverter] example, we encapsulate the _celsius variable by making it private and only accessing it through controlled methods
#   Purpose: Data hiding, bundling related functionality

# THE KEY DIFFERENCE:
#   Abstraction operates at a design-level ("What features to expose?")
#   Encapsulation operates at the implementation-level ("How to protect data?")

# CHALLENGE
# Given the code for Superhero class below, create an abstraction for the fly() method.
# The user should only need to know that the superhero can fly, and not how the fly method is implemented.
# Internally, the fly() method should check if the superhero has enough power to fly.
# If their power level is at least 20, it should reduce their power level by 20 and return "Up up and away!".
# If their power level is less than 20, it should return "Too tired to fly...".


class Superhero:
    def __init__(self, name: str):
        self._name = name
        self._power_level = 40

    def fly(self):
        if self._power_level >= 20:
            self._power_level -= 20
            return "Up up and away!"
        else:
            return "Too tired to fly..."


# Do not modify the code below
hero = Superhero("Superman")
print(hero.fly())
print(hero.fly())
print(hero.fly())
