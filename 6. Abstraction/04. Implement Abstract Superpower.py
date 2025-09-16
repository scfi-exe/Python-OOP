# Given the code below, implement the [Superpower] abstract class. The class should have:
#   1. A constructor that accepts two parameters, [name] and [power_level]
#   2. An [is_active] instance variable that is initialized to False
#   3. A concrete get_power_level() method that returns the power_level as an integer
#   4. An abstract activate() method
#   5. An abstract deactivate() method

from abc import ABC, abstractmethod


# TODO: Implement Superpower class
class Superpower:
    def __init__(self, name: str, power_level: int):
        self.name = name
        self.power_level = power_level

    is_active = False  # if this doesn't work, maybe move it into the __init__ method

    def get_power_level(self) -> int:
        return self.power_level

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass


# Don't modify the following code
class LaserBeam(Superpower):
    def activate(self) -> None:
        self.is_active = True
        print(f"{self.name} activated!")

    def deactivate(self) -> None:
        self.is_active = False
        print(f"{self.name} deactivated!")


class SuperStrength(Superpower):
    def activate(self) -> None:
        self.is_active = True
        print(f"{self.name} activated!")

    def deactivate(self) -> None:
        self.is_active = False
        print(f"{self.name} deactivated!")


laser_beam = LaserBeam("Laser Beam", 10)
super_strength = SuperStrength("Super Strength", 8)

print(laser_beam.get_power_level())
print(super_strength.get_power_level())

laser_beam.activate()
super_strength.activate()

laser_beam.deactivate()
super_strength.deactivate()
