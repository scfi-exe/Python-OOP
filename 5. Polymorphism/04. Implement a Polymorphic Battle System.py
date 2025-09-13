# Given the code of the [Hero] class, complete the following tasks:
#   1. Create a [Warrior] class that inherits from the [Hero] class and overrides the attack() method to return power+10 of the Hero
#   2. Create a [Mage] class that inherits from [Hero]. Set the health to 80. Override attack() to return power+20 of the Hero
#   3. Create a [show_attack()] function that takes a hero and prints the attack of the hero using the format:
#       "{hero.name} attacks with {hero.attack} damage!"


class Hero:
    def __init__(self, name: str, power: int):
        self.name = name
        self.health = 100
        self.power = power

    def attack(self) -> int:
        return self.power


# TODO: Implement the Warrior and Mage classes
class Warrior(Hero):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.health = 100

    def attack(self) -> int:
        atk = self.power + 10
        return atk


class Mage(Hero):
    def __init__(self, name: str, power: int):
        super().__init__(name, power)
        self.health = 80

    def attack(self) -> int:
        atk = self.power + 20
        return atk


# TODO: Implement the battle function


def show_attack(hero):
    print(f"{hero.name} attacks with {hero.attack()} damage!")


# Do not modify the following code
warrior = Warrior("Bob", 20)
mage = Mage("Alice", 15)

show_attack(warrior)
show_attack(mage)
