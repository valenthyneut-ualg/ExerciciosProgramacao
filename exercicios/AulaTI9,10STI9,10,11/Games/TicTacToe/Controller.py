from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from .Board import Board
from typing import cast

class Controller(AbstractController):
	def __init__(self, players: list[Player]):
		super().__init__("Jogo do galo", Board(players), 2)
		self.curPlayer = players[0]
		self.playerTurn = 0

	def turn(self) -> tuple[str, Player] | tuple[str, None]:
		print(self.board)

		player = cast(Board, self.board).inWinState()
		inWinState = player is not None
		if inWinState: return "win", player

		if cast(list[str], self.board.state).count(" ") == 0: return "draw", None

		print()
		rawPosition = input(f'[{self.curPlayer.symbol}] > ')

		try:
			coordinates = [int(n) for n in rawPosition.split(",")]
			if len(coordinates) != 2:
				raise ValueError("Tem de inserir exatamente dois valores nas coordenadas.")

			if coordinates[0] not in range(1, 4) or coordinates[1] not in range(1, 4):
				raise ValueError("Os valores das coordenadas têm de estar entre 1 e 3, inclusivo.")

			cast(Board, self.board).play(self.curPlayer, coordinates[0], coordinates[1])

			self.playerTurn += 1
			if self.playerTurn >= self.playerCount: self.playerTurn = 0
			self.curPlayer = self.board.players[self.playerTurn]

		except ValueError as error:
			print("Inseriu uma posição inválida!")
			print(error)

		return "ongoing", None

	def start(self):
		print("Insira um par de coordenadas separado por vírgula onde:")
		print("O primeiro número é a linha e o segundo é a coluna.")
		print("Exemplo: 2, 3")

		result = "ongoing", None
		while result[0] == "ongoing":
			result = self.turn()

		print()
		if result[0] == "draw": print("Empate!")
		elif result[0] == "win": print(f'O jogador "{result[1]}" ganhou!')