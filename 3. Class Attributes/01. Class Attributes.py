# Certain information needs to be shared across all classes
# When assembling the Avengers to fight Thanos, Nick Fury needs to keep track of how many heroes they have
class Superhero:
    hero_count = 0  # Class attribute

    def __init__(self, name: str, power: str):
        self.name = name  # Instance attribute
        self.power = power  # Instance attribute
        Superhero.hero_count += 1


# In the above code, [hero_count] is a CLASS attribute, whereas [name] and [power] are INSTANCE attributes
# In this case, [hero_count] belongs to the entire Superhero class - not to individual heroes.
# This attribute is shared by all instances of the class.
# Unlike instance attributes, we don't use the self. keyword to access class attributes.

# Class attributes must be declared OUTSIDE of the __init__ method, and WITHOUT the self. keyword

iron_man = Superhero("Iron Man", "repulsor beams")
thor = Superhero("Thor", "lightning")

print(f"Heroes ready to face Thanos: {Superhero.hero_count}")  # This should print 2
# Notice that we accessed the class attribute using the class name, not the instance name


# CHALLENGE
# You are given the code for class SmartDevice. Modify it to track the total and active devices in your house:
#   1. Add two class attributes:
#       total_devices: tracks total number of devices created, initialized to 0
#       active_devices: tracks total number of devices currently turned on, initialized to 0
#   2. Implement these methods:
#       turn_on(): Increases active devices by 1
#       turn_off(): Decreases active devices by 1

# NOTE: total_devices increases in __init__ (already done for you)
# Methods should only update the active_devices count

# UAT, EXPECTED OUTPUT:
# Total Devices: 2
# Active Devices: 1


class SmartDevice:
    # Add your class attributes here
    total_devices = 0
    active_devices = 0

    def __init__(self, name: str):
        self.name = name
        SmartDevice.total_devices += 1  # Each new device adds to total

    # Implement these methods
    def turn_on(self) -> None:
        SmartDevice.active_devices += 1

    def turn_off(self) -> None:
        SmartDevice.active_devices -= 1


# Don't change anything below this line
tv = SmartDevice("TV")
lights = SmartDevice("Lights")

# Control devices
tv.turn_on()
lights.turn_on()
tv.turn_off()

print(f"Total Devices: {SmartDevice.total_devices}")  # Shows 2
print(f"Active Devices: {SmartDevice.active_devices}")  # Shows 1
