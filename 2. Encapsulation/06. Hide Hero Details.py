# In this challenge, you'll replace the SuperHero class to hide the hero's attributes
# The goal is to protect the hero's attributes while providing controlled access to them. Your tasks are:
#   1. In the SuperHero class __init__ method:
#       Add the private attributes [health] and [power_level]
#   2. Implement the following methods:
#       Implement the method get_health that returns the heros health
#       Implement the method get_power_level that returns the heros power level
#       Implement a method set_health that sets the hero's health if it is within range 0-100
#           If health is > 100 print "You can't set the health to more than 100"
#           If health is <0 print "You can't set the health to less than 0"
#           Otherwise, set the health
#       Implement a method set_power_level that sets the heros power level within the range 1-10 inclusive
#           If the power level is greater than 10 print "You can't set the power level to more than 10"
#           If the power level is less then 1 print "You can't set the power level to less than 1"
#           Otherwise, set the power level
#   3. Print the hero's attribute, use the following format: {hero name} has {health} health and {power level} power level.
#       Do this without accessing the private attributes directly.


# NOTE: For this challenge, do not use the @property or @setter decorators. You will pracitce them in the next challenge.


class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        # TODO: Add the private attributes
        self.__health = health
        self.__power_level = power_level

    # TODO: Add the getter and setter methods
    def get_health(self) -> int:
        return self.__health

    def get_power_level(self):
        return self.__power_level

    def set_health(self, val: int):
        if val > 100:
            print("You can't set the health to more than 100")
        elif val < 0:
            print("You can't set the health to less than 0")
        else:
            self.__health = val

    def set_power_level(self, val: int):
        if val > 10:
            print("You can't set the power level to more than 10")
        elif val < 1:
            print("You can't set the power level to less than 1")
        else:
            self.__power_level = val


super_hero = SuperHero("Batman", 80, 9)

print(super_hero.get_health())  # this should print 80
super_hero.set_health(
    110
)  # this should print You can't set the health to more than 100
super_hero.set_health(
    -10
)  # this should print You can't set the health to less than 100
super_hero.set_health(70)

print(super_hero.get_power_level())  # this should print 9
super_hero.set_power_level(
    11
)  # this should print You can't set the power level to more than 10
super_hero.set_power_level(
    0
)  # this should print You can't set the power level to less than 1
super_hero.set_power_level(7)


# TODO: print the hero's attributes
#   3. Print the hero's attribute, use the following format: {hero name} has {health} health and {power level} power level.
#       Do this without accessing the private attributes directly.

print(
    f"{super_hero.name} has {super_hero.get_health()} health and {super_hero.get_power_level()} power level"
)
