import json
import random

def load_json(file):
    with open(file, "r") as f:
        data = json.load(f)

    riddles = []
    for riddle in data:
       riddles.append({riddle['riddle']:riddle['answer']})
    return riddles

def pere_fouras_riddles():
    riddles = load_json("data/PFRiddles.json")
    attempts = 3
    chosenRiddle = random.choice(riddles)
    print(f"Hello Adventurer.\nHere is my riddle : {list(chosenRiddle.keys())[0]}.")
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
pere_fouras_riddles()

