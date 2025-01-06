from AbstractGame.AbstractController import AbstractController
from .Board import Board
from typing import cast

class Controller(AbstractController):
	def __init__(self):
		super().__init__("Jogo da forca", Board(), 1)

	def turn(self) -> int | None:
		print(str(self.board))

		inWinState = self.board.inWinState()
		if inWinState: return 1
		if cast(Board, self.board).attempts <= 0: return 0

		print()
		letter = input("Escreva uma letra para adivinhar: ")

		print()
		if len(letter) != 1: print("Só pode tentar adivinhar uma letra!")
		elif not letter.isalpha(): print("Só pode adivinhar letras do alfabeto!")
		else:
			state = cast(Board, self.board).play(letter)
			if state == 0: print("Já tentou adivinhar essa letra!")
			elif state == 1: print(f'A palavra contém a letra {letter}!')
			elif state == 2: print(f'A palavra não contém a letra {letter}!')

	def start(self):
		word = None
		while word is None:
			temp = input("Insire uma palavra para começar o jogo: ")
			if temp.isalpha(): word = temp
			else: print("A palavra só pode conter caractéres do alfabeto!")

		cast(Board, self.board).initWord(word)

		result = None
		while result is None:
			result = self.turn()

		if result == 0: print(f'Perdeu! A palavra era {self.board.state}.')
		if result == 1: print(f'Ganhou! A palavra era {self.board.state}!')