from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""

    @abstractmethod
    def __init__(self, first_name, is_alive: bool = True):
        """Your docstring for constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Your docstring for method"""
        self.is_alive = False

    @abstractmethod
    def is_alive(self):
        """Your docstring for method"""
        return self.is_alive

    def __str__(self):
        copied = self.__dict__.copy()
        del copied['first_name'], copied['is_alive']
        return f"Vector: {tuple(copied.values())}"

    def __repr__(self):
        return self.__str__()


class Stark(Character):
    """Your docstring for Class"""

    def __init__(self, first_name, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for method"""
        super().die()

    def is_alive(self):
        """Your docstring for method"""
        return super().is_alive()
