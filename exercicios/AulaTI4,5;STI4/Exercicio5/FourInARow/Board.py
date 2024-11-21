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

    @staticmethod
    def __fourInARowCheck(playersSlice: list[str]) -> tuple[True, str] | tuple[False, None]:
        oldPlayer = ""
        count = 0
        for i in range(len(playersSlice)):
            newPlayer = playersSlice[i]
            if oldPlayer != newPlayer:
                oldPlayer = newPlayer
                count = 1
            else:
                if newPlayer != " ": count += 1
            if count >= 4: return True, oldPlayer
        return False, None

    def __xyAxisCheck(self, axis: str, rowCoord: int, colCoord: int) -> tuple[True, str] | tuple[False, None]:
        if axis != "row" and axis != "col": raise ValueError("Eixo inválido! (tem de ser um de 'row' ou 'col')")

        xyList = []
        for i in range(8):
            xyList.append(self.state[rowCoord if axis == "row" else i][colCoord if axis == "col" else i])

        return self.__fourInARowCheck(xyList)

    def __diagonalCheck(self, axis: str, rowCoord: int, colCoord: int) -> tuple[True, str] | tuple[False, None]:
        if axis != "asc" and axis != "desc": raise ValueError("Eixo inválido! (tem de ser um de 'asc' ou 'desc')")

        offset = 0
        diagonal = []

        for i in range(8):
            # In my way of storing the board, the row coordinate increasing means we are going lower into the board, so
            # everytime we want to go higher in a diagonal, we decrease the coordinate, and vice-versa for if we want to
            # go lower.
            offsetRowCoord = rowCoord + (-offset if axis == "asc" else offset)
            offsetColCoord = colCoord + offset
            # Bounds checks so we don't get any weird "start from end of array" Python shenanigans
            if offsetRowCoord < 0 or offsetRowCoord > 7 or offsetColCoord < 0 or offsetColCoord > 7: break

            diagonal.append(self.state[offsetRowCoord][offsetColCoord])
            offset += 1

        offset = -1
        for i in range(8):
            offsetRowCoord = rowCoord + (-offset if axis == "asc" else offset)
            offsetColCoord = colCoord + offset
            if offsetRowCoord < 0 or offsetRowCoord > 7 or offsetColCoord < 0 or offsetColCoord > 7: break

            # Insert before the diagonal elements we already have because we're getting the lower elements of it
            diagonal.insert(0, self.state[offsetRowCoord][offsetColCoord])
            offset -= 1

        return self.__fourInARowCheck(diagonal)

    def inWinState(self, propagationPoint: (int, int)) -> tuple[True, str] | tuple[False, None]:
        rowCoord = propagationPoint[0]
        if rowCoord <= 0 or rowCoord > 8:
            raise ValueError("Nº da linha tem de estar entre 1 e 8. (inclusivo)")
        trueRowCoord = rowCoord - 1

        colCoord = propagationPoint[1]
        if colCoord <= 0 or colCoord > 8:
            raise ValueError("Nº da coluna tem de estar entre 1 e 8. (inclusivo)")
        trueColCoord = colCoord - 1

        xyAxes = ("row", "col")
        for axis in xyAxes:
            result, player = self.__xyAxisCheck(axis, trueRowCoord, trueColCoord)
            if result: return result, player

        diagAxes = ("asc", "desc")
        for axis in diagAxes:
            result, player = self.__diagonalCheck(axis, trueRowCoord, trueColCoord)
            if result: return result, player

        return False, None