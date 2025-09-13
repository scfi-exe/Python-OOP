# ATTRIBUTES are the properties that define or belong to an object
# In our SuperHero example, we have the following attributes: name, power, health, and speed


# ACCESSING ATTRIBUTES
# To access an object's attributes, we use dot-notation: object_name.attribute_name
# Let's create a SuperHero and access it's attributes


class SuperHero:
    def __init__(self, name=str, power=str, health=int, speed=int):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed


iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)
print(iron_man.name)  # Iron Man
print(iron_man.power)  # repulsor beams


# MODIFYING ATTRIBUTES
# We can also MODIFY attributes by using the same dot notation
iron_man.health = 90  # 90
iron_man.power = "Advanced Repulsor Technology"  # Advanced Repulsor Technology


# ATTRIBUTE TYPES
# While Python won't give us any errors when changing data types of an attribute, we should avoid doing so to avoid unexpected behavior
iron_man.name = 42  # allowed but bad practice
iron_man.health = "full"  # allowed but bad practice


class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy


whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes
print(
    f"Initial Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}"
)
# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
whiskers.hunger = whiskers.hunger - 3
#  - Increase energy by 2
whiskers.energy = whiskers.energy + 2
# TODO: Print Whiskers' modified attributes
print(
    f"Modified Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}"
)
