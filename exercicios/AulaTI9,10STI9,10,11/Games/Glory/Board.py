from typing import Dict, cast, Literal, Any

from AbstractGame.AbstractBoard import AbstractBoard
from AbstractGame.Player import Player


class Board(AbstractBoard):
	def __init__(self, players: tuple[Player, ...]):
		super().__init__(players)
		self.player_positions = [1] * len(self.players)

		self.action_spaces: Dict[int, tuple[str, str, int | None, str]] = {
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

	def play(self, player: Player = None, spaces: int = 0) -> tuple[str, int | None, str] | None:
		try: player_index = self.players.index(player)
		except ValueError: raise ValueError("Jogador não presente na lista de jogadores.")
		# make the error a little more specific

		new_pos = self.player_positions[player_index] + spaces
		if new_pos > 64: new_pos = 64 - (new_pos - 64)
		if new_pos < 1: raise ValueError("Quantidade de espaços a mover inválida!")

		self.player_positions[player_index] = new_pos

		action_space = self.action_spaces.get(new_pos)
		if action_space is not None: return action_space[1], action_space[2], action_space[3]
		else: return None

	def current_state(self) -> tuple[Literal["ongoing", "win"], Player | None]:
		if 64 in self.player_positions: return "win", self.players[self.player_positions.index(64)]
		else: return "ongoing", None

	def __str__(self):
		occupied_spaces: list[int] = []
		for key in self.action_spaces: occupied_spaces.append(key)
		for position in cast(list[int], self.player_positions):
			if position not in occupied_spaces: occupied_spaces.append(position)

		occupied_spaces.sort()
		occupied_spaces_length = len(occupied_spaces)

		symbols: list[str] = []
		for space in occupied_spaces:
			action_space = self.action_spaces.get(space)
			if action_space is None:
				symbols.append("")
			else:
				symbols.append(action_space[0])
		# No need to sort here since we're getting our indices from an already sorted list.

		player_positions: list[list[str]] = []
		for i in range(len(self.player_positions)):
			position = cast(list[int], self.player_positions)[i]
			player_positions.insert(i, [""] * occupied_spaces_length)
			player_positions[i][occupied_spaces.index(position)] = self.players[i].symbol

		board_table = player_positions + [occupied_spaces] + [symbols]
		board_string = ""

		for row in board_table: board_string += ("{: <3}" * len(row)).format(*row) + "\n"
		return board_string

	def serialize(self) -> Dict[str, Any]:
		return {"player_positions": self.player_positions}