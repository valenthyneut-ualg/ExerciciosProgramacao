from AbstractGame.AbstractBoard import AbstractBoard
from typing import Dict, cast

class Board(AbstractBoard):
	def __init__(self, playerCount: int):
		super().__init__([1] * playerCount)

		self.actionSpaces: Dict[int, tuple[str, str, int | None, str]] = {
			1: ("b", "none", None, ""),

			8: ("M+", "move", 10, "És teleportado para a posição 18!"),
			15: ("M-", "move", -3, "Oops! És arrastado 3 posições de volta."),
			23: ("M+", "move", 4, "Boa! Avança mais 4 posições!"),
			28: ("S", "skip", None, "Má sorte! Salta a tua próxima jogada."),
			33: ("R", "reroll", None, "Atira os dados de novo para te moveres mais!"),
			39: ("M+", "move", 8, "Altamente! Avança mais 8 posições!"),
			40: ("S", "skip", None, "Que pena! Salta a tua próxima jogada."),
			48: ("M-", "move", -11, "És lançado 11 posições de volta."),
			54: ("R", "reroll", None, "Atira os dados de novo para avançares um pouco mais!"),
			56: ("M-", "move", -8, "És arrastado 8 posições de volta."),
			63: ("D", "move", -62, "Morreste! Começa do início."),

			64: ("g", "none", None, "")
		}

	def play(self, player: int = -1, spaces: int = -1) -> tuple[str, int | None, str] | tuple[None, None, None]:
		newPos = self.state[player] + spaces
		if newPos > 64: newPos = 64 - (newPos - 64)
		if newPos < 1: raise ValueError("Quantidade de espaços inválida!")

		self.state[player] = newPos

		actionSpace = self.actionSpaces.get(newPos)
		if actionSpace is not None: return actionSpace[1], actionSpace[2], actionSpace[3]
		else: return None, None, None

	def inWinState(self) -> tuple[True, int] | tuple[False, None]:
		try:
			lastPlaceIndex = cast(list[int], self.state).index(64)
			return True, self.state[lastPlaceIndex]
		except ValueError:
			return False, None

	def __str__(self):
		occupiedSpaces: list[int] = []
		for key in self.actionSpaces: occupiedSpaces.append(key)
		for position in self.state:
			if position not in occupiedSpaces: occupiedSpaces.append(position)

		occupiedSpaces.sort()
		occupiedSpacesLength = len(occupiedSpaces)

		symbols: list[str] = []
		for space in occupiedSpaces:
			actionSpace = self.actionSpaces.get(space)
			if actionSpace is None: symbols.append("")
			else: symbols.append(actionSpace[0])
		# No need to sort here since we're getting our indices from an already sorted list.

		playerPositions: list[list[str]] = []
		for i in range(len(self.state)):
			position = self.state[i]
			playerPositions.insert(i, [""] * occupiedSpacesLength)
			playerPositions[i][occupiedSpaces.index(position)] = str(i + 1)

		boardTable = playerPositions + [occupiedSpaces] + [symbols]
		boardString = ""

		for row in boardTable: boardString += ("{: <3}" * len(row)).format(*row) + "\n"
		return boardString