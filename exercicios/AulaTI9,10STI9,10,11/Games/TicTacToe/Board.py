from AbstractGame.AbstractBoard import AbstractBoard
from AbstractGame.Player import Player

class Board(AbstractBoard):
	def __init__(self, players: list[Player]):
		super().__init__([" "] * 9, players)
		self.winStates = [
			[0, 1, 2], [3, 4, 5], [6, 7, 8],
			[0, 3, 6], [1, 4, 7], [2, 5, 8],
			[0, 4, 8], [2, 4, 6]
		]

	def play(self, player: Player = Player("", ""), linePosition: int = 1, columnPosition: int = 1):
		oneDimensionPosition = (3 * (linePosition - 1) + columnPosition) - 1
		if self.state[oneDimensionPosition] == " ": self.state[oneDimensionPosition] = player.symbol
		else: raise ValueError("Essa posição já foi ocupada!")

	def inWinState(self) -> Player | None:
		for winState in self.winStates:
			boardSlice = []
			for n in winState: boardSlice.append(self.state[n])
			if boardSlice[0] != " " and boardSlice.count(boardSlice[0]) == len(boardSlice):
				for player in self.players:
					if boardSlice[0] == player.symbol: return player
		return None

	def __str__(self) -> str:
		return "\n".join([
			f'{self.state[0]} | {self.state[1]} | {self.state[2]}',
			"---------",
			f'{self.state[3]} | {self.state[4]} | {self.state[5]}',
			"---------",
			f'{self.state[6]} | {self.state[7]} | {self.state[8]}'
		])