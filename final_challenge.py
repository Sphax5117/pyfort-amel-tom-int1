import json
import random

def treasure_room():
    with open("data/TR_Clues.json", "r") as f:
        data = json.load(f)

    clues = []
    for clue in data:
        clues.append({clue["CODE-WORD"]: clue["Clues"]})
    chosen_clue = random.choice(clues)
    code_word = list(chosen_clue.keys())[0]
    associatedClues = list(chosen_clue.values())[0]
    print(associatedClues)
    attempts = 4 ## if we want to display all the clues to the user, he must be able to answer 4 times...
    answer_correct = False
    print(f"Hello Adventurer.\nHere are the first 3 clues that will help you to discover the secret word: {associatedClues[0]}, {associatedClues[1]} and {associatedClues[2]}.")
    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        usrInput = input("Your answer : ").upper()
        if usrInput == code_word:
            answer_correct = True
            break
        else:
            print(f"Sorry, but your answer is wrong. Here is the next clue : {associatedClues[-attempts]}") ## to display dynamically the resting clues, we start by -attempts (hence -3)
        attempts -= 1
    if answer_correct:
        print("You have won, bravo !")
    else:
        print("You failed... You'll stay on the fort boyard for the rest of your life")
treasure_room()