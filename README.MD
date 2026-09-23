# Python Battleship

A command-line Battleship game in Python, based on the Codecademy project.

## Requirements

Python 3. No other packages are needed.

## Running the game

```
python3 Main.py
```

## How to play

The computer hides 5 ships on a 10×10 grid. Your goal is to sink all of them before you run out of shots.

| Ship             | Length |
|------------------|--------|
| Aircraft Carrier | 5      |
| Battleship       | 4      |
| Submarine        | 3      |
| Destroyer        | 3      |
| Patrol Boat      | 2      |

Ships are placed at random, horizontally or vertically, and never overlap.

Each turn, the game shows your board and asks for a row and a column. Rows and columns are numbered 0 to 9, as labelled along the edges of the board:

```
  0 1 2 3 4 5 6 7 8 9
0 . . . . . . . . . .
1 . . . O . . . . . .
2 . . . X X . . . . .
...
```

| Symbol | Meaning        |
|--------|----------------|
| `.`    | Not shot yet   |
| `O`    | Miss           |
| `X`    | Hit            |

The game tells you when you hit a ship, and names it when you sink it ("You sunk my Battleship!").

- You have **40 shots**.
- A shot off the board, or at a square you've already tried, doesn't use up a turn.
- If you type something that isn't a number, the game asks again.

**You win** by sinking all 5 ships. **You lose** if you run out of shots; the game then lists the ships still afloat and shows where every ship was.

## Changing the difficulty

Edit `turns = 40` near the top of `Main.py` to give yourself more or fewer shots.
