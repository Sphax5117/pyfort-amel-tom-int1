import json
import random

'''
Fort Boyard Project 
Authors : Amel Boulhamane and Tom Hausmann
Role of this file : 
This file aims at providing the pere fouras challenge for the Fort Boyard Game.
It simply consists of giving the user a riddle. After that, the user has to guess the answer.
All functions have been commented.
'''

def load_json(file):
    with open(file, "r") as f:
        data = json.load(f)

    riddles = []
    for riddle in data:
       riddles.append({riddle['question']:riddle['answer']}) ##questions to riddle.
    return riddles

def pere_fouras_riddles():
    riddles = load_json("data/PFRiddles2.json") ## change to riddle
    attempts = 3
    chosenRiddle = random.choice(riddles)
    print(f"Hello Adventurer.\nHere is my riddle : \n\n{list(chosenRiddle.keys())[0]}.\n")
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        usrInput = input("Your answer : ").lower()
        if usrInput == list(chosenRiddle.values())[0]:
            print("Well done, you won a key !")
            return True
        else:
            print(f"Sorry, but your answer is wrong. Try again.")
        attempts -= 1
    print(f"You  lost... The answer was {list(chosenRiddle.values())[0]}")
    return False
