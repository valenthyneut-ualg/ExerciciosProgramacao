from abc import ABC, abstractmethod
from .AbstractBoard import AbstractBoard

class AbstractController(ABC):
	def __init__(self, title: str, board: AbstractBoard, playerCount: int):
		self.title = title
		self.board = board
		self.playerCount = playerCount

	@abstractmethod
	def start(self): pass

	@abstractmethod
	def turn(self): pass