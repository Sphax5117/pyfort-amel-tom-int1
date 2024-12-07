import random
## we'll define 0 for the player, 1 for the game master
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
    r,c = eval(input("Enter the position in the format row,column (1,2 or 3) : "))
    r,c = r-1,c-1
    while r < 0 or r > 2 or c < 0 or c > 2:
        r, c = eval(input("Enter the position in the format row,column : (1,2 or 3)"))
        r, c = r - 1, c - 1
    return (r,c)

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
    display_grid(player_shot_grid, "History of your previous shots")
    if player == 1:
        shot = (random.randint(0,2), random.randint(0,2))
        print(shot)
    else:
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
      Boats can occupy any square, but no two boats can share the same spot.  """)

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

    print(display_grid(masterG,"Master grid : "))
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
                return
        if actual_player == 1:
            turn(actual_player, masterS, playerG)
            won = has_won(masterS)
            if won:
                print("You lost...")
                return False


        actual_player = next_player(actual_player)





battleship_game()
