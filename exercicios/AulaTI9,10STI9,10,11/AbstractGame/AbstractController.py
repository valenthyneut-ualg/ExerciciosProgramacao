from abc import abstractmethod

from AbstractGame.AbstractBoard import AbstractBoard
from AbstractGame.Player import Player
from .Serializable import Serializable


class AbstractController(Serializable):
	def __init__(self, board: AbstractBoard, players: list[Player], min_player_count: int):
		self.board = board
		self.players = players
		self.player_count = len(players)
		self.min_player_count = min_player_count

		if self.player_count < min_player_count:
			raise ValueError(f'Este jogo necessita de pelo menos {self.min_player_count} jogadores, '
							 f'enquanto {self.player_count} foram especificados.')

	@abstractmethod
	def start(self) -> Player: pass

	@abstractmethod
	def turn(self): pass