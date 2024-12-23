import random

def shell_game():
    shells = ['A', 'B', 'C']
    rules = """
        🧙‍♂️ 
        Listen closely, brave adventurer,
        Here are the rules for this peculiar venture.
        Under one of three shells, a key lies concealed:
        Under A, under B, or under C, its hiding spot is revealed.

        - First rule: You have two attempts, no more, no less,
          To uncover the hiding place of the key, I confess.
          After each try, the key’s position will change,
          It moves in secret, sly and strange.

        - Second rule: Choose wisely, with focus and care,
          Point to a shell and say your prayer.
          If you find the key, victory is yours,
          But fail, and you must try once more.

        - Third rule: Remember, dear contender,
          The odds are tricky, but don’t surrender.
          Under A, under B, or under C, it could be,
          With sharp wits and luck, you’ll claim the key!

        So, play the game and keep your nerve,
        For here at Fort Boyard, only the bold deserve!
        """
    print(rules)
    for i in range(2):
        choice = random.choice(shells)
        print(f"You have {2-i} guesses left")
        userInput = input((f"Try {i+1}, what is your guess : ")).upper()
        while userInput not in shells:
            print("Your choice isn't in the propositions (A,B or C)")
            userInput = input((f"Try {i+1}, what is your guess : ")).upper()
        if userInput == choice:
            print(f"Well down brave adventurer, you found the key beneath shell {choice}")
            return True
        else:
            print("You were unsucessful, try again !")
    print("You lost...")
    return False

def chance_challenge():
        challenges = [shell_game, roll_dice_game]
        select_challenge = random.choice(challenges)
        return select_challenge()

def roll_dice_game():
    attempts = 3
    for i in range (attempts):
        n = str(input("Press 'Enter' to roll the dice"))
        if n != 'Enter':
            n= str(input("Press 'Enter' to roll the dice"))
        player_dice=(random.randint(1,6),random.randint(1,6))
        print (player_dice)
        if 6 in player_dice :
            print ("You win the game and the key !!")
            return True
        master_dice=(random.randint(1,6),random.randint(1,6))
        print(master_dice)
        if 6 in master_dice :
            print ("The game master has won the game...")
            return False
        print ("No one find 6. Move to the next attempt.")
    print ("Neither the player nor the game master  find 6")
    return False



