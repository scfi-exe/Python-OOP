# So far we've seen instance methods (using self) and class methods (using cls)
# There are also STATIC METHODS which are similar to class methods, but don't have access to [self] or [cls]
# They do not have instance attributes, but they *can* still access the class attributes using the class name


# They are jut regular functions that live inside of a class for oranizational purposes
class Superhero:
    def __init__(self, name: str, power: str):
        if not self.is_valid_power(power):
            raise ValueError(f"Invalid power: {power}")
        self.name = name  # Instance attribute
        self.power = power  # Instance attribute

    @staticmethod
    def is_valid_power(power: str) -> bool:
        valid_powers = ["Flying", "Strength", "Speed", "Intelligence"]
        for (
            valid_power
        ) in (
            valid_powers
        ):  # Iterate over each valid power and check if the power matches
            if power == valid_power:
                return True
        return False


# In the above code, we defined a class Superhero, with a static method is_valid_power()
# We call the method using the [self] parameter within the [__init__] method for validation before creating the hero
# Since the method would never be needed outside of the class, it's best to define it inside the class for organiztaional purposes

# Below is an example of how this class can be used. Notice we can also call the static method using the class name
print(Superhero.is_valid_power("Flying"))  # True
print(Superhero.is_valid_power("Mind Reading"))  # False

iron_man = Superhero("Iron Man", "Flying")  # Works
# mind_reader = Superhero("Hero", "Mind Reading")  # Raises ValueError


# CHALLENGE: Complete the CurrencyConverter class to convert between two currencies using static methods
#   1. Implement the static method to_usd that takes an amount and a currency code as an argument and converts the amount to USD
#      and returns the converted amount.
class CurrencyConverter:
    rates = {
        "EUR": 1.20,  # 1 EUR = 1.20 USD
        "JPY": 0.01,  # 1 JPY = 0.01 USD
    }  # Class attribute

    # TODO: Implement the static method `to_usd`
    @staticmethod
    def to_usd(val=int, curr=str):
        if curr.upper() == "EUR":
            val = val * 1.20
            return val
        elif curr.upper() == "JPY":
            val = val * 0.01
            return val


print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")  # 120 USD
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")  # 1 USD
