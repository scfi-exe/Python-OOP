# MULTIPLE INHERITANCE is a feature in OOP where a class can inherit attributes and methods from multiple classes
# While powerful, it is generally considered an ANTI-PATTERN [https://stackoverflow.com/questions/406081/why-should-i-avoid-multiple-inheritance]
# Let's see an example:
class Swimmer:
    def swim(self):
        print("Swimming")


class Flyer:
    def fly(self):
        print("Flying")


# Ducks inherits from both Swimmer and Flyer
class Duck(Swimmer, Flyer):
    pass


# Below, we create an instance of the Duck class and call the swim() and fly() methods
duck = Duck()
duck.swim()  # Should print "Swimming"
duck.fly()  # Should print "Flying"

# In most cases, you should NOT use multiple inheritance. BUT, you may see some code like this in the wild.

# Basic Syntax:
# class ChildClass(ParentClass1, ParentClass2, ...):
#   Class body


# CHALLENGE: Create a SmartWatch that inherits from both ElectronicDevice and HealthDevice
# Use the [pass] keyword to indicate that we are not adding any new methods or attributes to the SmartWatch class

# UAT/Expected Output:
# Device is turning on
# Measuring heart rate
# Device is turning off


class ElectronicDevice:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def turn_on(self) -> None:
        print("Device is turning on")

    def turn_off(self) -> None:
        print("Device is turning off")


class HealthDevice:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    def measure_heart_rate(self) -> None:
        print("Measuring heart rate")


# TODO: Create a SmartWatch class that inherits from both ElectronicDevice and HealthDevice
class SmartWatch(ElectronicDevice, HealthDevice):
    pass


# Do not modify the code below
smart_watch = SmartWatch("Apple", "Watch Series 6")
smart_watch.turn_on()
smart_watch.measure_heart_rate()
smart_watch.turn_off()
