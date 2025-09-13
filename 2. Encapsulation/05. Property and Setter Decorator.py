# Python provides a more IDIOMATIC way to use Getters and Setters using the @property and @setter decorators
class Hero:
    def __init__(self, name: str):
        self.__name = name  # private attribute

    # Getter
    @property
    def name(self) -> str:
        return self.__name

    # Setter
    @name.setter
    def name(self, new_name: str) -> None:
        if new_name != "":
            self.__name = new_name
        else:
            print("Name cannot be empty!")


# In the above code, we have defined two methods as attribute name
# But in effect, these are two different methods
# We use @property to define a GETTER method, and @name.setter to define a SETTER method
# We also added validation logic to prevent setitng the name to an empty string

hero = Hero("Batman")

# Getting name
print(hero.name)  # this calls the getter method not the attribute
# Setting name
hero.name = "Superman"  # this calls the setter method not the attribute
hero.name = ""  # Error: Name cannot be empty!

# In the above code, we created an instance of the Hero class and accessed and modified the name attribute
# Internally, ACCESSING the name attribute calls the getter method, and MODIFYING the name attribute calls the SETTER method
# Notice that the field is __name, but the method names for getter and setter are still name

# WHY USE @PROPERTY AND @SETTER?
#   1. Makes code look cleaner
#   2. Feels more natural (like using attributes)
#   3. Still gives us control (validation, etc.)


class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance  # Don't modify this line

    @property
    def balance(
        self,
    ) -> int:  # TODO: Convert this method to use the @property decorator
        return self.__balance

    @balance.setter
    def balance(
        self, value: int
    ) -> None:  # TODO: Convert this method to use the @property decorator
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative!")


# Don't modify the code below this line
account = BankAccount(1000)
print(account.balance)
account.balance = -100
