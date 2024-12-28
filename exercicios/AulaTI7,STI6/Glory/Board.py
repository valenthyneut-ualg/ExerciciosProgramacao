from typing import Dict

class Board:
    def __init__(self):
        self.playerPositions: list[int] = [1, 1]

        self.specialSpaces: Dict[int, tuple[str, str, int | None, str]] = {
            1:  ("b", "none",   None, ""),

            8:  ("M", "move",   10,   "You got teleported to the 18th place!"),
            15: ("B", "move",   -3,   "Backtrack 3 places."),
            23: ("M", "move",   4,    "Move forward 4 spaces!"),
            28: ("S", "skip",   None, "Tough luck! Skip your next turn."),
            33: ("R", "reroll", None, "Reroll to move forward some more!"),
            39: ("M", "move",   9,    "Move forward 9 spaces!"),
            40: ("S", "skip",   None, "Too bad! Skip your next turn."),
            48: ("M", "move",   -11,  "You get launched back eleven places."),
            54: ("R", "reroll", None, "Reroll to advance some more!"),
            56: ("M", "move",   -8,   "You get pulled back to the 48th place."),
            63: ("D", "move",   -62,  "You died! Start from the first place."),

            64: ("g", "none",   None, "")
        }

    def move(self, player: int, spaces: int):
        if spaces < 1: raise ValueError("Invalid amount of spaces to move!")
        newPos = self.playerPositions[player] + spaces
        if newPos > 64: newPos = 64 - (newPos - 64)

        self.playerPositions[player] = newPos

    def display(self):
        occupiedSpaces: list[int] = []
        for key in self.specialSpaces: occupiedSpaces.append(key)
        for position in self.playerPositions:
            if position not in occupiedSpaces: occupiedSpaces.append(position)
        occupiedSpaces.sort()
        occupiedSpacesLength = len(occupiedSpaces)

        symbols: list[str] = []
        for space in occupiedSpaces:
            specialSpace = self.specialSpaces.get(space)
            if specialSpace is None: symbols.append("")
            else: symbols.append(specialSpace[0])
            # No need to sort here since we're getting our indices from an already sorted list.

        playerPositions: list[list[str]] = []
        for index in range(len(self.playerPositions)):
            position = self.playerPositions[index]
            playerPositions.insert(index, [""] * occupiedSpacesLength)
            playerPositions[index][occupiedSpaces.index(position)] = str(index + 1)

        # what the hell
        boardTable = playerPositions + [occupiedSpaces] + [symbols]
        boardString = ""

        for row in boardTable:
            boardString += ("{: <3} " * len(row)).format(*row) + "\n"

        print(boardString)