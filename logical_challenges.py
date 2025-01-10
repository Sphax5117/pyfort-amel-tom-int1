import random

'''
Fort Boyard Project 
Authors : Amel Boulhamane and Tom Hausmann
Role of this file : 
This file aims at providing the logical challenges for the Fort Boyard Game.
It encompass the three challenges (Tic Tac Toe, Battle game and Nim Game), and chose between them randomly.
All functions have been commented.
'''


# we'll define 0 for the player, 1 for the game master
def next_player(player):
    if player == 1:
        return 0
    elif player == 0:
        return 1
    else:
        return ("There was an error in the player naming")

def empty_grid():
    grid = [[" " for i in range(3)] for i in range(3)]
    return grid

def display_grid(grid, message):
    print(message)
    for row in grid:
        print(" | ".join(row))
    print("——————————")

def ask_position():
    """
    This was our first attempt at securing and sanitazing the data, but it didn't handle it well.
    r,c = eval(input("Enter the position in the format row,column (1,2 or 3) : "))
    r,c = r-1,c-1
    while r < 0 or r > 2 or c < 0 or c > 2:
        r, c = eval(input("Enter the position in the format row,column : (1,2 or 3)"))
        r, c = r - 1, c - 1
    return (r,c)
    """
    while True:
        try:

            user_input = input("Enter the position in the format row,column (for example:  2,2 or 3,3): ")
            r, c = user_input.split(",") ## instead of evaluating, we split the data input by the user
            r = int(r.strip()) # strip allows us to remove the empty spaces in the given inpouts
            c = int(c.strip())
            if r in {1, 2, 3} and c in {1, 2, 3}: #we check if row and columns are well in 1,2 or 3
                break
            else:
                print("Invalid input. Both row and column must be 1, 2, or 3.")
        except ValueError:
            print("Please enter two numbers separated by a comma.")
    return (r-1,c-1) #We then convert to index

def initialize():
    playerBoats = empty_grid()
    boat1 = ask_position()
    boat2 = ask_position()
    while boat2 == boat1:
        print("Position already occupied")
        boat2 = ask_position()
    playerBoats[boat1[0]][boat1[1]] = "🚢"
    playerBoats[boat2[0]][boat2[1]] = "🚢"
    return playerBoats

def turn(player, player_shot_grid, opponent_grid):
    if player == 1:
        display_grid(player_shot_grid, "History of game master's previous shots")
        shot = (random.randint(0,2), random.randint(0,2))
        print("The game master shot at position : ", shot)
    else:
        display_grid(player_shot_grid, "History of your previous shots")
        print("Enter your shot")
        shot = ask_position()
    if opponent_grid[shot[0]][shot[1]] == "🚢" or opponent_grid[shot[0]][shot[1]] == "X":
        player_shot_grid[shot[0]][shot[1]] = "X"
    else:
        player_shot_grid[shot[0]][shot[1]] = "."

def has_won(player_shot_grid):
    cpt = 0
    for i in player_shot_grid:
        for j in i:
            if j == "X":
                cpt +=1
    if cpt == 2:
        return True
    else:
        return False

def battleship_game():
    print(""" Rules of the Battleship Game: 🚢 

    Ahoy, brave captains! Prepare for battle on the high seas!  
    Here are the rules for this maritime challenge:  

    - The Objective:  
      Sink your opponent’s boats before they sink yours!  

    - The Setup:  
      Each player has a 3x3 grid to command.  
      You must secretly place 2 boats on your grid.  
      Boats can occupy any square, but no two boats can share the same spot.  
      """)## Rules were written by ChatGPT, to give more immersion to the player.

    playerG = initialize()
    playerS = empty_grid()
    masterG = empty_grid()
    x1, y1 = random.randint(0, 2), random.randint(0, 2)
    masterG[x1][y1] = "🚢"
    while True:
        x2, y2 = random.randint(0, 2), random.randint(0, 2)
        if (x2, y2) != (x1, y1):
            masterG[x2][y2] = "🚢"
            break
    masterS = empty_grid()

    display_grid(playerG, "Player, here is your grid")
    won = False
    actual_player = 0
    while not won:
        if actual_player == 0:
            turn(actual_player, playerS, masterG)
            won = has_won(playerS)
            if won:
                print("Bravo ! You won")
                return True
        if actual_player == 1:
            turn(actual_player, masterS, playerG)
            won = has_won(masterS)
            if won:
                print("You lost...")
                return False


        actual_player = next_player(actual_player)










##################################################### The game of Nim (Weak)

def display_sticks(n) :
    nb_sticks = n * "|"
    print(nb_sticks)

def player_removal(n) :
    while True:
        try:
            a = int(input("Enter an integer between 1,2,3 :"))
            if a >= 1 and a <= 3 and len(str(a)) == 1:
                break
            else:
                print("Invalid input. Please enter an integer between 1,2,3 :")
        except ValueError:
            print("Please enter a number (not text)")
    n = n - a
    nb_sticks = n * '|'
    return (nb_sticks, a)

def master_removal (n):
    b = n % 4
    print('The game master have removed',b,'sticks')


def nim_game():
    n = 20
    is_player_turn = True
    while n > 0:
        display_sticks(n)
        if is_player_turn == True :
            print("Player's turn!")
            n_player_sticks, n_removed = player_removal(n)
            is_player_turn = False
        else:
            print("Game master's turn!")
            if n % 4 == 0:
                n_removed = 1
            else:
                n_removed = n % 4

            print(f"The game master removes {n_removed} stick.")
            is_player_turn = True
        n -= n_removed
        if n == 0:
            if is_player_turn == True:
                print("You removed the last stick! You lose.")
                return False
            else:
                print("The game master removed the last stick! The player wins !")
                return True

##### Tic Tac Toe (Medium)


grid = [[" "," "," "],
        [" "," "," "],
        [" "," ", " "]
        ]

def display_grid_ttt(grid):
    if grid == [] or len(grid) != 3:
        print("The grid isn't properly formatted")
        return False
    else:
        for i in range(len(grid)):
            for j in range(len(grid[i]) - 1):
                print(" ", grid[i][j], end=" |")#added spaces for more ergonomic reading
            print(" ", grid[i][len(grid[i]) - 1])
            print("-"*15)



def check_victory(grid, symbol): ## amel did that
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
    temp_grid = grid
    for i in range(len(grid)): ## preview the victory of the game master in each cell, and place symbole were win is possible
        for j in range(len(grid[i])):
            if temp_grid[i][j] == " ":
                temp_grid[i][j] = symbol
                if check_victory(temp_grid, symbol):
                    return (i,j)
                else:
                    temp_grid[i][j] = " "
    for i in range(len(grid)): ## preview the victory of the player in each cell, and place symbol were needed
        for j in range(len(grid[i])):
            if temp_grid[i][j] == " ":
                temp_grid[i][j] = "X"
                if check_victory(temp_grid, "X"):
                    return (i,j)
                else:
                    temp_grid[i][j] = " "
    return (random.randint(0,2), random.randint(0,2))



def player_turn(grid):
    while True:
        try:
            row = int(input("Enter a number between (0,1,2) for the row : "))
            col = int(input("Enter a number between (0,1,2) for the column : "))
            while row < 0 or row > 2:
                print("Invalid input, row must be between 0 and 2")
                row = int(input("Enter a number from (0,1,2) for the row : "))
            while col < 0 or col > 2:
                print("Invalid input, columns must be between 0 and 2")
                col = int(input("Enter a number between (0,1,2) for the column : "))
        # Check if the cell is empty
            if grid[row][col] == ' ':
                grid[row][col] = 'X'  # Place the player's symbol (X)
                break  # Exit the loop once a valid move is made
            else:
                print("The cell is already occupied. Choose another cell.")
        except ValueError:
            print("Please enter a number")

def master_turn(grid):
    x,y = master_move(grid, "O")
    grid[x][y] = 'O'
    return grid

def full_grid(grid):
    found_space = False
    for row in grid:
        if " " in row:
            found_space = True
            break
    if found_space:
        return False
    else:
        return True

def check_result(grid):
    if check_victory(grid, "O"):
        return True
    elif check_victory(grid, "X"):
        return True
    elif full_grid(grid):
        return True
    else:
        return False



def tictactoe_game() :
    grid = [[" " for i in range(3)] for j in range(3)]
    while True:
        display_grid_ttt(grid) ## we need to display the grid for more ergonomy.
        player_turn(grid)
        if check_result(grid) == False:
            master_turn(grid)
        else:
            playerWon = check_victory(grid, "X")
            masterWon = check_victory(grid, "O")
            if playerWon:
                print("Bravo, you won !")
                return True
            elif masterWon:
                print("Master has won")
                return False





#### Challenge choice

def logical_challenge() :
    challenges = [battleship_game, nim_game, tictactoe_game]
    select_challenge = random.choice(challenges)
    return select_challenge()
