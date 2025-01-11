from AbstractGame.AbstractBoard import AbstractBoard
from AbstractGame.Player import Player
from typing import Dict, cast, Any


class Board(AbstractBoard):
	def __init__(self, players: list[Player]):
		super().__init__([1] * len(players), players)

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

	def play(self, player: Player = Player("", "", {}, 0), spaces: int = 0) -> tuple[str, int | None, str] | None:
		try: playerIndex = self.players.index(player)
		except ValueError: raise ValueError("Jogador não presente na lista de jogadores!")
		# make the error a little more specific

		newPos = self.state[playerIndex] + spaces
		if newPos > 64: newPos = 64 - (newPos - 64)
		if newPos < 1: raise ValueError("Quantidade de espaços a mover inválida!")

		self.state[playerIndex] = newPos

		actionSpace = self.actionSpaces.get(newPos)
		if actionSpace is not None: return actionSpace[1], actionSpace[2], actionSpace[3]
		else: return None

	def inWinState(self) -> Player | None:
		if 64 in self.state:
			return self.players[cast(list[int], self.state).index(64)]
		else: return None

	def __str__(self):
		occupiedSpaces: list[int] = []
		for key in self.actionSpaces: occupiedSpaces.append(key)
		for position in cast(list[int], self.state):
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
			position = cast(list[int], self.state)[i]
			playerPositions.insert(i, [""] * occupiedSpacesLength)
			playerPositions[i][occupiedSpaces.index(position)] = self.players[i].symbol

		boardTable = playerPositions + [occupiedSpaces] + [symbols]
		boardString = ""

		for row in boardTable: boardString += ("{: <3}" * len(row)).format(*row) + "\n"
		return boardString

	def serialize(self) -> Dict[str, Any]:
		return {"state": self.state}