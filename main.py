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
        print("Now, you must chose which player will participate : ")
        if len(team) > 1:
            player = choose_player(team)
        else:
            player = team[0]
        if usrChoice == 1:
            if math_challenge():
                key_won += 1
        print(key_won)



game()
