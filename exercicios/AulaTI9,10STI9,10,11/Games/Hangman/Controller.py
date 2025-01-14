from typing import cast, Dict, Any

from AbstractGame.AbstractController import AbstractController
from AbstractGame.Player import Player
from Games.Hangman.Board import Board


class Controller(AbstractController):
	def __init__(self, players: tuple[Player, ...]):
		super().__init__(Board(players), players, 1)

	def turn(self):
		board: Board = cast(Board, self.board)
		print(board)

		state = self.board.current_state()
		if state == "win": return "win"
		elif state == "loss": return "loss"

		print()
		letter = input(
			f'{board.players[1].name}, insira uma letra para adivinhar: ' if len(board.players) >= 2
			else "Insira uma letra para adivinhar: "
		)

		print()
		if len(letter) != 1:
			print("Só pode tentar adivinhar uma letra de cada vez.")
		elif not letter.isalpha() and letter not in board.prefill_characters:
			print("Só pode tentar adivinhar letras do alfabeto.")
		else:
			result = board.play(letter)
			if result == "repeated": print("Já tentou adivinhar essa letra.")
			elif state == "correct": print(f'A palavra contém a letra "{letter}"!')
			elif state == "incorrect": print(f'A palavra não contém a letra "{letter}".')
			print()

		return "ongoing"

	def start(self):
		board: Board = cast(Board, self.board)
		more_than_one_player = len(board.players) > 1

		if len(board.word) == 0:
			word = input(
				f'{board.players[0].name}, insira uma palavra para começar: ' if more_than_one_player
				else "Insira uma palavra para começar: "
			)
			for char in word:
				is_valid = char.isalpha() or char in board.prefill_characters
				if not is_valid:
					print("A palavra só pode conter carácteres alfabéticos!")
					self.start()
					break

			board.init_word(word)

		result = "ongoing"
		while result == "ongoing": result = self.turn()

		winner = None
		if result == "win":
			if more_than_one_player: winner = board.players[1]
			else: winner = board.players[0]
		elif result == "loss" and more_than_one_player: winner = board.players[0]

		print(f'A palavra era "{board.word}". ' +
			  f'O jogador {winner.name} ganhou!' if winner is not None else "Perdeu!")

		return winner

	def serialize(self) -> Dict[str, Any]:
		return {}