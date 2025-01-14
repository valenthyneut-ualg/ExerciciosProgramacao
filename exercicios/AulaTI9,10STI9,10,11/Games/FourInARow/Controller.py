from typing import Literal, cast, Dict, Any

from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from Games.FourInARow.Board import Board


class Controller(AbstractController):
	def __init__(self, players: tuple[Player]):
		players = players[0:2]
		super().__init__(Board(players), players, 2)

		self.cur_player = players[0]
		self.player_turn = 0

	def start(self):
		print("Insira o número da coluna onde quer colocar a sua peça.")

		result = "ongoing", None
		while result[0] == "ongoing":
			result = self.turn()

		print()
		if result[0] == "draw": print("Empate!")
		elif result[0] == "win": print(f'O jogador "{result[1].name}" ganhou!')

	def turn(self) -> tuple[Literal["ongoing", "draw", "win"], Player | None]:
		board: Board = cast(Board, self.board)
		print(board)

		state, player = board.current_state()
		if state == "win": return "win", player
		elif state == "draw": return "draw", None

		rawInput = input(f'[{self.cur_player.symbol}] > ')
		try:
			column = int(rawInput)
			if column not in range(0, 8):
				raise ValueError("O número da coluna tem de estar entre 0 e 7, inclusivo.")

			board.play(self.cur_player, column)
			self.player_turn += 1
			if self.player_turn >= self.player_count: self.player_turn = 0
			self.cur_player = self.board.players[self.player_turn]
		except ValueError as error:
			print("Inseriu uma posição inválida.")
			print(error)

		return "ongoing", None

	def serialize(self) -> Dict[str, Any]:
		return {"player_turn": self.player_turn}

	def deserialize(self, data: Dict[str, Any]) -> None:
		super().deserialize(data)
		self.cur_player = self.board.players[self.player_turn]