"""
@author Julian
@date Summer 2022
@brief Used to test the board class.

In testing, we want to check the total, not the implementation. 
Our tests should ensure the games are working correctly, it should not
enforce the current implementation.

I am using a complicated way to check for a winning game state. So it could
make sense to check each individual functions. But if I did, these tests should
be commented with the label "Remove these tests if failing" to make future coders
feel comfortable with changing the implementation.

In these tests I use a few board states and check that the states are working correctly.

"""

from board import Board

def test_empty():
    board = Board()
    assert board.is_game_over() == False, f"false expected, got: {board.is_game_over()}" 
    assert board.is_winner() == False, f"false expected, got: {board.is_game_over()}" 
    assert board._is_full() == False, f"false expected, got: {board.is_game_over()}"
    assert board._is_tie() == False, f"false expected, got: {board.is_game_over()}"

def test_diag():
    board = Board()
    board.add_move(1, "X")
    board.add_move(5, "X")
    board.add_move(9, "X")
    board.is_game_over()
    assert board.is_game_over() == True, f"true expected, got: {board.is_game_over()}"
    assert board.is_winner() == True, f"true expected, got: {board.is_game_over()}"
    assert board._is_tie() == False, f"false expected, got: {board.is_game_over()}"
    assert board._is_full() == False, f"true expected, got: {board.is_game_over()}"


def test_row():
    board = Board()
    board.add_move(4, "O")
    board.add_move(5, "O")
    board.add_move(6, "O")
    board.is_game_over()
    assert board.is_game_over() == True, f"true expected, got: {board.is_game_over()}"
    assert board.is_winner() == True, f"true expected, got: {board.is_game_over()}"
    assert board._is_tie() == False, f"false expected, got: {board.is_game_over()}"
    assert board._is_full() == False, f"true expected, got: {board.is_game_over()}"


def test_col():
    board = Board()
    board.add_move(1, "X")
    board.add_move(2, "X")
    board.add_move(3, "X")
    board.is_game_over()
    assert board.is_game_over() == True, f"true expected, got: {board.is_game_over()}"
    assert board.is_winner() == True, f"true expected, got: {board.is_game_over()}"
    assert board._is_tie() == False, f"false expected, got: {board.is_game_over()}"
    assert board._is_full() == False, f"true expected, got: {board.is_game_over()}"


def test_tie():
    board = Board()
    board.add_move(1, "X")
    board.add_move(2, "X")
    board.add_move(3, "O")
    board.add_move(4, "X")
    board.add_move(5, "O")
    board.add_move(6, "X")
    board.add_move(7, "O")
    board.add_move(8, "X")
    board.add_move(9, "O")
    assert board.is_game_over() == True, f"true expected, got: {board.is_game_over()}" 
    assert board.is_winner() == False, f"false expected, got: {board.is_game_over()}" 
    assert board._is_full() == True, f"true expected, got: {board.is_game_over()}"
    assert board._is_tie() == True, f"true expected, got: {board.is_game_over()}"


def test_full():
    board = Board()
    board.add_move(1, "X")
    board.add_move(2, "X")
    board.add_move(3, "O")
    board.add_move(4, "X")
    board.add_move(5, "O")
    board.add_move(6, "X")
    board.add_move(7, "O")
    board.add_move(8, "X")
    board.add_move(9, "O")
    assert board.is_game_over() == True, f"true expected, got: {board.is_game_over()}" 
    assert board.is_winner() == False, f"false expected, got: {board.is_game_over()}" 
    assert board._is_full() == True, f"true expected, got: {board.is_game_over()}"
    assert board._is_tie() == True, f"false expected, got: {board.is_game_over()}"


def test_almost_full():
    board = Board()
    board.add_move(1, "X")
    board.add_move(2, "X")
    board.add_move(3, "O")
    board.add_move(4, "X")
    board.add_move(5, "O")
    board.add_move(6, "X")
    board.add_move(7, "O")
    board.add_move(9, "O")
    assert board.is_game_over() == False, f"true expected, got: {board.is_game_over()}" 
    assert board.is_winner() == False, f"false expected, got: {board.is_game_over()}" 
    assert board._is_full() == False, f"true expected, got: {board.is_game_over()}"
    assert board._is_tie() == False, f"false expected, got: {board.is_game_over()}"


if __name__ == "__main__":
    test_empty()
    test_diag()
    test_row()
    test_col()
    test_tie()
    test_full()
