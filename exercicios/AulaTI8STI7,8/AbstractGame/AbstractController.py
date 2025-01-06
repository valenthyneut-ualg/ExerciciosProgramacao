from abc import ABC, abstractmethod
from .AbstractBoard import AbstractBoard

class AbstractController(ABC):
    def __init__(self, gameTitle: str, board: AbstractBoard, playerCount: int):
        self.gameTitle = gameTitle
        self.board = board
        self.playerCount = playerCount

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def turn(self): pass