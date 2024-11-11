class Board:
    """Holds information regarding game state, and methods to interact with it."""
    def __init__(self):
        self.state = []
        self.winStates = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 4, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        # Fill board with empty positions
        for i in range(9): self.state.insert(i, " ")

    def display(self):
        print(f'{self.state[0]} | {self.state[1]} | {self.state[2]}')
        print('---------')
        print(f'{self.state[3]} | {self.state[4]} | {self.state[5]}')
        print('---------')
        print(f'{self.state[6]} | {self.state[7]} | {self.state[8]}')
