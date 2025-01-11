from abc import abstractmethod
from .AbstractBoard import AbstractBoard
from .Player import Player
from .Serializable import Serializable

class AbstractController(Serializable):
	def __init__(self, title: str, board: AbstractBoard, playerCount: int, minPlayerCount: int):
		self.title = title
		self.board = board
		self.playerCount = playerCount
		self.minPlayerCount = minPlayerCount

		if self.playerCount < minPlayerCount:
			raise ValueError(f'Este jogo necessita de pelo menos {minPlayerCount} jogadores.')

	@abstractmethod
	def start(self) -> Player: pass

	@abstractmethod
	def turn(self): pass