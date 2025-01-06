from AbstractGame.AbstractBoard import AbstractBoard
from typing import cast

class Board(AbstractBoard):
	def __init__(self):
		super().__init__("")
		self.underscoreWord = ""
		self.attempts = 10
		self.playedLetters: list[str] = []

	def initWord(self, word: str):
		self.state = word
		self.underscoreWord = "_" * len(word)

	def play(self, letter: str = "") -> int:
		if letter in self.playedLetters: return 0
		else:
			self.playedLetters.append(letter)
			containsLetter = cast(str, self.state).count(letter) > 0
			if containsLetter:
				tempWord = cast(str, self.state)
				while tempWord.count(letter) > 0:
					tempWordList = [char for char in tempWord]
					tempUnderscoreWordList = [char for char in self.underscoreWord]

					letterIndex = tempWordList.index(letter)
					tempWordList[letterIndex] = " "
					tempUnderscoreWordList[letterIndex] = letter

					tempWord = "".join(tempWordList)
					self.underscoreWord = "".join(tempUnderscoreWordList)
				return 1
			else:
				self.attempts -= 1
				return 2

	def inWinState(self):
		return cast(str, self.state) == self.underscoreWord

	def __str__(self):
		return self.underscoreWord + f'\nTentativas restantes: {self.attempts}'