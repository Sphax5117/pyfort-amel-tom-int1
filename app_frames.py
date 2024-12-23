import tkinter as tk
from tkinter import ttk
import json
import random
import os
from fractions import Fraction

# Import math challenge functions
from math_challenges import random_math_challenge


class FortBoyardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fort Boyard Game - Amel and Tom")
        self.geometry("800x500")
        self.resizable(width=False, height=False)

        # Dictionary to store references to frames
        self.frames = {}

        # This will store the final team data
        self.team_data = []

        # Container where all frames (pages) live
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Make container stretch if window resizes
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create instances of each page
        self.main_frame = MainFrame(container, self)
        self.team_creation_frame = TeamCreationFrame(container, self)
        self.challenge_frame = ChallengeFrame(container, self)
        self.math_challenge_frame = MathChallengeFrame(container, self)
        self.pere_fouras_frame = PereFourasFrame(container, self)   # NEW FRAME

        # Place each frame in the same row/column
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.team_creation_frame.grid(row=0, column=0, sticky="nsew")
        self.challenge_frame.grid(row=0, column=0, sticky="nsew")
        self.math_challenge_frame.grid(row=0, column=0, sticky="nsew")
        self.pere_fouras_frame.grid(row=0, column=0, sticky="nsew") # NEW FRAME

        # Add frames to dictionary for easy access
        self.frames["MainFrame"] = self.main_frame
        self.frames["TeamCreationFrame"] = self.team_creation_frame
        self.frames["ChallengeFrame"] = self.challenge_frame
        self.frames["MathChallengeFrame"] = self.math_challenge_frame
        self.frames["PereFourasFrame"] = self.pere_fouras_frame      # NEW FRAME

        # Show the initial page
        self.show_frame("MainFrame")

    def show_frame(self, frame_name):
        """
        Bring the frame with name 'frame_name' to the front.
        """
        frame = self.frames[frame_name]
        frame.tkraise()


class MainFrame(tk.Frame):
    """
    Page 1: Intro + choose how many players (max 3).
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(
            self,
            text="Hello Adventurer, welcome to our Fort Boyard Game!",
            font=('Montserrat', 16)
        )
        title.pack(pady=20)

        rule = tk.Label(
            self,
            text=(
                "To win the game, you must complete challenges to earn keys.\n"
                "With 3 keys, you open the treasure room!"
            ),
            font=('Montserrat', 12),
            wraplength=600
        )
        rule.pack(pady=10)

        prompt = tk.Label(
            self,
            text="How many players are in your team?",
            font=('Montserrat', 14)
        )
        prompt.pack(pady=10)

        # Only 3 players max => combobox has ["1","2","3"]
        self.num_players_cb = ttk.Combobox(
            self,
            values=["1", "2", "3"],
            font=('Montserrat', 14),
            state="readonly"
        )
        self.num_players_cb.set("1")  # default is 1
        self.num_players_cb.pack(pady=5)

        start_button = tk.Button(
            self,
            text="Start Team Creation",
            font=('Montserrat', 12),
            command=self.go_to_team_creation
        )
        start_button.pack(pady=20)

    def go_to_team_creation(self):
        """
        Move to TeamCreationFrame and let it know how many players to display.
        """
        num_players = int(self.num_players_cb.get())

        # Set the number of players in TeamCreationFrame
        team_frame = self.controller.frames["TeamCreationFrame"]
        team_frame.set_num_players(num_players)

        # Clear any old data from previous usage
        self.controller.team_data = []

        # Show the next frame
        self.controller.show_frame("TeamCreationFrame")


class TeamCreationFrame(tk.Frame):
    """
    Page 2: Collect each player's name, profession, role.
    Exactly one leader must exist.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.num_players = 1
        self.name_entries = []
        self.prof_entries = []
        self.role_comboboxes = []

        self.entries_frame = None

        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(self, text="Team Creation", font=('Montserrat', 16))
        header.pack(pady=20)

        self.entries_frame = tk.Frame(self)
        self.entries_frame.pack()

        self.confirm_button = tk.Button(
            self,
            text="Confirm",
            font=('Montserrat', 12),
            command=self.confirm_data
        )
        self.confirm_button.pack(pady=10)

        self.next_button = tk.Button(
            self,
            text="Next -> Choose Challenge",
            font=('Montserrat', 12),
            command=self.go_to_challenge
        )
        self.next_button.pack(pady=10)
        self.next_button.config(state="disabled")

        back_button = tk.Button(
            self,
            text="Back to Main",
            font=('Montserrat', 12),
            command=lambda: self.controller.show_frame("MainFrame")
        )
        back_button.pack(pady=10)

    def set_num_players(self, num_players):
        """
        Called by MainFrame to specify how many player fields we need.
        """
        self.num_players = num_players

        # Clear existing widgets
        for widget in self.entries_frame.winfo_children():
            widget.destroy()

        self.name_entries = []
        self.prof_entries = []
        self.role_comboboxes = []

        for i in range(num_players):
            row_frame = tk.Frame(self.entries_frame)
            row_frame.pack(pady=5)

            tk.Label(
                row_frame,
                text=f"Player {i + 1} Name:",
                font=('Montserrat', 12)
            ).pack(side="left", padx=5)

            name_entry = tk.Entry(row_frame, font=('Montserrat', 12), width=12)
            name_entry.pack(side="left", padx=5)
            self.name_entries.append(name_entry)

            tk.Label(
                row_frame,
                text="Profession:",
                font=('Montserrat', 12)
            ).pack(side="left", padx=5)

            prof_entry = tk.Entry(row_frame, font=('Montserrat', 12), width=12)
            prof_entry.pack(side="left", padx=5)
            self.prof_entries.append(prof_entry)

            tk.Label(
                row_frame,
                text="Role:",
                font=('Montserrat', 12)
            ).pack(side="left", padx=5)

            # Combobox with 'Leader' or 'Member'
            role_cb = ttk.Combobox(
                row_frame,
                values=["Leader", "Member"],
                state="readonly",
                width=8
            )
            role_cb.set("Member")
            role_cb.pack(side="left", padx=5)
            self.role_comboboxes.append(role_cb)

        # Disable "Next" each time we set the players
        self.next_button.config(state="disabled")

    def confirm_data(self):
        """
        Validates the 'exactly one leader' rule and finalizes the team data.
        """
        team_data = []
        leader_count = 0
        leader_index = -1

        for i in range(self.num_players):
            name_val = self.name_entries[i].get().strip()
            prof_val = self.prof_entries[i].get().strip()
            role_val = self.role_comboboxes[i].get()

            player_dict = {
                "name": name_val if name_val else f"Player{i + 1}",
                "profession": prof_val if prof_val else "Unspecified",
                "leader": (role_val == "Leader")
            }
            team_data.append(player_dict)

        # Count how many leaders; track first one
        for idx, player in enumerate(team_data):
            if player["leader"]:
                leader_count += 1
                if leader_index < 0:
                    leader_index = idx

        if leader_count == 0:
            # No leader => first player becomes leader
            team_data[0]["leader"] = True
        elif leader_count > 1:
            # Keep only the first encountered leader
            for idx, player in enumerate(team_data):
                if idx != leader_index:
                    player["leader"] = False

        # Now exactly one leader
        self.controller.team_data = team_data

        print("Finalized Team Data:")
        for p in team_data:
            print(p)

        # Enable "Next" button
        self.next_button.config(state="normal")

    def go_to_challenge(self):
        """
        Go to the ChallengeFrame, passing the final team data.
        """
        challenge_frame = self.controller.frames["ChallengeFrame"]
        challenge_frame.set_team_data(self.controller.team_data)
        self.controller.show_frame("ChallengeFrame")


class ChallengeFrame(tk.Frame):
    """
    Page 3: Choose challenge type & which player will attempt it.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.team_data = []
        self.challenge_type = tk.StringVar(value="Mathematics")
        self.selected_player_idx = tk.IntVar(value=0)

        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(self, text="Choose a Challenge & Player", font=('Montserrat', 16))
        header.pack(pady=20)

        # Challenge options
        challenge_frame = tk.LabelFrame(self, text="Challenge Type", font=('Montserrat', 12))
        challenge_frame.pack(pady=10)

        challenges = [
            ("Mathematics", "Mathematics"),
            ("Logic", "Logic"),
            ("Chance", "Chance"),
            ("Père Fouras’ Riddle", "Père Fouras’ Riddle"),
        ]
        for label_text, value in challenges:
            rb = tk.Radiobutton(
                challenge_frame,
                text=label_text,
                variable=self.challenge_type,
                value=value,
                font=('Montserrat', 12)
            )
            rb.pack(anchor="w", padx=20, pady=2)

        # Player selection
        self.players_frame = tk.LabelFrame(self, text="Choose Player", font=('Montserrat', 12))
        self.players_frame.pack(pady=10)

        # Confirm & Back
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        confirm_button = tk.Button(
            button_frame,
            text="Confirm Choice",
            font=('Montserrat', 12),
            command=self.confirm_choice
        )
        confirm_button.pack(side="left", padx=10)

        back_button = tk.Button(
            button_frame,
            text="<- Back to Team Creation",
            font=('Montserrat', 12),
            command=lambda: self.controller.show_frame("TeamCreationFrame")
        )
        back_button.pack(side="left", padx=10)

    def set_team_data(self, team_data):
        """
        Builds radio buttons for each player in the team.
        """
        self.team_data = team_data

        # Clear any old radio buttons
        for widget in self.players_frame.winfo_children():
            widget.destroy()

        self.selected_player_idx.set(0)  # default to first

        for i, player in enumerate(team_data):
            role_str = "Leader" if player["leader"] else "Member"
            display_text = f"Player {i + 1}: {player['name']} ({player['profession']}, {role_str})"

            rb = tk.Radiobutton(
                self.players_frame,
                text=display_text,
                variable=self.selected_player_idx,
                value=i,
                font=('Montserrat', 12),
                anchor="w"
            )
            rb.pack(anchor="w", padx=10, pady=2)

    def confirm_choice(self):
        chosen_challenge = self.challenge_type.get()
        chosen_idx = self.selected_player_idx.get()
        chosen_player = self.team_data[chosen_idx]

        print(f"Challenge chosen: {chosen_challenge}")
        print(f"Player chosen: {chosen_player['name']} (Leader={chosen_player['leader']})")

        # For demonstration, show a label with the results
        tk.Label(
            self,
            text=f"Choice Confirmed: {chosen_challenge} by {chosen_player['name']}",
            font=('Montserrat', 12),
            fg="green"
        ).pack()

        if chosen_challenge == "Mathematics":
            self.controller.show_frame("MathChallengeFrame")
        elif chosen_challenge == "Père Fouras’ Riddle":
            # Show the PereFourasFrame
            self.controller.show_frame("PereFourasFrame")
        else:
            # In a complete app, you'd create other frames for Logic, Chance, etc.
            pass


class MathChallengeFrame(tk.Frame):
    """
    This frame will randomly present one of the three math challenges:
      1) Factorial
      2) Roulette (add/sub/mult)
      3) Linear Equation (accept fractions like "4/37")
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Keep track of the correct answer for each challenge
        self.correct_answer = None

        # Title
        self.title_label = tk.Label(
            self,
            text="Mathematics Challenge",
            font=('Montserrat', 16)
        )
        self.title_label.pack(pady=20)

        # Where the challenge text will appear
        self.challenge_label = tk.Label(self, text="", font=('Montserrat', 14))
        self.challenge_label.pack(pady=10)

        # Entry for the user's answer
        self.answer_entry = tk.Entry(self, font=('Montserrat', 14), width=10)
        self.answer_entry.pack(pady=5)

        # Button to check the answer
        check_button = tk.Button(
            self,
            text="Check Answer",
            font=('Montserrat', 12),
            command=self.check_answer
        )
        check_button.pack(pady=10)

        # Label to show the result (correct / incorrect)
        self.result_label = tk.Label(self, text="", font=('Montserrat', 12))
        self.result_label.pack(pady=10)

        # Button to get a new random challenge
        new_button = tk.Button(
            self,
            text="New Math Challenge",
            font=('Montserrat', 12),
            command=self.load_new_challenge
        )
        new_button.pack(pady=10)

        # Button to go back to the ChallengeFrame
        back_button = tk.Button(
            self,
            text="Back to Challenge Selection",
            font=('Montserrat', 12),
            command=lambda: controller.show_frame("ChallengeFrame")
        )
        back_button.pack(pady=10)

        # Automatically load a new random challenge when this frame is created
        self.load_new_challenge()

    def load_new_challenge(self):
        """
        Pick a new random math challenge and update the UI.
        """
        challenge_text, correct_answer = random_math_challenge()
        self.correct_answer = correct_answer

        # Show the challenge text
        self.challenge_label.config(text=challenge_text)
        # Clear previous answer & result
        self.answer_entry.delete(0, tk.END)
        self.result_label.config(text="", fg="black")

    def check_answer(self):
        """
        Check if the user's input matches the correct answer.
        Allows fraction input (like -4/37) if the user types a slash.
        Otherwise, tries float comparison (for factorial/roulette).
        """
        user_answer = self.answer_entry.get().strip()

        try:
            if "/" in user_answer:
                # Parse fraction input
                user_val = Fraction(user_answer)
                if isinstance(self.correct_answer, Fraction):
                    # Compare fraction to fraction
                    if user_val == self.correct_answer:
                        self.result_label.config(text="Correct!", fg="green")
                    else:
                        self.result_label.config(
                            text=f"Incorrect! Correct answer: {self.correct_answer}",
                            fg="red"
                        )
                else:
                    # Compare fraction float to int/float
                    if abs(float(user_val) - float(self.correct_answer)) < 1e-6:
                        self.result_label.config(text="Correct!", fg="green")
                    else:
                        self.result_label.config(
                            text=f"Incorrect! Correct answer: {self.correct_answer}",
                            fg="red"
                        )
            else:
                # Parse float input
                user_val_float = float(user_answer)
                if isinstance(self.correct_answer, Fraction):
                    # Compare float of user input vs float of fraction
                    if abs(user_val_float - float(self.correct_answer)) < 1e-6:
                        self.result_label.config(text="Correct!", fg="green")
                    else:
                        self.result_label.config(
                            text=f"Incorrect! Correct answer: {self.correct_answer}",
                            fg="red"
                        )
                else:
                    # correct_answer is int or float
                    correct_val = float(self.correct_answer)
                    if abs(user_val_float - correct_val) < 1e-6:
                        self.result_label.config(text="Correct!", fg="green")
                    else:
                        self.result_label.config(
                            text=f"Incorrect! Correct answer: {self.correct_answer}",
                            fg="red"
                        )
        except ValueError:
            self.result_label.config(
                text="Please enter a valid numeric or fraction answer!",
                fg="red"
            )


class PereFourasFrame(tk.Frame):
    """
    This frame presents a random Père Fouras riddle from data/PFRiddles.json.
    The user has 3 attempts to guess the correct answer.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # State variables
        self.attempts_left = 3
        self.current_riddle_text = ""
        self.current_riddle_answer = ""

        # Title label
        self.title_label = tk.Label(
            self,
            text="Père Fouras’ Riddle Challenge",
            font=('Montserrat', 16)
        )
        self.title_label.pack(pady=20)

        # Where the riddle text will appear
        self.riddle_label = tk.Label(self, text="", font=('Montserrat', 14), wraplength=600)
        self.riddle_label.pack(pady=10)

        # Attempt count label
        self.attempt_label = tk.Label(self, text="", font=('Montserrat', 12))
        self.attempt_label.pack(pady=5)

        # Entry for the user's answer
        self.answer_entry = tk.Entry(self, font=('Montserrat', 14), width=30)
        self.answer_entry.pack(pady=5)

        # Button to check the answer
        check_button = tk.Button(
            self,
            text="Check Answer",
            font=('Montserrat', 12),
            command=self.check_answer
        )
        check_button.pack(pady=10)

        # Label to show the result (correct / incorrect)
        self.result_label = tk.Label(self, text="", font=('Montserrat', 12))
        self.result_label.pack(pady=10)

        # Button to load a new random riddle
        new_button = tk.Button(
            self,
            text="New Riddle",
            font=('Montserrat', 12),
            command=self.load_new_riddle
        )
        new_button.pack(pady=5)

        # Button to go back to the ChallengeFrame
        back_button = tk.Button(
            self,
            text="Back to Challenge Selection",
            font=('Montserrat', 12),
            command=lambda: self.controller.show_frame("ChallengeFrame")
        )
        back_button.pack(pady=10)

        # Automatically load a riddle when this frame is created
        self.load_new_riddle()

    def load_new_riddle(self):
        """
        Pick a new random riddle from 'data/PFRiddles.json', reset attempts, and update the UI.
        """
        riddles = self.load_json("data/PFRiddles.json")
        chosen_riddle = random.choice(riddles)

        # Each entry is a dict like {"riddle": "...", "answer": "..."}
        self.current_riddle_text = chosen_riddle['riddle']
        self.current_riddle_answer = chosen_riddle['answer']

        self.attempts_left = 3
        self.riddle_label.config(text=self.current_riddle_text)
        self.result_label.config(text="", fg="black")
        self.answer_entry.delete(0, tk.END)
        self.update_attempt_label()

    def load_json(self, file_path):
        """
        Utility method to load riddles from JSON.
        """
        abs_path = os.path.abspath(file_path)
        with open(abs_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def update_attempt_label(self):
        """
        Update the label that shows how many attempts are left.
        """
        self.attempt_label.config(text=f"Attempts left: {self.attempts_left}")

    def check_answer(self):
        """
        Compare the user's input to the riddle's correct answer (case-insensitive).
        """
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.current_riddle_answer.strip().lower()

        if user_answer == correct_answer:
            self.result_label.config(text="Well done, you won a key!", fg="green")
        else:
            self.attempts_left -= 1
            self.update_attempt_label()

            if self.attempts_left <= 0:
                self.result_label.config(
                    text=f"You lost... The answer was: '{self.current_riddle_answer}'",
                    fg="red"
                )
            else:
                self.result_label.config(text="Wrong answer, try again!", fg="red")


if __name__ == "__main__":
    app = FortBoyardApp()
    app.mainloop()
