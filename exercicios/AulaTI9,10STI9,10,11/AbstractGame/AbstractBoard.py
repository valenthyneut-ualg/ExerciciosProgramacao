from abc import abstractmethod
from typing import Any

from AbstractGame.Serializable import Serializable


class AbstractBoard(Serializable):
	@abstractmethod
	def play(self) -> Any: pass

	@abstractmethod
	def current_state(self) -> str: pass

	@abstractmethod
	def __str__(self) -> str: pass