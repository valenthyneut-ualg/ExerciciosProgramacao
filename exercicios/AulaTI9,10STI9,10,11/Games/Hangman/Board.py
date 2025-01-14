from typing import Literal, Dict, Any

from AbstractGame.AbstractBoard import AbstractBoard
from AbstractGame.Player import Player


class Board(AbstractBoard):
	def __init__(self, players: tuple[Player, ...]):
		super().__init__(players[:2])
		self.word = ""
		self.underscore_word = ""
		self.attempts = 10
		self.played_letters: list[str] = []
		self.prefill_characters = ["-", " ", "'", "\""]

	def init_word(self, word: str):
		self.word = word
		self.underscore_word = "_" * len(self.word)

		for i in range(len(self.word)):
			cur_char = word[i]
			if cur_char in self.prefill_characters:
				self.underscore_word = self.underscore_word[:i] + cur_char + self.underscore_word[i + 1:]

	def play(self, letter: str = "") -> Literal["repeated", "correct", "incorrect"]:
		if letter in self.played_letters: return "repeated"
		else:
			self.played_letters.append(letter)
			contains_letter = self.word.count(letter) > 0
			if contains_letter:
				temp_word = self.word
				while temp_word.count(letter) > 0:
					temp_word_list = [char for char in temp_word]
					temp_underscore_word_list = [char for char in self.underscore_word]

					letter_index = temp_word.index(letter)
					temp_word_list[letter_index] = " "
					temp_underscore_word_list[letter_index] = letter

					temp_word = "".join(temp_word_list)
					self.underscore_word = "".join(temp_underscore_word_list)
				return "correct"
			else:
				self.attempts -= 1
				return "incorrect"

	def current_state(self) -> str:
		if self.attempts <= 0: return "loss"
		elif self.word == self.underscore_word: return "win"
		else: return "ongoing"

	def __str__(self) -> str:
		return (self.underscore_word
				+ f'\nErros restantes: {self.attempts}'
				+ f'\nLetras adivinhadas: {", ".join(self.played_letters)}')

	def serialize(self) -> Dict[str, Any]:
		return {
			"word": self.word,
			"underscore_word": self.underscore_word,
			"attempts": self.attempts,
			"played_letters": self.played_letters
		}