# Fort Boyard Simulator Project - Amel Boulhamane And Tom Hausmann

The Fort Boyard simulator, created by Hausmann Tom and Boulhamane Amel, is a project inspired by the TV game show. In this game, players must work in teams to complete various challenges and win three keys. Once all the keys have been collected, they move on to the final challenge, where the aim is to guess the secret word and unlock the treasure room. Developed in Python, the game uses the random library to introduce unpredictable elements. ChatGPT was also used to generate rules. Throughout the creation of the game, PyCharm was used as the main coding environment.

We are now going to present our game line by line for a better understanding:

1. The main function of Fort Boyard Simulator is `game()`.
2. Calls up the introductory function to display the rules and context of the game.
3. Prints a message to indicate the start of team composition.
4. Calls the `compose_team` function to collect information on team members (each player's name, profession and whether he/she is the leader). It then returns a list of team members in the `team` variable.
5. Initializes the `key_won` variable to 0, which represents the number of keys collected.
6. Loop continues until the player has collected 3 keys.
7. Displays the number of keys collected.
8. Calls the `challenge_menu` function to display challenge types: mathematical, logical, chance, and the riddle of Père Fouras. The user's choice, an integer, is stored in `usrChoice`.  
9. Message to choose a player for the next challenge.
10. Checks if the team has more than one player.
11. Calls the `choose_player` function to select a player from the team.
12. //
13. If there is only one player, he/she is automatically chosen for the challenge.
14. Checks if the user has chosen option 1 (mathematical challenge).
15. Calls the `math_challenge` function and checks if the player has succeeded.
16. Increases the number of keys won by 1 if the challenge is successful.
17. Checks if the user has chosen option 2 (logical challenge).
18. Calls the `logical_challenge` function and checks if the player succeeded. 
19. Increments the `key_won` count by 1 if the challenge is successful. 
20. Checks if the user chose option 3 (chance challenge). 
21. Calls the `chance_challenge` function and checks if the player succeeded. 
22. Increments the `key_won` count by 1 if the challenge is successful.
23. Checks if the user chose option 4 (Père Fouras' riddle). 
24. Calls the `pere_fouras_riddles` function and checks whether the player has succeeded.
25. Increases the number of keys won by 1 if the challenge is successful.
26. If all 3 keys are won, the player moves on to the `treasure_room` function where they guess a secret word.
27. If the `treasure_room` function returns `True`, a victory message is displayed.
28. If the `treasure_room` function returns `False`, a failure message is displayed.

---

## Functions Prototypes

- **`game()`**  
  The game's main controller. It manages team composition, challenges, and the final treasure room. It takes no parameters.
  
- **`introduction()`**  
  Displays the rules to the player. It takes no parameters.
  
- **`compose_team()`**  
  Allows the player to create their team by providing names, professions, and roles. It takes no parameters but returns a list of team members.
  
- **`challenge_menu()`**  
  Presents a menu of challenges and allows the player to select one. It takes no parameters but returns an integer corresponding to the challenge.
  
- **`choose_player(team)`**  
  Allows the player to select a team member for the next challenge. It takes a list of team members as a parameter and returns the chosen member.
  
- **`math_challenge`**  
  Randomly presents one of the mathematical challenges (solving a factorial problem, a linear equation, a mathematical roulette, or finding the nearest prime number). Depending on the player's response, it indicates whether the challenge has been successfully completed (winning a key or not).
  
- **`logical_challenge`**  
  Presents the player with a series of logical puzzles (Tic-Tac-Toe or Battleship). The function selects a game, and if the player wins, they get a key.
  
- **`chance_challenge`**  
  Combines two games of chance - the shell game and the dice game - into a single challenge. The player must succeed in at least one of these games to win the key.
  
- **`pere_fouras_riddles`**  
  Offers a challenge in which the player has 3 attempts to guess the correct answer. If they guess correctly, they win a key.
  
- **`treasure_room`**  
  A riddle based on clues to a secret word provided during the game. The player has 4 attempts to guess the correct word.

---

## Input and Error Management

- The game prompts users to choose a challenge (1 to 4). Inputs are checked to ensure they are valid, and invalid choices require retrying.
- When forming the team, players must enter their name, profession, and leader status (“yes” or “no”). The game ensures all fields are completed correctly before proceeding.
- Challenges like riddles and math require specific answers. If the answer is wrong, players can retry until attempts are used up, with guiding messages provided.
- To enter the treasure room, players must guess a secret word in four tries. Wrong guesses provide extra clues until the word is guessed or attempts run out.

---

## Project Chronology

- **Friday, December 6th**  
  Completed the first challenge (mathematical + logical + chance + Père Fouras).
  
- **Friday, December 20th**  
  Integrated all the individual functions into the final program and started the final tests and improvements.

---

## Task Distribution

- **Amel**  
  Focused on designing the different types of challenges players encounter in the game, including mathematical, logical, and chance challenges, as well as the initial implementation of the Père Fouras challenge (with significant help from Tom for the coding of this last one).
  
- **Tom**  
  Developed the main logic of the various challenges, including logic puzzles, games of chance, the Père Fouras challenge, and the final challenge.  
  Throughout the process, they worked closely together, providing mutual logic support.
