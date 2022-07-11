"""
@author Julian
@date Summer 2022
@brief The player class keeps track of the players name, letter, and score.
    The player class also prompts the user for a move.

"""

class Player:
    def __init__(self, name, letter = None):
        self.name = name
        self.letter = letter
        self.score = 0

    def __str__(self):
        return self.name

    
    def prompt_move(self):
        return input(f'{ self.name }, enter your move:\n' )

    # ---- get and set current letter ----

    def get_letter(self):
        return self.letter

    def set_letter(self, letter):
        self.letter = letter

    # ----- get and set score -----

    def get_score(self):
        return self.score
    
    def add_score(self):
        self.score += 1
    
    def reset_score(self):
        self.score = 0

    
    
