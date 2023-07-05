import sys


class calculator:
    """My own minimal calculator"""

    def __init__(self, vector):
        self.vector = vector.copy()

    # your code here
    def __add__(self, object) -> None:
        print([value + object for value in self.vector])

    # your code here
    def __mul__(self, object) -> None:
        print([value * object for value in self.vector])

    # your code here
    def __sub__(self, object) -> None:
        print([value - object for value in self.vector])

    # your code here
    def __truediv__(self, object) -> None:
        try:
            print([value / object for value in self.vector])

        except ZeroDivisionError:
            sys.stderr.write("Error: Cannot divide by zero. Please provide a non-zero denominator.\n")
