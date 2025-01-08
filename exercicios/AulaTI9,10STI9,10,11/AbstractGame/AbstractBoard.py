from abc import ABC, abstractmethod
from .Player import Player
from typing import Dict, Any

class AbstractBoard(ABC):
	def __init__(self, state, players: list[Player]):
		self.state = state
		self.players = players

	@abstractmethod
	def play(self): pass

	@abstractmethod
	def inWinState(self): pass

	@abstractmethod
	def __str__(self): pass

	@abstractmethod
	def serialize(self) -> Dict[str, Any]: pass

	@abstractmethod
	def deserialize(self, rawData: str): pass