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

    def __xyAxisCheck(self, axis: str, rowCoord: int, colCoord: int) -> tuple[True, str] | tuple[False, None]:
        if axis != "row" and axis != "col": raise ValueError("Eixo inválido! (tem de ser um de 'row' ou 'col')")

        oldPlayer = 0
        count = 0
        for i in range(8):
            newPlayer = self.state[rowCoord if axis == "row" else i][colCoord if axis == "col" else i]
            if newPlayer != " ":
                if oldPlayer != newPlayer:
                    oldPlayer = newPlayer
                    count = 1
                else:
                    count += 1
                if count >= 4: return True, oldPlayer
        return False, None

    def __diagonalCheck(self, axis: str, rowCoord: int, colCoord: int) -> tuple[True, str] | tuple[False, None]:
        if axis != "asc" and axis != "desc": raise ValueError("Eixo inválido! (tem de ser um de 'asc' ou 'desc')")

        offset = 0
        diagonal = []

        for i in range(8):
            offsetRowCoord = rowCoord + (-offset if axis == "asc" else offset)
            offsetColCoord = colCoord + offset
            # We're outside the range of the grid, bail
            if offsetRowCoord < 0 or offsetRowCoord > 7 or offsetColCoord < 0 or offsetColCoord > 7: break

            diagonal.append(self.state[offsetRowCoord][offsetColCoord])
            offset += 1

        offset = -1
        for i in range(8):
            offsetRowCoord = rowCoord + (-offset if axis == "asc" else offset)
            offsetColCoord = colCoord + offset
            if offsetRowCoord < 0 or offsetRowCoord > 7 or offsetColCoord < 0 or offsetColCoord > 7: break

            diagonal.insert(0, self.state[offsetRowCoord][offsetColCoord])
            offset -= 1

        oldPlayer = ""
        count = 0
        for i in range(len(diagonal)):
            curPlayer = diagonal[i]
            if curPlayer != " ":
                if oldPlayer != curPlayer:
                    oldPlayer = curPlayer
                    count = 1
                else:
                    count += 1
            if count >= 4: return True, oldPlayer
        return False, None

    def inWinState(self, propagationPoint: (int, int)) -> tuple[True, str] | tuple[False, None]:
        rowCoord = propagationPoint[0]
        if rowCoord <= 0 or rowCoord > 8:
            raise ValueError("Nº da linha tem de estar entre 1 e 8. (inclusivo)")
        trueRowCoord = rowCoord - 1

        colCoord = propagationPoint[1]
        if colCoord <= 0 or colCoord > 8:
            raise ValueError("Nº da coluna tem de estar entre 1 e 8. (inclusivo)")
        trueColCoord = colCoord - 1

        result, player = self.__xyAxisCheck("row", trueRowCoord, trueColCoord)
        if result: return result, player

        result, player = self.__xyAxisCheck("col", trueRowCoord, trueColCoord)
        if result: return result, player

        result, player = self.__diagonalCheck("asc", trueRowCoord, trueColCoord)
        if result: return result, player

        result, player = self.__diagonalCheck("desc", trueRowCoord, trueColCoord)
        if result: return result, player

        return False, None