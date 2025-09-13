# Multiple Inheritance is a powerful but complex feature. It is important to use Multiple Inheritance carefully.
# If used incorrectly, you can encounter situations where methods are inherited from multiple parent classes.
# This leads to ambiguous behavior known as the DIAMOND PROBLEM


# Let's see an example of the Diamond Problem:
class A:
    def print_method(self) -> None:
        print("A")


class B(A):
    def print_method(self) -> None:
        print("B")


class C(A):
    def print_method(self) -> None:
        print("C")


class D(B, C):
    pass


d = D()
d.print_method()  # Which method will be called?

# In the above code, you can see that [D] is inherting from both [B] and [C], which both inherit from [A]
# Now, when you call d.print_method(), which method will be called? This ambiguity is known as the DIAMOND PROBLEM
# The inheritance structure creates a diamond shape, as illustrated below:
#    A
#   / \
#  B   C
#   \ /
#    D

# How Python resolves methods:
# Python uses Method Resolution Order (MRO) to determine which method to output when dealing with multiple inheritance.
#   First, Python looks for the method in the current class [D]
#   If not found, it checks the first Parent Class [B] as it was the first parent passed to the D class
#   Then, the second Parent Class [C] as it is the second Parent of the [D] class
#   Finally, it checks the base class [A]

# You can view this order using the __mro__ attribute
print(D.__mro__)
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


# CHALLENGE: Given the starter code below, the current MRO will print C. Modify it so that it instead prints B.
class A:
    def print_method(self) -> None:
        print("A")


class B(A):
    def print_method(self) -> None:
        print("B")


class C(A):
    def print_method(self) -> None:
        print("C")


class D(B, C):
    pass


# Do not change the code below
d = D()
d.print_method()
