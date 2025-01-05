from typing import cast

from AbstractGame.AbstractController import AbstractController
from .Board import Board

class Controller(AbstractController):
	def __init__(self):
		super().__init__("Jogo do Galo", Board(), 2)

		self.curPlayer = "X"

	def turn(self) -> tuple[int, str] | None:
		print(str(self.board))

		inWinState, player = self.board.inWinState()
		if inWinState: return 1, player

		if cast(list[str], self.board.state).count(" ") == 0: return 0, ""

		print()
		gameInput = input(f'[{self.curPlayer}] > ')

		try:
			coordinates = [int(n) for n in gameInput.split(", ")]
			if len(coordinates) != 2:
				raise ValueError("Tem de inserir dois valores nas coordenadas.")

			if coordinates[0] not in range(1, 4) or coordinates[1] not in range(1, 4):
				raise ValueError("Os valores das coordenadas têm de estar entre 1 e 3, inclusivo.")

			# WHY DO I HAVE TO TYPECAST???
			cast(Board, self.board).play(self.curPlayer, coordinates[0], coordinates[1])
			self.curPlayer = "O" if self.curPlayer == "X" else "X"
		except ValueError as error:
			print("Inseriu uma posição inválida.")
			print(error)

		return None

	def start(self):
		print("Insira um par de coordenadas separado por vírgula onde:")
		print("O primeiro número é a linha e o segundo a coluna.")
		print("Exemplo: 2, 3")

		result = None
		while result is None:
			result = self.turn()

		if result[0] == 0: print("Empate!")
		elif result[0] == 1: print(f'O jogador [{result[1]}] ganhou!')