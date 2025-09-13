# Remember our SuperHero class? We used a private attribute __power_level and accessed it through a method:
class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.__name = name  # private attribute
        self.__power_level = power_level  # private attribute

    # method to get power_level
    def get_power_level(self) -> int:
        return self.__power_level

    # The method get_power_level() is what we call a GETTER - it's a method that returns (GETS) the value of a private/protected attribute
    # Similarly, a SETTER is a method that SETS (changes) the value of a private or protected attribute.

    # Let's add a SETTER method to our SuperHero class with validation:

    def set_power_level(self, new_level: int) -> None:  # method to set power_level
        if 0 <= new_level <= 100:  # validation
            self.__power_level = new_level
        else:
            print("Power level must be between 0 and 100!")

    # The above method not only sets the value of a private attribute, it also validates the value
    # We specifically check if the value is in a range of 0 to 100 in the if statemetn. If the value is not in range, there is an error.
    # This ensures we never set an invalid value for the power level.
    # This is another reason we prefer using methods to access and modify private attributes.


# CHALLENGE: You're given a BankAccount class. Your goal is to:
#   1. Add a private attribute, __balance, which is initialized in the constructor. It should store an integer value.
#   2. Add a getter method for balance named get_balance() -> int that returns the balance
#   3. Add a setter method for balance named set_balance(new_balance: int) -> None that sets the value of the balance
#      ONLY IF the value passed is non-negative.
#      If the balance is negative, print "Cannot set negative balance!" and do NOT update the balance.


class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance  # Add private balance

    # TODO: Add getter method for balance
    def get_balance(self) -> int:
        return self.__balance

    # TODO: Add setter method for balance
    def set_balance(self, new_balance: int) -> None:
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Cannot set negative balance!")


# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
