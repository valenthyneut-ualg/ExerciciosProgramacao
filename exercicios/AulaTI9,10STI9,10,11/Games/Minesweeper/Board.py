from random import randint
from typing import Literal, Dict, Any

from AbstractGame.AbstractBoard import AbstractBoard
from AbstractGame.Player import Player


class Board(AbstractBoard):
	def __init__(self, players: tuple[Player, ...], grid_size: int = 9):
		self.SYMBOLS = {
			"revealed": " ",
			"mine": 	"*",
			"flagged": 	"F",
			"unknown": 	"#"
		}

		super().__init__(players)
		self.grid_size = grid_size
		self.grid = [[self.SYMBOLS["unknown"] * self.grid_size for _ in range(grid_size)]]
		self.mine_pos: set[tuple[int, int]] = set()
		self.flag_pos: set[tuple[int, int]] = set()
		self.hit_mines = False

	def adjacent_tile_pos(self, pos: tuple[int, int]) -> tuple[tuple[int, int], ...]:
		tile_pos: list[tuple[int, int]] = []
		directions = [(-1, -1), (-1,  0), (-1,  1),
					  ( 0, -1),           ( 0,  1),
					  ( 1, -1), ( 1,  0), ( 1,  1)]

		for directionX, directionY in directions:
			offsetX, offsetY = pos[0] + directionX, pos[1] + directionY
			if offsetX not in range(0, self.grid_size) or offsetY not in range(0, self.grid_size): continue
			else: tile_pos.append((offsetX, offsetY))

		return tuple(tile_pos)

	def check_around(self, pos: tuple[int, int]) -> int:
		mine_count = 0

		for pos in self.adjacent_tile_pos(pos):
			if pos in self.mine_pos: mine_count += 1

		return mine_count

	def bfsUpdate(self, start_pos: tuple[int, int]):
		queue = [start_pos]
		visited = set()

		while queue:
			pos = queue.pop(0)
			pos_x, pos_y = pos
			is_valid_tile = pos[0] in range(0, self.grid_size) and pos[1] in range(0, self.grid_size)
			if pos in visited or not is_valid_tile: continue

			visited.add(pos)
			self.grid[pos_x][pos_y] = self.SYMBOLS["revealed"]

			surrounding_mine_count = self.check_around(pos)
			if surrounding_mine_count > 0:
				self.grid[pos_x][pos_y] = str(surrounding_mine_count)
				continue

			for pos in self.adjacent_tile_pos(pos): queue.append(pos)

	def reveal_mines(self):
		self.hit_mines = True
		for mine_x, mine_y in self.mine_pos:
			self.grid[mine_x][mine_y] = self.SYMBOLS["mine"]

	def init_mines(self, starting_pos: tuple[int, int]):
		while len(self.mine_pos) < self.grid_size:
			random_pos = (randint(0, self.grid_size - 1), randint(0, self.grid_size - 1))
			if random_pos not in self.mine_pos and random_pos != starting_pos: self.mine_pos.add(random_pos)

	def play(self, player: Player = None, pos: tuple[int, int] = (0, 0), flagged: bool = False) -> Literal["flagged", "unflagged", "hit_mine", "ongoing"]:
		pos_x, pos_y = pos
		if pos_x not in range(0, self.grid_size):
			raise ValueError(f'A posição X tem de estar entre 0 e {self.grid_size}, inclusivo.')

		if pos_y not in range(0, self.grid_size):
			raise ValueError(f'A posição Y tem de estar entre 0 e {self.grid_size}, inclusivo.')

		if flagged:
			if self.grid[pos_x][pos_y] not in (self.SYMBOLS["unknown"], self.SYMBOLS["flagged"]):
				raise ValueError("Essa posição já foi revelada.")

			if pos not in self.flag_pos:
				self.flag_pos.add(pos)
				self.grid[pos_x][pos_y] = self.SYMBOLS["flagged"]
				return "flagged"
			else:
				self.flag_pos.remove(pos)
				self.grid[pos_x][pos_y] = self.SYMBOLS["unknown"]
				return "unflagged"

		if pos in self.mine_pos:
			self.reveal_mines()
			return "hit_mine"

		self.bfsUpdate(pos)
		return "ongoing"

	def current_state(self) -> str:
		if self.hit_mines: return "loss"
		elif self.flag_pos == self.mine_pos: return "win"
		else: return "ongoing"

	def __str__(self) -> str:
		board_str = "     "

		for i in range(0, self.grid_size): board_str += f'{i}  '
		board_str += "\n"

		for i in range(0, self.grid_size):
			board_str += f'\n{i}    '
			for j in range(0, self.grid_size):
				board_str += f'{self.grid[i][j]}  '

		return board_str

	def serialize(self) -> Dict[str, Any]:
		return {
			"grid": self.grid,
			"grid_size": self.grid_size,
			"mine_pos": self.mine_pos,
			"flag_pos": self.flag_pos,
			"symbols": self.SYMBOLS
		}