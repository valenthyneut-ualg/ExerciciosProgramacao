from AbstractGame.AbstractController import AbstractController
from .Board import Board
from typing import cast

class Controller(AbstractController):
	def __init__(self):
		super().__init__("Jogo da forca", Board(), 1, 1)

	def turn(self) -> str:
		print(self.board)

		inWinState = self.board.inWinState()
		if inWinState: return "win"
		if cast(Board, self.board).attempts <= 0: return "loss"

		print()
		letter = input("Insira uma letra para adivinhar: ")

		print()
		if len(letter) != 1: print("Só pode tentar adivinhar uma letra de cada vez!")
		elif not letter.isalpha(): print("Só pode adivinhar letras do alfabeto!")
		else:
			state = cast(Board, self.board).play(letter)
			if state == "repeated": print("Já tentou adivinhar essa letra!")
			elif state == "correct": print(f'A palavra contém a letra "{letter}"!')
			elif state == "incorrect": print(f'A palavra não contém a letra "{letter}".')
			print()

		return "ongoing"

	def start(self):
		word = input("Insira uma palavra para começar o jogo: ")
		for char in word:
			isValid = char.isalpha() or char in cast(Board, self.board).prefillCharacters
			if not isValid:
				print("A palavra só pode conter caractéres alfabéticos!")
				self.start()
				break

		cast(Board, self.board).initWord(word)

		result = "ongoing"
		while result == "ongoing": result = self.turn()

		if result == "win": print(f'Ganhou! A palavra era "{self.board.state}".')
		elif result == "loss": print(f'Perdeu... A palavra era "{self.board.state}".')