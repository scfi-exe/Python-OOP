# You are given a Knight class which implements the Attacker, Defender, and Healer interfaces
# The interfaces are not yet defined. Your task is to:
#   1. Implement the Attacker interface with the abstract method attack()
#   2. Implement the Defender interface with the abstract method defend()
#   3. Implement the Healer interface with the abstract method heal()

from abc import ABC, abstractmethod


# TODO: Create the Attacker, Defender, and Healer interfaces
class Attacker:
    def __init__(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class Defender:
    def __init__(self):
        pass

    @abstractmethod
    def defend(self):
        pass


class Healer:
    def __init__(self):
        pass

    @abstractmethod
    def heal(self):
        pass


# Don't modify the following code
class Knight(Attacker, Defender, Healer):
    def __init__(self, name: str) -> None:
        self.name = name

    def attack(self) -> None:
        print(f"{self.name} attacks with sword!")

    def defend(self) -> None:
        print(f"{self.name} raises shield!")

    def heal(self) -> None:
        print(f"{self.name} uses healing potion!")


hero = Knight("Sir Galahad")
hero.attack()
hero.defend()
hero.heal()


# UAT/Expected Output:
# Sir Galahad attacks with sword!
# Sir Galahad raises shield!
# Sir Galahad uses healing potion!
