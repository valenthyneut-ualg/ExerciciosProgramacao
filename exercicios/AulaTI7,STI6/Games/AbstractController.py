from abc import ABC, abstractmethod

class AbstractController(ABC):
    def __init__(self, playerCount: int):
        self.playerCount = playerCount

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def turn(self, player: int): pass