from abc import abstractmethod
from .Player import Player
from .Serializable import Serializable


class AbstractBoard(Serializable):
	def __init__(self, state, players: list[Player]):
		self.state = state
		self.players = players

	@abstractmethod
	def play(self): pass

	@abstractmethod
	def inWinState(self): pass

	@abstractmethod
	def __str__(self): pass