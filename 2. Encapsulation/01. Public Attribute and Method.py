# In Python, PUBLIC ATTRIBUTES can be accessed and modified directly from outside of the class
# By default, ALL attributes and methods in Python are PUBLIC


class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.name = name  # public attribute
        self.power_level = power_level  # public attribute

    # Public method
    def display_power_level(self) -> None:
        print(f"{self.name} has a power level of {self.power_level}")


# When an attribute or method is public, we can:
#   Access it directly using dot-notation
#   Modify the attribute from outside of the class
#   Call the method from outside of the class

# Let's see public attributes in action:
# Creating a superhero
spider_man = SuperHero("Spider-Man", 85)

# Accessing public attributes/methods
print(spider_man.name)
spider_man.display_power_level()

# Modifying public attributes
spider_man.power_level = 90

# Public attributes are suitable when:
#   The attribute doesn't need validation
#   Direct access won't compromise the object's integrity
#   You want to keep the code simple and straightforward


# CHALLENGE: Your tasks are:
#   Add public attributes for name and price
#   Access the attributes of the {chips} object and display them. Use this format for printing: Item: [name] - Price: $[price]
class StoreItem:
    def __init__(self, name=str, price=float):
        self.name = name
        self.price = price


chips = StoreItem("Chips", 1.99)  # Don't modify this line

# TODO: Access the attributes of the chips object and display them
print(chips.name)
print(chips.price)
