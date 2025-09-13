# DUCK TYPING is a Polymorphism concept where the type of an object is determined by its behavior, rather than explicit declaration
# In other words, if an object has the methods or attributes that are required by a function or method, it can be used in that context
# regardless of its actual class or type
# NOTE: The name Duck Typing comes from the phrase "if it walks like a duck and quacks like a duck, then it's a duck!"

# WHY USE DUCK TYPING?
#   1. Flexibility
#   2. Less Code
#   3. Loose Coupling - SpiderMan doesn't need to know BlackWidow exists, and neither need the parent class. Just the BattleSequence method


# CHALLENGE - You are given the SpiderMan class below
#   1. Create a BlackWidow class with:
#       a. An attack() method that returns "Widow's Bite!"
#       b. A defend() method that returns "Acrobatic Dodge!"


class SpiderMan:
    def attack(self) -> str:
        return "Web Shooter!"

    def defend(self) -> str:
        return "Spider Sense!"


class BlackWidow:
    def attack(self) -> str:
        return "Widow's Bite!"

    def defend(self) -> str:
        return "Acrobatic Dodge!"


#   2. Create a battle_sequence() function that:
#       a. Takes an object as a parameter
#       b. First it should call the attack() method and print the result
#       c. Then it should call the defend() method and print the result


def battle_sequence(hero):
    print(hero.attack())
    print(hero.defend())


# Don't modify the code below
spider_man = SpiderMan()
black_widow = BlackWidow()

battle_sequence(spider_man)
battle_sequence(black_widow)


# UAT/Expected Output:
# Web Shooter!
# Spider Sense!
# Widow's Bite!
# Acrobatic Dodge!
