# So far, we've seen the general concept of abstraction. Now. let's explore 2 key concepts used to achieve abstraction in Python:
#   1. An ABSTRACT METHOD is a method that is declared in a base class, but contains no implementation/functionality.
#      The child class must implement the abstract method. Abstract methods are used to enforce a contract on Subclasses.
#      Subclasses must implement the abstract method, otherwise they will raise an error.
#   2. An ABSTRACT CLASS is a class that contains one or more abstract methods.
#      It serves as a blueprint for other classes and cannot be instantiated on its own.

# Let's look at an example
from abc import ABC, abstractmethod


class Superhero(ABC):
    def __init__(self, name):
        self._name = name

    def get_name(self) -> str:  # public methods
        return self._name

    @abstractmethod
    def fly(self) -> str:
        pass


class Superman(Superhero):
    def fly(self) -> str:
        return "Up up and away!"


# In the above example:
#   1. Superhero is the base abstract class that inherits from ABC. In Python, abstract classes are created by inheriting from ABC.
#   2. The @abstractmethod decorator marks fly() as an abstract method.
#      In Python, abstract methods are created by decorating a method with the @abstractmethod decorator.
#   3. Superman, and any other child class that inherits from Superhero, must implement the fly() method
#   4. Non-abstract methods like get_name() are optional to override.

# NOTE: You cannot create an instance of Superhero class because it is an abstract class and has an abstract method.
#       Instead, you can only create child classes of Superhero.


# WHY USE ABSTRACT METHOD?
#   Abstract Methods are a powerful tool for achieving abstraction because they:
#       1. Hide Implementation Details (Abstraction): The base class only declares what methods must exist,
#          without specifying how they work.
#       2. Enforce Consistency: Child classes must implement these methods, ensuring a standard interface across all
#          subclasses, which allows for Polymorphism
#       3. Prevent Incomplete Objects: You can't create instances of classes with abstract methods,
#          ensuring only fully-implemented classes can be used.


# CHALLENGE: You'll implement a payment card system using abstract classes.
# You are given a class PaymentCard. Your tasks are to:
#   1. Make the PaymentCard class abstract
#   2. Add an abstract method, process_payment(amt: int) -> str: which takes a float [amt] as an argument and returns a string
#   3. Implement a DebitCard class that:
#       a. Inherits from a PaymentCard
#       b. Implements the process_payment(amt: int) -> str: method
#          It should take the [amt] as an argument and subtract it from the balance.
#          If the balance is less than the amount, it should return "Insufficient funds"
#          Otherwise, it should return "Payment successful" and update the balance
