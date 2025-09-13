# METHODs are FUNCTIONS that belong to a CLASS or OBJECT
# They define the behavior of the class or object.


# DEFINING METHODS IN CLASS
# Let's update our SuperHero class to include two methods, use_power() and take_damage(amount)
class SuperHero:
    def __init__(self, name, power, health, speed):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}.")


# We can now create an object of the SuperHero class and call these methods on the object
iron_man = SuperHero("Iron Man", "super strength", 100, 90)

iron_man.use_power()  # Output: Iron Man uses super strength!
iron_man.take_damage(20)  # Output: Iron Man takes 20 damage. Health is now 80.


# CHALLENGE


class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        self.hunger -= 1
        print(f"{self.name} has been fed.")
        print(f"{self.name}'s hunger level: {self.hunger}")
        pass


# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
my_pet.feed()
my_pet.feed()
my_pet.feed()
