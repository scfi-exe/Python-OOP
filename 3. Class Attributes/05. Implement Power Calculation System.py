# Suppose we are making a game, and need to determine the effective power level of a hero when creating it
# You are given the Hero class and the __init__ method. Your tasks are:
#   1. Add a static method, calculate_effective_power, that takes two parameters:
#       base_power: The hero's base power level (integer)
#       attributes: A dictionary containing the hero's attributes (strength, speed, intelligence)
#      The method should:
#       1. Calculate the attribute_bonus by averaging all attrbute values. Use sum(attribute.values())/len(attributes) to get the average
#       2. Calculate the effective power, using the formula: base_power * (1+attribute_bonus)
#       3. Round the final result to once decimal place
#       4. Return the effective calculated power

# UAT, Expected Output:
# Base Power: 8
# Attributes: {'strength': 7, 'speed': 6, 'intelligence': 8}
# Effective Power: 64.0

# Base Power: 6
# Attributes: {'strength': 4, 'speed': 5, 'intelligence': 6}
# Effective Power: 36.0


class Hero:
    def __init__(self, name: str, base_power: int, attributes: dict):
        self.name = name
        self.base_power = base_power
        self.attributes = attributes

    # TODO: Add calculate_effective_power static method here
    @staticmethod
    def calculate_effective_power(basePower=int, Attributes=dict):
        attribute_bonus = sum(Attributes.values()) / len(Attributes)
        effective_power = round((basePower * (1 + attribute_bonus)), 1)
        return effective_power


# Don't change the following code
base_power1 = 8
attributes1 = {"strength": 7, "speed": 6, "intelligence": 8}

power1 = Hero.calculate_effective_power(base_power1, attributes1)
print(f"Base Power: {base_power1}")
print(f"Attributes: {attributes1}")
print(f"Effective Power: {power1}\n")

base_power2 = 6
attributes2 = {"strength": 4, "speed": 5, "intelligence": 6}

power2 = Hero.calculate_effective_power(base_power2, attributes2)
print(f"Base Power: {base_power2}")
print(f"Attributes: {attributes2}")
print(f"Effective Power: {power2}")
