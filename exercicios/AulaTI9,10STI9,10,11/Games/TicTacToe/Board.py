from typing import Literal, Dict, Any

from AbstractGame.AbstractBoard import AbstractBoard
from AbstractGame.Player import Player


class Board(AbstractBoard):
	def __init__(self, players: tuple[Player, ...]):
		self.WINSTATES = (
			(0, 1, 2), (3, 4, 5), (6, 7, 8),
			(0, 3, 6), (1, 4, 7), (2, 5, 8),
			(0, 4, 8), (2, 4, 6)
		)

		super().__init__(players)
		self.grid = [" "] * 9

	def play(self, player: Player = None, pos: tuple[int, int] = None):
		x, y = pos
		one_dimension_pos = (3 * x) + y

		if self.grid[one_dimension_pos] == " ":
			self.grid[one_dimension_pos] = player.symbol
		else:
			raise ValueError(f'A posição {x}, {y} já foi ocupada.')

	def current_state(self) -> tuple[Literal["ongoing", "draw", "win"], Player | None]:
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
		return "\n".join([
			"    0   1   2\n",
			f'0   {self.grid[0]} | {self.grid[1]} | {self.grid[2]}',
			"   -----------",
			f'1   {self.grid[3]} | {self.grid[4]} | {self.grid[5]}',
			"   -----------",
			f'2   {self.grid[6]} | {self.grid[7]} | {self.grid[8]}'
		])

	def serialize(self) -> Dict[str, Any]:
		return {"grid": self.grid}