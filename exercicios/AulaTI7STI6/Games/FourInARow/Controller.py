from AbstractGame.AbstractController import AbstractController
from .Board import Board
from typing import cast

class Controller(AbstractController):
	def __init__(self):
		super().__init__("Quatro em linha", Board(), 2)

		self.curPlayer: str = "X"
		self.lastPlayedCoords: tuple[int, int] = (1, 1)

	def start(self):
		print("Insira o número onde quer colocar a sua peça.")

		result = None
		while result is None:
			result = self.turn()

		print(f'O jogador [{result[1]}] ganhou!')

	def turn(self) -> tuple[int, str]:
		print()
		print(str(self.board))

		inWinState, player = cast(Board, self.board).inWinState(self.lastPlayedCoords)
		if inWinState: return 1, player

		gameInput = input(f'[{self.curPlayer}] > ')

		try:
			column = int(gameInput)
			if column not in range (1, 9): raise ValueError("O número da coluna tem de estar compreendido entre 1 e 8, inclusivo.")

			self.lastPlayedCoords = cast(Board, self.board).play(self.curPlayer, column)
			self.curPlayer = "X" if self.curPlayer == "O" else "O"
		except ValueError as error:
			print("Inseriu uma posição inválida.")
			print(error)