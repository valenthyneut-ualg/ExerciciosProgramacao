from abc import abstractmethod
from typing import Any

from AbstractGame.Player import Player
from AbstractGame.Serializable import Serializable


class AbstractBoard(Serializable):
	def __init__(self, players: tuple[Player]):
		self.players = players

	@abstractmethod
	def play(self) -> Any: pass

	@abstractmethod
	def current_state(self) -> str: pass

	@abstractmethod
	def __str__(self) -> str: pass