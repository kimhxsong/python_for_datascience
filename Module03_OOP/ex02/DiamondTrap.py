from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def get_eyes(self) -> str:
        return self.eyes
        # return super().eyes

    def set_eyes(self, eyes: str) -> None:
        self.eyes = eyes
        # super().__setattr__('eyes', eyes)

    def get_hairs(self) -> str:
        return self.hairs
        # return super().hairs

    def set_hairs(self, hairs: str) -> None:
        self.hairs = hairs
        # super().__setattr__('hairs', hairs)
