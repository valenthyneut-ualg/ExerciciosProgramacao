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
			print()

	def start(self):
		word = input("Insira uma palavra para começar o jogo: ")
		for char in word:
			isValid = char.isalpha() or char in cast(Board, self.board).prefillCharacters
			if not isValid:
				print("A palavra só pode conter caractéres alfabéticos!")
				self.start()
				break

		cast(Board, self.board).initWord(word)

		result = None
		while result is None:
			result = self.turn()

		if result == 0: print(f'Perdeu! A palavra era {self.board.state}.')
		if result == 1: print(f'Ganhou! A palavra era {self.board.state}!')