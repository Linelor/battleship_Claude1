from copy import deepcopy #required to copy elements of the board
from Functions import *

#Initializing the board
board = []
board_dim = 10
turns = 40
blank_char = (".")
miss_char = ("O")
hit_char = ("X")
for x in range(board_dim):
    board.append([blank_char] * board_dim)

player_board = deepcopy(board)
board_key = deepcopy(board)


#Placing the ships
ships = {
    "A": ("Aircraft Carrier", 5),
    "B": ("Battleship", 4),
    "S": ("Submarine", 3),
    "D": ("Destroyer", 3),
    "P": ("Patrol Boat", 2),
}
ship_hits_left = {}
for ship_char, (ship_name, ship_size) in ships.items():
    place_ship(board_key,ship_size,ship_char,blank_char)
    ship_hits_left[ship_char] = ship_size

#Beginning Greeting
print("Let's play Battleship!")
print("Sink all " + str(len(ships)) + " ships in " + str(turns) + " shots.")
print("Rows and columns are numbered 0 to " + str(board_dim - 1) + ".")
print("")


#Main Game
turn = 0
while turn < turns:
    # Asks user for their guess
    print("Turn: "+str(turn+1)+" of "+str(turns))
    print_board(player_board)
    while True:
        try:
            guess_row = int(input("Guess Row:"))
            guess_col = int(input("Guess Col:"))
            break
        except ValueError:
            print("Oops, that's not a valid number!")

    # Off-board and repeat shots don't use up a turn
    if ((guess_row < 0 or guess_row >= board_dim) or
        (guess_col < 0 or guess_col >= board_dim)):
        print("Oops, that's not even in the ocean!")
        continue
    elif (player_board[guess_row][guess_col] == hit_char or
        player_board[guess_row][guess_col] == miss_char):
        print("You already shot there!")
        continue

    turn += 1
    target = board_key[guess_row][guess_col]
    if target == blank_char:
        print("You missed!")
        player_board[guess_row][guess_col] = miss_char
    else:
        print("HIT!!")
        player_board[guess_row][guess_col] = hit_char
        ship_hits_left[target] -= 1
        if ship_hits_left[target] == 0:
            print("You sunk my " + ships[target][0] + "!")
    print("")

    if sum(ship_hits_left.values()) == 0:
        print_board(player_board)
        print("Congratulations! You sunk all my ships in " + str(turn) + " shots!")
        break
else:
    print("Game Over! You're out of shots.")
    ships_left = [ships[c][0] for c in ship_hits_left if ship_hits_left[c] > 0]
    print("Ships still afloat: " + ", ".join(ships_left))
    print("Here's where they were:")
    print_board(board_key)
