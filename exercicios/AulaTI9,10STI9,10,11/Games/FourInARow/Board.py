from typing import Literal, Dict, Any

from AbstractGame.AbstractBoard import AbstractBoard
from AbstractGame.Player import Player


class Board(AbstractBoard):
	def __init__(self, players: tuple[Player, ...]):
		self.XY_AXES = ("row", "col")
		self.DIAG_AXES = ("asc", "desc")

		super().__init__(players)
		self.grid = [[" "] * 8 for _ in range(8)]
		self.last_played_pos = (0, 0)

	def __four_in_a_row_check(self, cut: list[str]) -> Player | None:
		old_player = ""
		count = 0

		for i in range(len(cut)):
			new_player = cut[i]
			if old_player != new_player:
				old_player = new_player
				count = 1
			else:
				if new_player.strip() != "": count += 1

			if count >= 4:
				for player in self.players:
					if old_player == player.symbol: return player
		return None

	def __xy_axis_check(self, axis: str, pos: tuple[int, int]) -> Player | None:
		if axis not in self.XY_AXES:
			raise ValueError("Eixo inválido! (tem de ser um de 'row', 'col'.)")

		xy_list = []
		for i in range(8):
			xy_list.append(self.grid[pos[0] if axis == "row" else i][pos[1] if axis == "col" else i])

		return self.__four_in_a_row_check(xy_list)

	def __diagonal_check(self, axis: str, pos: tuple[int, int]) -> Player | None:
		if axis not in self.DIAG_AXES:
			raise ValueError("Eixo inválido! (tem de ser um de 'asc', 'desc'.)")

		offset = 0
		diagonal = []

		for i in range(8):
			# In my way of storing the board, the row coordinate increasing means we are going lower into the board, so
			# everytime we want to go higher in a diagonal, we decrease the coordinate, and vice-versa for if we want to
			# go lower.
			offsetRowCoord = pos[0] + (-offset if axis == "asc" else offset)
			offsetColCoord = pos[1] + offset
			# Bounds checks so we don't get any weird "start from end of array" Python shenanigans
			if offsetRowCoord < 0 or offsetRowCoord > 7 or offsetColCoord < 0 or offsetColCoord > 7: break

			diagonal.append(self.grid[offsetRowCoord][offsetColCoord])
			offset += 1

		offset = -1
		for i in range(8):
			offsetRowCoord = pos[0] + (-offset if axis == "asc" else offset)
			offsetColCoord = pos[1] + offset
			if offsetRowCoord < 0 or offsetRowCoord > 7 or offsetColCoord < 0 or offsetColCoord > 7: break

			# Insert before the diagonal elements we already have because we're getting the lower elements of it
			diagonal.insert(0, self.grid[offsetRowCoord][offsetColCoord])
			offset -= 1

		return self.__four_in_a_row_check(diagonal)

	def play(self, player: Player = None, column: int = 0):
		if column not in range(8):
			raise ValueError("Número da coluna tem de estar entre 0 e 7, inclusivo.")

		last_empty_row = -1
		for i in range(8):
			if self.grid[i][column].strip() == "": last_empty_row = i

		if last_empty_row == -1: raise ValueError(f'A coluna {column} já está preenchida.')
		self.grid[last_empty_row][column] = player.symbol

		self.last_played_pos = (last_empty_row, column)
		return last_empty_row, column

	def current_state(self) -> tuple[Literal["ongoing", "draw", "win"], Player | None]:
		empty_count = 0
		for row in self.grid:
			for col in row:
				if col.strip() == "": empty_count += 1
		if empty_count == 0: return "draw", None

		for axis in self.XY_AXES:
			player = self.__xy_axis_check(axis, self.last_played_pos)
			if player: return "win", player

		for axis in self.DIAG_AXES:
			player = self.__diagonal_check(axis, self.last_played_pos)
			if player: return "win", player

		return "ongoing", None

	def __str__(self):
		boardString = ""
		for row in self.grid:
			rowString = ""
			rowLength = len(row)

			for i in range(rowLength):
				col = row[i]
				rowString += f' {col} '

				if i != rowLength - 1: rowString += "|"
			boardString += rowString + "\n"
		for i in range(8): boardString += f' {i}  '
		return boardString

	def serialize(self) -> Dict[str, Any]:
		return {"grid": self.grid, "last_played_pos": self.last_played_pos}