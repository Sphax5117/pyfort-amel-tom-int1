'''
Fort Boyard Project
Authors : Amel Boulhamane and Tom Hausmann
Role of this file :
This file encompasses all the necesseraries useful functions. They are mostly used to show data to the player or to ensure the game logic.
'''



def introduction():
    print("Welcome to the Fort Boyard, adventurer ! To win the game, you must complete challenges in order to earn keys. With 3 keys, you shall open the treasure room !")

def compose_team():
    equip = [] ### we should change that variable name to teams
    n = int(input("How many players do you want : "))
    while n > 3 or n < 0:
        print("Please enter a number of player between 1 and 3 (included)")
        n = int(input("How many players do you want : "))
    for i in range(n):
        name = input("What is your name? ")
        profession = input("What is your profession? ")
        if i == 0 or equip[i-1]["leader"] == False:
            leader = input("Are you the leader ? (enter y or n) ") == "y"
            equip.append({"name": name, "profession": profession, "leader": leader})
        else:
            equip.append({"name": name, "profession": profession, "leader": False})
    cpt = 0
    for i in range(n):
        if equip[i]["leader"] == False:
            cpt += 1
    if cpt == n:
        equip[0]["leader"] = True

    return equip



def challenge_menu():
    print("----------- \n You must chose a challenge type:  \n 1. Mathematics challenge \n 2. Logic challenge \n 3. Chance challenge \n 4. Père Fouras' riddle")
    usrChoice = int(input("Enter you choice : "))
    while usrChoice < 1 or usrChoice > 4:
        usrChoice = int(input("Re-enter your choice : "))
    return usrChoice

def choose_player(team):
    for i in range(len(team)):
        if team[i]["leader"]:
            r = "Leader"
        else: r = "Member"
        print(f"---------- Player {i +1 } \n Name : {team[i]['name']} \n Profession {team[i]['profession']} \n Role : {r}")
    usrchoice = int(input("Enter the player's number : "))
    while usrchoice < 1 or usrchoice > len(team):
        usrchoice = int(input("Re-enter the player's number :"))

    return team[usrchoice-1]

def record_history(): ### We'll develop that later, might store in a JSON
    pass
