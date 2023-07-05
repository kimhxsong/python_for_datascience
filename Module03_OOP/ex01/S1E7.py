from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        super().die()

    def is_alive(self) -> bool:
        return super().is_alive()


# your code here
class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        super().die()

    def is_alive(self) -> bool:
        return super().is_alive()

    @staticmethod
    def create_lannister(first_name: str, is_alive=True) -> object:
        return Lannister(first_name, is_alive)
