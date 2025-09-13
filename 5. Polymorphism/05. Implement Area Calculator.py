# CHALLENGE: You are given an empty AreaCalc class. Implement a method calculate(length, width=None) that handles 2 types of calcs:
#   1. When given one argument, radius, it should calculate circle area: math.pi*(radius**2); round to 2 decimal places
#   2. When given two arguments, length and width, it should calculate length * width; return result as-is


import math


class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, num1, num2=None):
        if num2 == None:
            output = round((math.pi * (num1**2)), 2)
            return output
        else:
            return num1 * num2


# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))
print(calc.calculate(4, 6))
