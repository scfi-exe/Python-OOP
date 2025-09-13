# An OBJECT is an instance of a class
# It is a specific item created using a the blueprint defined by the class


# CREATING OBJECTS
# We have seen the class definition for SuperHero before
class SuperHero:
    def __init__(self, name: str, power: str, health: int, speed: int):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed


# We can CREATE an object by calling the class and passing the required arguments
# Creating superhero objects
iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)
spider_man = SuperHero("Spider Man", "web slinging", 90, 95)
