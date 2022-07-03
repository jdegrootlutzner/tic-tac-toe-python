# tic-tac-toe-python
A command line version of tic tac toe implemented in Python. 


## 

Using Python3 

To run the game from the command line:
```
python3 main.py
```

To run the test from the command line:
```
python3 main.py
```


### Planning my Code

Before I started coding, I came up with a plan. I walked through each step of a game to figure out the scope of the project, which helped me figure out what data I needed to track and what problems I may encounter. As I did this, I also drafted a version of my classes and their responsibilities.


#### Walking through a game:
1. Prompt “Welcome to Tic Tac Toe!“
2. Prompt “	Who is playing?”
	1. enter name (or computer)
3. Play a game
	1. create a board
	2. Chose the first player randomly
	3. Keep track of who’s turn it is and 
	4. Loop until game is over
		1. show board
		2. ask for move from player
		3. confirm legal move or prompt player again
		4. add move
		5. update win state 
4. Update score and ask to play again with same players or new players?


#### Classes

##### Move
- X or O

##### Board
- Keeps track of moves
- Print board
- Add move
	- Checks legal move
	- Return win state
		- check depends on how I keep track of a move

##### Controller
-  keep track of total games played 
	-  and current games between players
- sets up and keeps track of players
	- Prompts human vs human or computer vs computer?
	- prints player's scores
		- and keeps track of ties?
- creates a board
- starts a game, keeps track of turns, and prompts players for moves

##### Player
- Keeps track of name
- Keeps track of score
- Ask for move





