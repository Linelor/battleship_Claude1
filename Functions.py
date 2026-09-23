#
# Functions
#
from random import randint


#Function to print the board
def print_board(board):
    print("  " + " ".join(str(col) for col in range(len(board[0]))))
    for row_num, row in enumerate(board):
        print(str(row_num) + " " + " ".join(row))
       
#Function to place a ship of ship_size length
def place_ship(board,ship_size,ship_char,blank_char):
    #Tries to place the ship 50 times, if it fails it gives up.
    max_tries = 50
    tries = 0
    ship_created = False
    
    while tries < max_tries and ship_created == False:
        #sets the starting point for the ship
        new_row = randint(0, len(board)-1)
        new_col = randint(0, len(board)-1)
        #print ("new_row="+str(new_row)+", new_col="+str(new_col)) ####
        #sets the direction of the ship
        #1: row-1, 2: row+1, 3:col-1, 4:col+1
        row_delt = 0
        col_delt = 0
        direc = randint(1,4)
        
        if direc == 1: row_delt = -1
        elif direc == 2: row_delt = 1
        elif direc == 3: col_delt = -1
        elif direc == 4: col_delt = 1
        else: print("There is an issue with the random direction")

        # Checks if ship is clear to place
        collision = False # sets collision variable to false
        for each_cell in range(ship_size):
            cur_row = new_row+row_delt*each_cell
            cur_col = new_col+col_delt*each_cell
            #print("cur_row="+str(cur_row)+", cur_col="+str(cur_col))####
            if 0 <= cur_row < len(board) and 0 <= cur_col < len(board):
                if board[cur_row][cur_col] == blank_char:
                    ignore_this=1
                else:
                    #print("collision")
                    collision = True
            else:
                #print("out of bounds")
                collision = True

        if collision == False:
            for each_cell in range(ship_size):
                cur_row = new_row+row_delt*each_cell
                cur_col = new_col+col_delt*each_cell
                board[cur_row][cur_col] = ship_char
                ship_created = True

        tries += 1
        if tries == max_tries:
            print("Max attempts exceeded for ship size" + str(ship_size))
    #print_board(board)####
    #print(board)####
        
