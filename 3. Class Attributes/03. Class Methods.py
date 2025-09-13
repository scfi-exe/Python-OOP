# So far, we have only looked at instance methods
# Sometimes, we need methods that work for/on the entire class, rather than on individual instances/objects
# For example, we want to upgrade the training level of all of the heroes at once. Let's see how we can do that using Class Methods
class Superhero:
    training_level = 1  # Class attribute

    def __init__(self, name: str, power: str):
        self.name = name  # Instance attribute
        self.power = power  # Instance attribute

    @classmethod
    def upgrade_training(cls) -> None:
        cls.training_level += 1
        print(f"All heroes now at training level {cls.training_level}")


# In the above Superhero class, the upgrade_training(cls) method is a class method
#   It uses the @classmethod decorator to define the class method
#   It uses cls as the first parameter, instead of self
#   It upgrades the training_level (a class attribute) by 1
#   cls is used to access the class attribute, instead of the class name Superhero

# The below code shows the recommended way to call the class method:
Superhero.upgrade_training()  # Recommend way to use class method
print(Superhero.training_level)  # 2

# The below code shows how the class method may be called using an instance of the class, which is NOT recommended
iron_man = Superhero("Iron Man", "Flying")
iron_man.upgrade_training()  # Works but not recommended
print(iron_man.training_level)  # 3


# NOTE: Class Methods are similar to Class Attributes. They are shared by all instances of the class.
# This also means that they do NOT have access to instance attrbutes, which is why we don't use [self] in class methods.
# Class Methods can be defined with additional parameters, after the (cls) parameter


# CHALLENGE: Given the code for the Libary class, implement the following two class methods to manage book lending:
#   lend_books: takes [number] as an argument and subtracts it from books_available
#   return_books: takes [number] as an argument and adds it to books_available


# UAT/Expected Output:
# Initial status: 100 books available
# After lending: 70 books available
# After return: 80 books available


class Library:
    books_available = 100  # Total books in library

    # TODO: Implement class methods to manage book lending
    @classmethod
    def lend_books(cls, value: int):
        Library.books_available -= value

    # TODO: Implement return_books method to increase the number of books available
    @classmethod
    def return_books(cls, value: int):
        Library.books_available += value


# Don't change the code below
print(f"Initial status: {Library.books_available} books available")
Library.lend_books(30)
print(f"After lending: {Library.books_available} books available")
Library.return_books(10)
print(f"After return: {Library.books_available} books available")
