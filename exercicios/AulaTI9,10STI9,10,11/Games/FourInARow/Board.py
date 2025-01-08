from AbstractGame.AbstractBoard import AbstractBoard
from AbstractGame.Player import Player

class Board(AbstractBoard):
	def __init__(self, players: list[Player]):
		super().__init__([[" "] * 8 for _ in range(8)], players)

	def __fourInARowCheck(self, boardSlice: list[str]) -> Player | None:
		oldPlayer = ""
		count = 0

		for i in range(len(boardSlice)):
			newPlayer = boardSlice[i]
			if oldPlayer != newPlayer:
				oldPlayer = newPlayer
				count = 1
			else:
				if newPlayer != " ": count += 1
			if count >= 4:
				for player in self.players:
					if oldPlayer == player.symbol: return player
		return None

	def __xyAxisCheck(self, axis: str, rowCoord: int, colCoord: int) -> Player | None:
		if axis != "row" and axis != "col": raise ValueError("Eixo inválido! (tem de ser um de 'row' ou 'col'.)")

		xyList = []
		for i in range(8): xyList.append(self.state[rowCoord if axis == "row" else i][colCoord if axis == "col" else i])

		return self.__fourInARowCheck(xyList)

	def __diagonalCheck(self, axis: str, rowCoord: int, colCoord: int) -> Player | None:
		if axis != "asc" and axis != "desc": raise ValueError("Eixo inválido! (tem de ser um de 'asc' ou 'desc')")

		offset = 0
		diagonal = []

		for i in range(8):
			# In my way of storing the board, the row coordinate increasing means we are going lower into the board, so
			# everytime we want to go higher in a diagonal, we decrease the coordinate, and vice-versa for if we want to
			# go lower.
			offsetRowCoord = rowCoord + (-offset if axis == "asc" else offset)
			offsetColCoord = colCoord + offset
			# Bounds checks so we don't get any weird "start from end of array" Python shenanigans
			if offsetRowCoord < 0 or offsetRowCoord > 7 or offsetColCoord < 0 or offsetColCoord > 7: break

			diagonal.append(self.state[offsetRowCoord][offsetColCoord])
			offset += 1

		offset = -1
		for i in range(8):
			offsetRowCoord = rowCoord + (-offset if axis == "asc" else offset)
			offsetColCoord = colCoord + offset
			if offsetRowCoord < 0 or offsetRowCoord > 7 or offsetColCoord < 0 or offsetColCoord > 7: break

			# Insert before the diagonal elements we already have because we're getting the lower elements of it
			diagonal.insert(0, self.state[offsetRowCoord][offsetColCoord])
			offset -= 1

		return self.__fourInARowCheck(diagonal)

	def play(self, player: Player = Player("", ""), column: int = 1) -> tuple[int, int]:
		if column <= 0 or column > 8: raise ValueError("Número da coluna tem de ser entre 1 e 8 inclusivo.")
		zeroIndexColumn = column - 1

		lastEmptyRow = -1
		for i in range(8):
			if self.state[i][zeroIndexColumn].strip() == "": lastEmptyRow = i

		if lastEmptyRow == -1: raise ValueError("A coluna já está preenchida.")
		self.state[lastEmptyRow][zeroIndexColumn] = player.symbol

		return lastEmptyRow + 1, column

	def inWinState(self, propagationPoint: tuple[int, int] = (1, 1)) -> Player | None:
		rowCoord = propagationPoint[0]
		if rowCoord <= 0 or rowCoord > 8: raise ValueError("Nº da linha tem de estar entre 1 e 8, inclusivo.")
		zeroIndexRowCoord = rowCoord - 1

		colCoord = propagationPoint[1]
		if colCoord <= 0 or colCoord > 8: raise ValueError("Nº da coluna tem de estar entre 1 e 8, inclusivo.")
		zeroIndexColCoord = colCoord - 1

		xyAxes = ("row", "col")
		for axis in xyAxes:
			player = self.__xyAxisCheck(axis, zeroIndexRowCoord, zeroIndexColCoord)
			if player: return player

		diagAxes = ("asc", "desc")
		for axis in diagAxes:
			player = self.__diagonalCheck(axis, zeroIndexRowCoord, zeroIndexColCoord)
			if player: return player

		return None

	def __str__(self):
		boardString = ""
		for row in self.state:
			rowString = ""
			rowLength = len(row)

			for i in range(rowLength):
				col = row[i]
				rowString += f' {col} '

				if i != rowLength - 1: rowString += "|"
			boardString += rowString + "\n"
		for i in range(8): boardString += f' {i + 1}  '
		return boardString