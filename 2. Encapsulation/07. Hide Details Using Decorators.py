# In this challenge, you'll refactor the SuperHero class using decorators
# You are given a SuperHero class. Your tasks are:
#   1. Inside the Superhero class:
#       Implementer a GETTER for health using the @property decorator that returns the heros health
#       Implement a GETTER for power_level using the @property decorator that returns the heros power level
#       Implement a health SETTER using the @setter decorator with validation (0-100 range)
#           If the health is greater than 100 print "You can't set the health to more than 100"
#           If the health is less 0 print "You can't set the health to less than 0"
#           Otherwise, set the health
#       Implement a power_level setter using the @setter decorator with validation (1-10 range)
#           If the power level is greater than 10 print "You can't set the power level to more than 10"
#           If the power level is less than 1 print "You can't set the power level to less than 1"
#           Otherwise, set the power level
#   2. Print the hero's attributes. Use the following format: {hero name} has {healt} health and {power level} power level.

# Expected output:
# 80
# You can't set the health to more than 100
# 9
# You can't set the power level to more than 10
# You can't set the power level to less than 1
# Batman has 80 health and 9 power level


class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level

    # TODO: Add the getter and setter methods
    @property
    def health(self):
        return self.__health

    @property
    def power_level(self):
        return self.__power_level

    @health.setter
    def health(self, val):
        if val > 100:
            print("You can't set the health to more than 100")
        elif val < 0:
            print("You can't set the health to less than 0")
        else:
            self.__health = val

    @power_level.setter
    def power_level(self, val):
        if val > 10:
            print("You can't set the power level to more than 10")
        elif val < 1:
            print("You can't set the power level to less than 1")
        else:
            self.__power_level = val

    # Remember to use the @property decorator for the getter methods
    # Remember to use the @setter decorator for the setter methods


# Don't change the following code
super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health)  # this should print 80
super_hero.health = 110  # this should print You can't set the health to more than 100

print(super_hero.power_level)  # this should print 9
super_hero.power_level = (
    100  # this should print You can't set the power level to more than 10
)
super_hero.power_level = (
    0  # this should print You can't set the power level to less than 1
)


# TODO: print the hero's attributes
print(
    f"{super_hero.name} has {super_hero.health} health and {super_hero.power_level} power level"
)
