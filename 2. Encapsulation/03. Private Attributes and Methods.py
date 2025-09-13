# PRIVATE attributes and methods are class members that should not be accessed from outside the class.
# The are denoted by prefixing the attribute/method name with DOUBLE underscores (__)
# UNLIKE Protected Attributes/Methods, PRIVATE Attributes/Methods are NOT accessible from Child Classes.
#   We will learn more about Child Classes in the Inheritance chapter.


class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.__name = name  # private attribute
        self.__power_level = power_level  # private attribute

    # private method
    def __secret_power(self) -> str:
        return f"Using {self.__name}'s secret power!"

    # public method to access private method
    def use_power(self) -> str:
        return self.__secret_power()

    # public method to access private attribute
    def get_power_level(self) -> int:
        return self.__power_level


# In the above code, the __name and __power_level attributes are private, meaning they cannot be accessed directly from outside the class.
# The same goes for the __secret_power() method
# We can, however, access them using PUBLIC methods get_power_level() and use_power()

# When an attribute/method is PRIVATE:
#   It should not be accessed using normal dot notation from outside of the class
#   It's meant to only be used within the class itself
#   It provides the strongst form of information in Python


# CHALLENGE: You are given the code for the PasswordManager class. Your task is to:
#   1. Add a private attribute for storing the password, which should be a string initialized in the constructor.
#   2. Implement a public method verify_password that takes an input password and returns True if it matches the stored password
#      Otherwise, return False.


class PasswordManager:
    def __init__(self, __pw=str):
        self.__pw = __pw

    # TODO: Implement the verify_password method
    def verify_password(self, inputpw):
        if inputpw == self.__pw:
            return True
        else:
            return False


# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))  # Should print: False
