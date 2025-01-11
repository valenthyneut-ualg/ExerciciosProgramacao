from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from .Board import Board
from typing import cast, Dict, Any

class Controller(AbstractController):
	def __init__(self, players: list[Player]):
		super().__init__("Jogo da forca", Board(players), 2, 2)

	def turn(self) -> str:
		print(self.board)

		inWinState = self.board.inWinState()
		if inWinState: return "win"
		if cast(Board, self.board).attempts <= 0: return "loss"

		print()
		letter = input(f'{self.board.players[1].name}, insira uma letra para adivinhar: ')

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
		if len(cast(Board, self.board).state) == 0:
			word = input(f'{self.board.players[0].name}, insira uma palavra para começar o jogo: ')
			for char in word:
				isValid = char.isalpha() or char in cast(Board, self.board).prefillCharacters
				if not isValid:
					print("A palavra só pode conter caractéres alfabéticos!")
					self.start()
					break

			cast(Board, self.board).initWord(word)

		result = "ongoing"
		while result == "ongoing": result = self.turn()

		if result == "win": winner = self.board.players[1]
		else: winner = self.board.players[0]

		print(f'A palavra era "{self.board.state}". O jogador "{winner.name}" ganhou!')
		return winner

	def serialize(self) -> Dict[str, Any]:
		return {}