"""
@author Julian
@date Summer 2022
@brief The board class keeps track of the current board state, and handles
    adding moves to the board.

"""
from move import Move

NUM_ROWS = 3
NUM_COLS = 3
NUM_TOTAL_SPACES = NUM_ROWS * NUM_COLS

class Board:
    def __init__(self):
        self.numRows = NUM_ROWS
        self.numCols = NUM_COLS
        self.numTotalSpaces = self.numRows * self.numCols
        self.moves = [Move(i) for i in range(1,NUM_TOTAL_SPACES+1)]
        self.numMoves = 0


    def add_move(self, location, letter):
        self.moves[location-1] = Move(letter)
        self.numMoves += 1

    def is_valid_move(self, location):
        return(location is not None and
                location >= "1" and location <= str(self.numTotalSpaces) and 
                int(location) in range(1,self.numTotalSpaces) and 
                self.moves[int(location)-1].integer == 0)

    # ----- Code for Checking Game State -----

    def is_game_over(self):
        return(self.is_winner() or self._is_full())

    def is_winner(self):
        return(self._is_win_row() or self._is_win_col() or self._is_win_diag())

    def _is_full(self):
        return(self.numMoves == self.numTotalSpaces)

    def _is_tie(self):
        return(self._is_full() and not self.is_winner())

    #  since X is 1 and O is -1, we can use the sum of three "squares" to determine if there is a win
    def _row_as_int(self, row):
        start = (row-1) * self.numCols
        return(sum(map(int,self.moves[start:start+self.numCols])))

    def _is_win_row(self):
        for row in range(1,self.numRows+1):
            if abs(self._row_as_int(row)) == self.numCols:
                return(True)
        return(False)

    def _col_as_int(self, col):
        return(sum(map(int,self.moves[(col-1)::self.numCols])))

    def _is_win_col(self):
        for col in range(1,self.numCols+1):
            if abs(self._col_as_int(col)) == self.numRows:
                return(True)
        return(False)

    def _ltr_diag_as_int(self):
        return(int(self.moves[0]) + int(self.moves[4]) + int(self.moves[8]))

    def _rtl_diag_as_int(self):
        return(int(self.moves[2]) + int(self.moves[4]) + int(self.moves[6]))

    def _is_win_diag(self):
        return((self._ltr_diag_as_int() == self.numCols) or (self._rtl_diag_as_int() == self.numCols))


    # ----- Code for Printing -----

    def _row_as_str(self, row):
        start = (row-1) * self.numCols
        return(" | ".join(map(str,self.moves[start:start+self.numCols])))

    def _row_as_repr(self, row):
        start = (row-1) * self.numCols
        return(" | ".join(map(repr,self.moves[start:start+self.numCols])))

    def __str__(self):
        return("\n--------- \n".join(map(self._row_as_str,range(1,self.numRows+1))))

    # 'repr' is usually used for debugging. 
    # In this case, we use it to show the available moves if the user is having trouble.
    def __repr__(self):
        return("\n--------- \n".join(map(self._row_as_repr,range(1,self.numRows+1))))

