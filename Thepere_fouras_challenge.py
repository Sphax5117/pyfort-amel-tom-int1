"""
Function : pere_fouras_riddles() → Boolean Local variables4 :
• A list to store the riddles.
• A dictionary to store the randomly selected riddle.
• An integer initialized to 3, representing the number of
attempts.
Begin
1. Use the load_riddles(file) function to retrieve the riddles
    from the JSON file and store them in a list.
2. Randomly select a riddle from the list and store it in a
    dictionary variable.
3. Display the riddle's question to the player.
4. As long as the number of attempts is greater than zero 0 do:
• Prompt the player to enter their answer and convert the input to lowercase.
• If the player's answer matches the correct answer from the chosen riddle:
§ Display a message indicating the answer is correct and that the player wins a key.
§ Return True.
• Otherwise:
End.
§ Decrease the number of remaining attempts by 1. § If any attempts remain:
• Display a message that the answer is incorrect and show the number of remaining attempts.
§ Otherwise:
• Display a failure message along with the correct
answer to the riddle. § Return False.
"""

import json
import random

def load_riddles(file) :
    with open(file,‘r’, encoding=’utf-8’) as f:
        file = json.load(f)
        return file

def pere_fouras_riddles() :
    riddles = []
    selected_riddle = {}
    attempts = 3

    riddles = load_riddles(file)
    selected_riddle = random.choice(riddles)
    print(selected_riddle)

