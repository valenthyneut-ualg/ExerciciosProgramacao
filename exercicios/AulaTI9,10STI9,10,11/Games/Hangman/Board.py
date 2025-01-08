from json import loads

from AbstractGame.AbstractBoard import AbstractBoard
from typing import cast, Dict, Any


class Board(AbstractBoard):
	def __init__(self):
		super().__init__("", [])
		self.underscoreWord = ""
		self.attempts = 10
		self.playedLetters: list[str] = []
		self.prefillCharacters = ["-", " ", "'", "\""]

	def initWord(self, word: str):
		self.state = word
		self.underscoreWord = "_" * len(word)

		for i in range(len(word)):
			curChar = word[i]
			if curChar in self.prefillCharacters:
				self.underscoreWord = self.underscoreWord[:i] + curChar + self.underscoreWord[i + 1:]

	def play(self, letter: str = "") -> str:
		if letter in self.playedLetters: return "repeated"
		else:
			self.playedLetters.append(letter)
			containsLetter = cast(str, self.state).count(letter) > 0
			if containsLetter:
				tempWord = cast(str, self.state)
				while tempWord.count(letter) > 0:
					tempWordList = [char for char in tempWord]
					tempUnderscoreWordList = [char for char in self.underscoreWord]

					letterIndex = tempWord.index(letter)
					tempWordList[letterIndex] = " "
					tempUnderscoreWordList[letterIndex] = letter

					tempWord = "".join(tempWordList)
					self.underscoreWord = "".join(tempUnderscoreWordList)
				return "correct"
			else:
				return "incorrect"

	def inWinState(self) -> bool:
		return cast(str, self.state) == self.underscoreWord

	def __str__(self):
		return self.underscoreWord + f'\nErros restantes: {self.attempts}'

	def serialize(self) -> Dict[str, Any]:
		return {
			"state": self.state,
			"underscoreWord": self.underscoreWord,
			"attempts": self.attempts,
			"playedLetters": self.playedLetters
		}

	@staticmethod
	def deserialize(rawData: str, players = None):
		try:
			parsedData = loads(rawData)

			hasValidState = hasattr(parsedData, "state") and parsedData.state is str
			hasValidUnderscoreWord = hasattr(parsedData, "underscoreWord") and parsedData.underscoreWord is str
			hasValidAttempts = hasattr(parsedData, "attempts") and parsedData.attempts is int
			hasValidPlayedLetters = hasattr(parsedData, "playedLetters") and parsedData.playedLetters is list[str]

			if hasValidState and hasValidUnderscoreWord and hasValidAttempts and hasValidPlayedLetters:
				board = Board()

				board.state = parsedData.state
				board.underscoreWord = parsedData.underscoreWord
				board.attempts = parsedData.attempts
				board.playedLetters = parsedData.playedLetters
		except AttributeError as error:
			print("Ocorreu um erro a ler um save do jogo!")
			print(error)