from chance_challenges import chance_challenge
from final_challenge import treasure_room
from logical_challenges import logical_challenge
from pere_fouras_challenge import pere_fouras_riddles
from utility_functions import *
from math_challenges import *

### we should add error management on some functions

def game():
    introduction()
    print("You'll now compose your team !")
    team = compose_team()
    key_won = 0
    while key_won < 3 :
        usrChoice = challenge_menu()
        print("--------------- \n Now, you must chose which player will participate : ")
        if len(team) > 1:
            player = choose_player(team)
        else:
            player = team[0]
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
        print("Well done, you finished the game and won !")
    else:
        print("You lost the game, goodbye...")


        print(key_won)



game()

print('test on the branch')