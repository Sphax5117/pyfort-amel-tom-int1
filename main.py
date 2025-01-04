from chance_challenges import chance_challenge
from final_challenge import treasure_room
from logical_challenges import logical_challenge
from pere_fouras_challenge import pere_fouras_riddles
from utility_functions import *
from math_challenges import *

'''
Fort Boyard Project 
Authors : Amel Boulhamane and Tom Hausmann
Role of this file : 
This file is the heart of the game, where everything is launched. It follows the order given in the project file.
'''

def game():
    introduction()
    print("You'll now compose your team !")
    team = compose_team()
    key_won = 0
    while key_won < 3 :
        print(f"-------------------- \n  You have {key_won} keys")
        usrChoice = challenge_menu()
        if len(team) > 1:
            print("-------------------- \nNow, you must chose which player will participate : ")
            player = choose_player(team)
        else:
            player = team[0]
            print("--------------------")
        if usrChoice == 1:
            if math_challenge():
                key_won += 1
        if usrChoice == 2:
            if logical_challenge(): ### the boat must be fixed, there are some problems (true not returned, weird prints)
                key_won += 1
        if usrChoice == 3:
            if chance_challenge():
                key_won += 1
        if usrChoice == 4:
            if pere_fouras_riddles():
                key_won += 1
    if treasure_room():
        print("You have won, bravo !")
    else:
        print("You failed... You'll stay on the fort boyard for the rest of your life")




if __name__ == "__main__":
    game()
