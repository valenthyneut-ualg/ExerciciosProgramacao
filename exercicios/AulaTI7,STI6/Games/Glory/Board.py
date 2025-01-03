from typing import Dict

class Board:
    def __init__(self, playerCount: int):
        self.playerPositions: list[int] = [1] * playerCount

        self.specialSpaces: Dict[int, tuple[str, str, int | None, str]] = {
            1:  ("b", "none",   None, ""),

            8:  ("M+", "move",   10,   "És teleportado para a posição 18!"),
            15: ("M-", "move",   -3,   "Oops! És arrastado 3 posições de volta."),
            23: ("M+", "move",   4,    "Boa! Avança mais 4 posições!"),
            28: ("S",  "skip",   None, "Má sorte! Salta a tua próxima jogada."),
            33: ("R",  "reroll", None, "Atira os dados de novo para te moveres mais!"),
            39: ("M+", "move",   8,    "Altamente! Avança mais 8 posições!"),
            40: ("S",  "skip",   None, "Que pena! Salta a tua próxima jogada."),
            48: ("M-", "move",   -11,  "És lançado 11 posições de volta."),
            54: ("R",  "reroll", None, "Atira os dados de novo para avançares um pouco mais!"),
            56: ("M-", "move",   -8,   "És arrastado 8 posições de volta."),
            63: ("D",  "move",   -62,  "Morreste! Começa do início."),

            64: ("g", "none",   None, "")
        }

    def move(self, player: int, spaces: int):
        newPos = self.playerPositions[player] + spaces
        if newPos > 64: newPos = 64 - (newPos - 64)
        if newPos < 1: raise ValueError("Quantidade de espaços inválida!")

        self.playerPositions[player] = newPos

        specialSpace = self.specialSpaces.get(newPos)
        if specialSpace is not None:
            return specialSpace[1], specialSpace[2], specialSpace[3]
        else: return None, None, None

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