"""
@author Julian
@date Summer 2022
@brief The controller class creates the board and player objects, keeps track
    of the current player and turn, handles the game logic, and coordinates 
    the command line text.

"""
from player import Player
from board import Board

class Controller:
    def __init__(self):
        self.board = Board()
        self.playerOne = Player("Player One", "X")
        self.playerTwo = Player("Player Two", "O")
        self.currentPlayer = self.playerOne
        self.gamesPlayed = 0
    
    def play_game(self):
        while not self.board.is_game_over():
            print(self.board)
            location = self.get_valid_move()
            self.board.add_move(location, self.currentPlayer.get_letter())
            self.currentPlayer = self.get_next_player()
        print(self.board)
        self.gamesPlayed += 1
        self.print_game_over()
        self.print_score()
        self.reset_game()

    def reset_game(self):
        self.board = Board()
        self.currentPlayer = self.playerOne
        self.currentLetter = "X"

    def get_next_player(self):
        if self.currentPlayer == self.playerOne:
            return self.playerTwo
        else:
            return self.playerOne

    def start(self):
        self.introduce_game()
        self.play_game()

    def introduce_game(self):
        print('Welcome to Tic Tac Toe!')

    def get_valid_move(self):
        move = self.currentPlayer.prompt_move()
        while not self.board.is_valid_move(move):
            print("Invalid move. Try again. Here are the available moves:")
            print(repr(self.board))
            move = self.currentPlayer.prompt_move()
        return int(move)
    
    def print_game_over(self):
        print("Game over!")
        if self.board.is_winner():
            print("The winner is " + self.currentPlayer.name)
            self.currentPlayer.add_score()
        else:
            print("It's a tie!")

    def print_score(self):
        print("The score is:")
        print(self.playerOne.name + ": " + str(self.playerOne.get_score()))
        print(self.playerTwo.name + ": " + str(self.playerTwo.get_score()))
        print("Ties: " + str(self.gamesPlayed - self.playerOne.get_score() - self.playerTwo.get_score()))
        print("Games played: " + str(self.gamesPlayed))

