from typing import Dict, Any
from AbstractGame.Serializable import Serializable

class Player(Serializable):
	def __init__(self, name: str, symbol: str, score: int):
		self.name = name
		self.symbol = symbol
		self.score = score

	def __str__(self):
		return self.name

	def serialize(self) -> Dict[str, Any]:
		return {"name": self.name, "symbol": self.symbol, "score": self.score}