# In Python, protected attributes and methods are class members that should NOT be accessed from outside of the class.
# However, they can be accessed within the class and within child classes (more on child classes later)


# PROTECTED Attributes are denoted by prefixing the attrbute/method with a single underscore, _
class SuperHero:
    def __init__(self, name: str, power_level: int):
        self._name = name  # protected attribute
        self._power_level = power_level  # protected attribute

    def get_name(self) -> str:  # public method
        return self._name

    def _some_protected_method(self) -> None:  # protected method
        pass

    def some_public_method(self) -> None:
        self._some_protected_method()


# Unlike other languages, Python does not directly support protected methods. We can still access them, but it's not recommended.
# Using an underscore is a common naming convention in Python to signal other developers that this method is meant to be protected.
# If an attribute or method is prefixed with a single underscore, it isn't meant to be accessed from the outside

# Below is the recommended way to access protected attributes and methods:
spider_man = SuperHero("Spider-Man", 85)

print(spider_man._name)  # Allowed but discouraged
print(spider_man.get_name())  # Recommended

spider_man._some_protected_method()  # Allowed but discouraged
spider_man.some_public_method()  # Recommended


# CHALLENGE:
# 1. Initialize two attributes, [1] a "title" public attribute, and [2] a "_balance" protected attribute
# 2. Use a public method display_balance() to display the balance


class Account:
    def __init__(self, title=str, _balance=int):
        self.title = title
        self._balance = _balance

    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
