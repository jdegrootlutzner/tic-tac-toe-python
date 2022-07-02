"""
@author Julian
@date Summer 2022
@brief The move class keeps track of the location and letter of a move.
    A move can be either X (1), O (-1), or empty (0). We take advantage of this
    class to figure out the board state and to provide pretty printing of the board.
"""


class Move:
    def __init__(self, letter):
        self.letter = str(letter)
        self.integer = self.to_integer()

    def to_integer(self):
        if self.letter == "X":
            return 1
        elif self.letter == "O":
            return -1
        else:
            return 0

    def __int__(self):
        return self.integer

    # 'repr' is usually used for debugging. 
    # In this case, we use it to show the available moves if the user is having trouble.
    def __repr__(self):
        return self.letter

    def __str__(self):
        return self.letter if self.integer != 0 else " "
