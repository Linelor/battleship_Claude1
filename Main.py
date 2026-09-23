from random import randint
from copy import deepcopy #required to copy elements of the board
from Functions import *
 
#Initializing the board
board = []
board_dim = 10
turns = 4
blank_char = (".")
ship_char = ("S")
miss_char = ("O")
hit_char = ("X")
for x in range(board_dim):
    board.append([blank_char] * board_dim)
 
player_board = deepcopy(board)
board_key = deepcopy(board)


#Placing the ships
place_ship(board_key,5,"A",blank_char) #Aircraft Carrier
place_ship(board_key,4,"B",blank_char) #Battleship
place_ship(board_key,3,"S",blank_char) #Submarine
place_ship(board_key,3,"D",blank_char) #Destroyer
place_ship(board_key,2,"P",blank_char) #Patrol Boat




# Remove this after fixing guns
ship_row = randint(0, len(board) - 1)
ship_col = randint(0, len(board[0]) - 1)
print (ship_row)
print (ship_col)
 
#Beginning Greeting
print ("Let's play Battleship!")
print_board(board_key) ### for debugging
print("")
 
                
#Main Game
for turn in range(turns):
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


    if ((guess_row < 0 or guess_row >= board_dim) or
        (guess_col < 0 or guess_col >= board_dim)):
        print("Oops, that's not even in the ocean!")
    elif (player_board[guess_row][guess_col] == hit_char or
        player_board[guess_row][guess_col] == miss_char):
        print("You already shot there!")
    elif(board_key[guess_row][guess_col] == blank_char):
        print("You missed!")
        player_board[guess_row][guess_col] = miss_char
    else:
        print("HIT!!")
        player_board[guess_row][guess_col] = hit_char
        ## Need to implement way to see if all ships were hit


    

        #print ("Congratulations! You sunk my battleship!")
        #break
  
            #if turn == 3:
              #  print ("Game Over")
        # Print (turn + 1) here!
        #print (str(turn+1))
        #print_board(board)
