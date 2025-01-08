from abc import ABC, abstractmethod
from .AbstractBoard import AbstractBoard
from typing import Dict, Any

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

	@abstractmethod
	def serialize(self) -> Dict[str, Any]: pass

	@abstractmethod
	def deserialize(self, rawData: str): pass