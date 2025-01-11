from typing import Dict, Any
from AbstractGame.Serializable import Serializable

class Player(Serializable):
	def __init__(self, name: str, symbol: str, score: Dict[str, int], totalScore: int):
		self.name = name
		self.symbol = symbol
		self.score = score
		self.totalScore = totalScore

	def __str__(self):
		return self.name

	def serialize(self) -> Dict[str, Any]:
		return {"name": self.name, "symbol": self.symbol, "score": self.score, "totalScore": self.totalScore}
