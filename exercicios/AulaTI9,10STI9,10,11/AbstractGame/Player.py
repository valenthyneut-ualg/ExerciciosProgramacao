from typing import Dict, Any
from AbstractGame.Serializable import Serializable

class Player(Serializable):
	def __init__(self, name: str, symbol):
		self.name = name
		self.symbol = symbol

	def __str__(self):
		return self.name

	def serialize(self) -> Dict[str, Any]:
		return {"name": self.name, "symbol": self.symbol}