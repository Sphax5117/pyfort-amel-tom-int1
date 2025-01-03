import random

def display_grid(grid):
    for i in range(len(grid)):
        print(" | ".join(grid[i]))
        print("-" * 9)

gird = [["","",""],
        ["","",""]
        ["","",""]
        ]
print (display_grid(grid))
"""
def check_victory(grid, symbol):
    row = 3
    col = 3
    # Check rows for victory
    for i in range(row) :
        cpt = 0
        for j in range(col):
            if symbol == grid[i][j]:
                cpt += 1
        if cpt == 3 :
            return True
    # Check main diagonal for victory
    cpt1 = 0
    for i in range (row):
        if symbol == grid[i][i]:
            cpt1 += 1
    if cpt1 == 3 :
        return True
    # Check secondary diagonal for victory
    cpt2 = 0
    for i in range(row):
        if symbol == grid[i][row - i - 1]:
            cpt2 += 1
    if cpt2 == 3:
        return True
    # Check columns for victory
    for j in range(col) :
        cpt3 = 0
        for i in range (row):
            if symbol == grid [i][j] :
                cpt3 += 1
        if cpt3 == 3 :
            return True
    return False

def master_move(grid, symbol):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == ' ':
                grid[i][j] = symbol
                if check_victory(grid, symbol) == True :
                    return (i, j)
                grid[i][j] = ' '
    #### pas la suite


def player_turn(grid):
    while True:
        try:
            row = int(input("Enter a number between (0,1,2) for the row : "))
            col = int(input("Enter a number between (0,1,2) for the column : "))

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Row and column must be between 0 and 2.")
                continue

            # Check if the cell is empty
            if grid[row][col] == ' ':
                grid[row][col] = 'X'  # Place the player's symbol (X)
                break  # Exit the loop once a valid move is made
            else:
                print("The cell is already occupied. Choose another cell.")

def tictactoe_game() :
    gird = [[" "," "," "],
            [" "," "," "]
            [" "," "," "]
            ]
    for i in range (5) :
        player_turn(grid)
        if check_result(grid) == True:
            return True

        master_turn(grid)
        if check_result(grid) == True:
            return False
    return None
"""
