from typing import Dict, Any
from json import loads

class Player:
	def __init__(self, name: str, symbol):
		self.name = name
		self.symbol = symbol

	def __str__(self):
		return self.name

	def serialize(self) -> Dict[str, Any]:
		return {"name": self.name, "symbol": self.symbol}

	@staticmethod
	def deserialize(rawData: str):
		try:
			parsedData = loads(rawData)

			hasValidName = hasattr(parsedData, "name") and parsedData.name is str
			hasValidSymbol = hasattr(parsedData, "symbol") and parsedData.symbol is str

			if hasValidName and hasValidSymbol: return Player(parsedData.name, parsedData.symbol)
		except AttributeError as error:
			print("Ocorreu um erro a ler um jogador!")
			print(error)