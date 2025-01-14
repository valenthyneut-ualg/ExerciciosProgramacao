from typing import Dict

from AbstractGame.Serializable import Serializable


class Player(Serializable):
	def __init__(self, name: str, symbol: str, game_scores: Dict[str, int] = {}, total_score: int = 0):
		self.name = name
		self.symbol = symbol
		self.game_scores = game_scores
		self.total_score = total_score

	def __str__(self) -> str: return self.name

	def serialize(self) -> Dict[str, int]:
		return {
			"name": self.name,
			"symbol": self.symbol,
			"game_scores": self.game_scores,
			"total_score": self.total_score
		}