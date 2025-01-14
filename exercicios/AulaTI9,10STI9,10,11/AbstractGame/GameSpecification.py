from typing import TypedDict

from AbstractGame.AbstractController import AbstractController


class GameSpecification(TypedDict):
	title: str
	min_player_count: int
	controller: AbstractController