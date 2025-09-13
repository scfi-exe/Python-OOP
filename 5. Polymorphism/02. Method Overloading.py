# METHOD OVERLOADING is a feature that allows a class to have multiple methods with the same name, but different parameters
# This is a form of Polymorphism (one function name, multiple implementations)


# Python does not support method overloading in the same way that languages like C++ or Java do
# THE SOLUTION: We can achieve method overloading in Python through default arguments or variable-length arguments
class Calculator:
    # Method 1: Default arguments
    def add(self, a: int, b: int, c: int = 0) -> int:
        return a + b + c

    # Method 2: Variable-length arguments
    def add_multiple(self, *args: int) -> int:
        return sum(args)


# Example Usage:
# calc = Calculator()
#
# print(calc.add(5, 10))        # Output: 15
# print(calc.add(5, 10, 15))    # Output: 30
#
# print(calc.add_multiple(5, 10, 15, 20))    # Output: 50
# print(calc.add_multiple(1, 2))             # Output: 3
#


class TextProcessor:
    # Implement method overloading for format_text method
    def __init__(self):
        pass

    def format_text(self, text1: str, text2: str = None):
        if text2 is None:
            return text1.upper()
        else:
            return text1 + text2


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
