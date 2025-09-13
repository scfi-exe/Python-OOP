# POLYMORPHISM means "Many Forms" in Greek
# It lets objects behave differently while sharing a common interface
# An analogy would be different phones sharing the same charger,
# or the len() function working in different ways on different objects.


class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> None:
        print("Animal is making a sound")


# TODO: Create the Dog and Cat classes with make_sound method
class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self) -> None:
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self) -> None:
        print(f"{self.name} says: Meow!")


# TODO: Create a common interface that takes any object of type Animal (or its subclasses) and calls their make_sound method
def animal_sound(animal: Animal) -> None:
    animal.make_sound()


# Do not change the code below
animal = Animal("Rabbit")
animal.make_sound()

animal = Dog("Buddy")
animal.make_sound()

animal = Cat("Whiskers")
animal.make_sound()
