from typing import cast, Literal, Dict, Any

from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from Games.TicTacToe.Board import Board

class Controller(AbstractController):
	def __init__(self, players: tuple[Player, ...]):
		players = players[0:2]
		super().__init__(Board(players), players, 2)

		self.cur_player = players[0]
		self.player_turn = 0

	def turn(self) -> tuple[Literal["ongoing", "draw", "win"], Player | None]:
		board: Board = cast(Board, self.board)
		print(board)

		state, player = board.current_state()
		if state == "win": return state, player
		elif state == "draw": return state, None

		print()
		raw_pos = input(f'[{self.cur_player.symbol}] > ')

		try:
			parsedCoords = [int(coord) for coord in raw_pos.split(',')]

			if len(parsedCoords) != 2:
				raise ValueError("Tem de inserir exatamete dois valores nas coordenadas.")

			if parsedCoords[0] not in range(0, 3) or parsedCoords[1] not in range(0, 3):
				raise ValueError("Os valores das coordenadas têm de estar entre 0 e 2, inclusivo.")

			coords = (parsedCoords[0], parsedCoords[1])
			board.play(self.cur_player, coords)

			self.player_turn += 1
			if self.player_turn >= self.player_count: self.player_turn = 0
			self.cur_player = self.board.players[self.player_turn]
		except ValueError as error:
			print("Inseriu uma posição inválida.")
			print(error)

		return "ongoing", None

	def start(self):
		print("Insira duas coordenadas onde:")
		print("O primeiro número e a linha, e o segunda a coluna.")
		print("Exemplo: 1, 2")

		result = "ongoing", None
		while result[0] == "ongoing": result = self.turn()

		print()
		if result[0] == "draw": print("Empate!")
		elif result[0] == "win": print(f'O jogador "{result[1].name}" ganhou!')

		return result[1]

	def serialize(self) -> Dict[str, Any]:
		return {"player_turn": self.player_turn}

	def deserialize(self, data: Dict[str, Any]) -> None:
		super().deserialize(data)
		self.cur_player = self.board.players[self.player_turn]