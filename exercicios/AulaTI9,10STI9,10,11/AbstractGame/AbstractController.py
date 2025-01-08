from abc import ABC, abstractmethod
from .AbstractBoard import AbstractBoard

class AbstractController(ABC):
	def __init__(self, title: str, board: AbstractBoard, playerCount: int, minPlayerCount: int):
		self.title = title
		self.board = board
		self.playerCount = playerCount
		self.minPlayerCount = minPlayerCount

		if self.playerCount < minPlayerCount:
			raise ValueError(f'Este jogo necessita de pelo menos {minPlayerCount} jogadores.')

	@abstractmethod
	def start(self): pass

	@abstractmethod
	def turn(self): pass