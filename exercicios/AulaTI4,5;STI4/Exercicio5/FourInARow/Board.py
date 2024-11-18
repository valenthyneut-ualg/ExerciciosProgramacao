class Board:
    """Holds information regarding game state and methods to interact with it"""
    def __init__(self):
        self.state = []

        # Fill board with empty positions
        for i in range(8):
            self.state.insert(i, [" "] * 8)

    def display(self):
        for row in self.state:
            rowString = ""
            zeroIRowLen = len(row) - 1

            for i in range(zeroIRowLen + 1):
                col = row[i]
                rowString += f' {col} '

                if i != zeroIRowLen: rowString += '|'
            print(rowString)

        numString = ""

        for i in range(8):
            numString += f' {i + 1}  '
        print(numString)

    def play(self, player: str, column: int) -> tuple[int, int]:
        if column <= 0 or column > 8: raise ValueError("Nº da coluna tem de estar entre 1 e 8. (inclusivo)");
        trueColumn = column - 1

        lastEmptyRow = -1
        for i in range(8):
            if self.state[i][trueColumn].strip() == "": lastEmptyRow = i

        if lastEmptyRow == -1: raise ValueError("A coluna já está preenchida.")
        self.state[lastEmptyRow][trueColumn] = player

        return lastEmptyRow + 1, column

    def inWinState(self, propagationPoint: (int, int)) -> tuple[True, str] | tuple[False, None]:
        rowCoord = propagationPoint[0]
        if rowCoord <= 0 or rowCoord > 8:
            raise ValueError("Nº da linha tem de estar entre 1 e 8. (inclusivo)")
        trueRowCoord = rowCoord - 1

        colCoord = propagationPoint[1]
        if colCoord <= 0 or colCoord > 8:
            raise ValueError("Nº da coluna tem de estar entre 1 e 8. (inclusivo)")
        trueColCoord = colCoord - 1

        # Horizontal win check, traverse across the
        # columns, counting number of equal player
        # characters. If it reaches four, win

        oldPlayer = ""
        count = 0
        for i in range(8):
            newPlayer = self.state[trueRowCoord][i]
            if newPlayer.strip() != "":
                if oldPlayer != newPlayer:
                    oldPlayer = newPlayer
                    count = 1
                else:
                    count += 1
            if count >= 4: return True, oldPlayer

        # Vertical win check, traverse across the
        # current column vertically, (...)

        oldPlayer = ""
        count = 0
        for i in range(8):
            newPlayer = self.state[i][trueColCoord]
            if newPlayer.strip() != "":
                if oldPlayer != newPlayer:
                    oldPlayer = newPlayer
                    count = 1
                else:
                    count += 1
            if count >= 4: return True, oldPlayer

        # Ascending diagonal checks
        offset = 0
        diagonal = []

        # Traverse across the grid in an upwards fashion
        for i in range(8):
            try:
                curPoint = self.state[trueRowCoord - offset][trueColCoord + offset]
                diagonal.append(curPoint)
            except IndexError: break
            offset = offset + 1

        offset = -1
        for i in range(8):
            try:
                curPoint = self.state[trueRowCoord - offset][trueColCoord + offset]
                diagonal.insert(0, curPoint)
            except IndexError: break
            offset = offset - 1

        oldPlayer = ""
        count = 0
        for i in range(len(diagonal)):
            curPlayer = diagonal[i]
            if curPlayer.strip() != "":
                if oldPlayer != curPlayer:
                    oldPlayer = curPlayer
                    count = 1
                else:
                    count += 1
            if count >= 4: return True, oldPlayer

        return False, None