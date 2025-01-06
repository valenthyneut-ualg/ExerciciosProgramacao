from AbstractGame.AbstractBoard import AbstractBoard
from typing import cast

class Board(AbstractBoard):
	def __init__(self):
		super().__init__("")
		self.underscoreWord = ""
		self.attempts = 10
		self.playedLetters: list[str] = []

	def play(self, letter: str = "") -> int:
		if letter in self.playedLetters: return 0
		else:
			self.playedLetters.append(letter)
			containsLetter = cast(str, self.state).count(letter) > 0
			if containsLetter:
				tempWord = cast(str, self.state)
				while True:
					letterIndex = tempWord.find(letter)
					if letterIndex == -1: break

					tempWord = tempWord[:letterIndex] + " " + tempWord[letterIndex + 1:]
					self.underscoreWord = self.underscoreWord[:letterIndex] + letter + tempWord[letterIndex + 1:]
				return 1
			else:
				return 2

	def inWinState(self):
		return cast(str, self.state) == self.underscoreWord

	def __str__(self):
		return self.underscoreWord