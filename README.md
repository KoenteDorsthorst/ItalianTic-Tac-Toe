# Italian Tic-Tac-Toe


### What is Italian Tic-Tac-Toe?

Italian tic-tac-toe is similar to the well known tic-tac-toe game. The game is played by two players on a 3 by 3 grid. Each player represents a shape, either a cross or a circle. Players take turns placing their shape on a tile in the three by three grid. Players can only place their shape in an unoccupied tile. The first player to get three of their shapes in a row (horizontal, vertical or diagonal) wins the game.

The Italian version of this game works a little different. In this version the first three turns of each player is the same. Take turns placing shapes on the grid. After each player has placed three of their shapes onto the grid the second phase of the game begins. Players now take turns sliding their pieces onto unoccupied tiles. Again, the first player to get three of their shapes in a row (horizontal, vertical or diagonal) wins the game.

### Sliding rules

The sliding that happens when both players have three of their shapes on the board has a set of rules that you have to follow:

- You can only slide a shape to an unoccupied tile.
- Shapes can only slide to locations that are directly connected to them (this includes diagonal connection)

### Interesting sliding tips

The tile on the middle of the board directly connects to every other tile. This means that every tile can slide to and from the middle.

Shapes in a corner have more win posibilities than shapes at the middle of an edge. Keep this in mind when trying to win by sliding. 

Do not only think of your own moves when sliding, keep in mind that the opponent has to slide right after you. You can use this to your advantage by sliding your shapes in such a way that the only moves that your opponent can make will be disadvantageous for them.



## Program


### What will I be making

In this project I will be making a console based version of Italian tic-tac-toe. This program will be writen in python. This version of Italian tic-tac-toe will have multiple features listed below:

- A welcoming message when starting the application
- A prompt for the names of both players
- Both gameplay phases (placing shapes and sliding shapes)
- Error handling when users use invalid or rule-breaking moves
- An endscreen where the winner will be displayed
- A way to play another round after one has finished

### Possible features

These are extra features that I might add:

- A computer opponent that you can play the game with
- A way to also play the original tic-tac-toe (and maybe more variations?)
- Different shapes you can select

