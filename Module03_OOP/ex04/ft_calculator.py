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

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(f"Dot product is: {sum([v1 * v2 for v1, v2 in zip(V1, V2)])}")

    # your code here
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print(f"Add Vector is : {[float(v1) + v2 for v1, v2 in zip(V1, V2)]}")

    # your code here
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print(f"Sous Vector is: {[float(v1) - v2 for v1, v2 in zip(V1, V2)]}")
