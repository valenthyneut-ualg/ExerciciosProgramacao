class Board:
	def __init__(self):
		self.state: list[str] = [" "] * 9
		self.winStates = [
			[0, 1, 2], [3, 4, 5], [6, 7, 8],
			[0, 3, 6], [1, 4, 7], [2, 5, 8],
			[0, 4, 8], [2, 4, 6]
		]

	def display(self):
		print(f'{self.state[0]} | {self.state[1]} | {self.state[2]}')
		print('---------') 
		print(f'{self.state[3]} | {self.state[4]} | {self.state[5]}')
		print('---------')
		print(f'{self.state[6]} | {self.state[7]} | {self.state[8]}')

	def placePiece(self, player: str, linePosition: int, columnPosition: int):
		truePosition = (3 * (linePosition - 1) + columnPosition) - 1
		if self.state[truePosition] == " ": self.state[truePosition] = player
		else: raise ValueError("Essa posição já foi ocupada!")

	def inWinState(self) -> tuple[True, str] | tuple[False, None]:
		for winState in self.winStates:
			boardSlice = []
			for n in winState: boardSlice.append(self.state[n])
			if boardSlice[0] != " " and boardSlice.count(boardSlice[0]) == len(boardSlice):
				return True, boardSlice[0]
		return False, None