from abc import ABC, abstractmethod

class AbstractBoard(ABC):
    def __init__(self, state):
        self.state = state

    @abstractmethod
    def play(self): pass

    @abstractmethod
    def inWinState(self): pass

    @abstractmethod
    def __str__(self): pass