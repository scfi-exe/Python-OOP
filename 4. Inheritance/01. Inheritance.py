# INHERITANCE is a fundamental concept in OOP that allows you to create a new class based on an existing class
# The new class, known as a CHILD CLASS or SUBCLASS, inherits properties and methods from the existing Parent Class (a.k.a. Superclass)

# Inheritance allows us to create new classes based on existing ones.
# Instead of modifying an existing class, inheritance lets us reuse its code while only writing the differences we need in the new class.

# CHALLENGE: Let's take the parent class SmartDevice with property name. Your task is to create a child class SmartLight that inherits
# from the SmartDevice class and has a method turn_on and turn_off.


class SmartDevice:
    def __init__(self, name: str):
        self.name = name

    def turn_on(self):
        print(f"{self.name} is turned on")

    def turn_off(self):
        print(f"{self.name} is turned off")


# TODO: Implement the SmartLight class
class SmartLight(SmartDevice):
    def __init__(self, name: str):
        self.name = name


# Don't change the code below
device = SmartLight("Smart Light")
device.turn_on()
device.turn_off()
