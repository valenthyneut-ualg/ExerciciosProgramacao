from typing import Literal, Dict, Any

from AbstractGame.AbstractBoard import AbstractBoard
from AbstractGame.Player import Player


class Board(AbstractBoard):
	def __init__(self, players: tuple[Player]):
		self.WINSTATES = (
			(0, 1, 2), (3, 4, 5), (6, 7, 8),
			(0, 3, 6), (1, 4, 7), (2, 5, 8),
			(0, 4, 8), (2, 4, 6)
		)

		super().__init__()
		self.grid = [" "] * 9
		self.players = players[0:2]

	def play(self, player: Player = None, pos: tuple[int, int] = None):
		x, y = pos
		one_dimension_pos = (3 * x) + y

		if self.grid[one_dimension_pos] == " ":
			self.grid[one_dimension_pos] = player.symbol
		else:
			raise ValueError(f'A posição {x}, {y} já foi ocupada.')

	def current_state(self) -> (tuple[Literal["ongoing"], None] |
								tuple[Literal["win"], Player] |
								tuple[Literal["draw"], None]):
		if self.grid.count(" ") == 0: return "draw", None

		for cutter in self.WINSTATES:
			grid_slice = []
			for cut in cutter: grid_slice.append(self.grid[cut])
			first_cut = grid_slice[0]
			if first_cut != " " and grid_slice.count(first_cut) == len(grid_slice):
				for player in self.players:
					if first_cut == player.symbol: return "win", player

		return "ongoing", None

	def __str__(self) -> str:
		grid_string = "  ".join([str(i) for i in range(len(self.grid))])
		for i in range(3):
			grid_string += f'{i} '
			for j in range(3):
				one_dimension_pos = (3 * i) + j
				grid_string += f'{self.grid[one_dimension_pos]} '

		return grid_string

	def serialize(self) -> Dict[str, Any]:
		return {"grid": self.grid}