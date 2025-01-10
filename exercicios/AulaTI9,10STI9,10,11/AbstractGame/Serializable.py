from abc import ABC, abstractmethod
from typing import Dict, Any

class Serializable(ABC):
	@abstractmethod
	def serialize(self) -> Dict[str, Any]: pass

	def deserialize(self, data: Dict[str, Any]):
		for key, value in data.items():
			self.__setattr__(key, value)