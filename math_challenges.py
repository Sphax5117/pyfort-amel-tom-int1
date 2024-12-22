import tkinter as tk
from tkinter import ttk
import random


# ------------------------- Math Challenge Helpers ----------------------------
def factorial(n):
    final = 1
    for i in range(2, n + 1):
        final *= i
    return final


def math_challenge_factorial():
    """
    Returns (challenge_text, correct_answer).
    Example: "Calculate the factorial of 5" => correct_answer=120
    """
    n = random.randint(1, 10)
    challenge_text = f"Math Challenge: Calculate the factorial of {n}"
    correct_answer = factorial(n)
    return challenge_text, correct_answer


def math_roulette_challenge():
    """
    Returns (challenge_text, correct_answer) for a random 'roulette' of 5 numbers
    with addition, subtraction, or multiplication.
    """
    nums = [random.randint(1, 20) for _ in range(5)]
    operations = ["addition", "subtraction", "multiplication"]
    op_choice = random.choice(operations)

    if op_choice == "addition":
        correct_answer = sum(nums)
        challenge_str = " + ".join(str(x) for x in nums)
    elif op_choice == "subtraction":
        correct_answer = nums[0]
        for i in range(1, 5):
            correct_answer -= nums[i]
        challenge_str = " - ".join(str(x) for x in nums)
    else:  # multiplication
        correct_answer = 1
        for x in nums:
            correct_answer *= x
        challenge_str = " * ".join(str(x) for x in nums)

    challenge_text = f"Math Challenge: {challenge_str} = ?"
    return challenge_text, correct_answer


def solve_linear_equation():
    """
    Returns (a, b, x) for a*x + b = 0
    x = -b / a
    """
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = -b / a
    return a, b, x


def math_challenge_equation():
    """
    Returns (challenge_text, correct_answer) for a linear eqn: a*x + b = 0
    """
    a, b, x = solve_linear_equation()
    challenge_text = f"Math Challenge: Solve the equation {a}x + {b} = 0"
    correct_answer = x
    return challenge_text, correct_answer


def random_math_challenge():
    """
    Randomly picks one of the three math sub-challenges
    and returns (challenge_text, correct_answer).
    """
    challenges = [math_challenge_factorial, math_roulette_challenge, math_challenge_equation]
    chosen_func = random.choice(challenges)
    return chosen_func()


# ------------------------- Main Tkinter App & Frames -------------------------
class FortBoyardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fort Boyard Game - Amel and Tom")
        self.geometry("800x500")
        self.resizable(width=False, height=False)

        # Store references to frames
        self.frames = {}

        # Final team data will live here
        self.team_data = []

        # Create one container, managed by pack (so it fills the window)
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Create each page
        self.main_frame = MainFrame(container, self)
        self.team_creation_frame = TeamCreationFrame(container, self)
        self.challenge_frame = ChallengeFrame(container, self)
        self.math_challenge_frame = MathChallengeFrame(container, self)

        # Place each page using place() at (0,0), filling the container
        # so tkraise() can reliably show/hide them.
        for frame in (
                self.main_frame,
                self.team_creation_frame,
                self.challenge_frame,
                self.math_challenge_frame
        ):
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        # Keep references in a dictionary
        self.frames["MainFrame"] = self.main_frame
        self.frames["TeamCreationFrame"] = self.team_creation_frame
        self.frames["ChallengeFrame"] = self.challenge_frame
        self.frames["MathChallengeFrame"] = self.math_challenge_frame

        # Show the main frame first
        self.show_frame("MainFrame")

    def show_frame(self, frame_name):
        """
        Raise the specified frame to the top, making it visible.
        """
        frame = self.frames[frame_name]
        frame.tkraise()


# ------------------------- Page 1: Main Frame -------------------------
class MainFrame(tk.Frame):
    """
    Lets user pick how many players (1 to 3).
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
            text=("To win, you must complete challenges to earn keys.\n"
                  "With 3 keys, you open the treasure room!"),
            font=('Montserrat', 12),
            wraplength=600
        )
        rule.pack(pady=10)

        prompt = tk.Label(
            self,
            text="How many players in your team? (Max 3)",
            font=('Montserrat', 14)
        )
        prompt.pack(pady=10)

        self.num_players_cb = ttk.Combobox(
            self,
            values=["1", "2", "3"],
            font=('Montserrat', 14),
            state="readonly"
        )
        self.num_players_cb.set("1")  # default
        self.num_players_cb.pack(pady=5)

        start_button = tk.Button(
            self,
            text="Start Team Creation",
            font=('Montserrat', 12),
            command=self.go_to_team_creation
        )
        start_button.pack(pady=20)

    def go_to_team_creation(self):
        num_players = int(self.num_players_cb.get())
        team_frame = self.controller.frames["TeamCreationFrame"]
        team_frame.set_num_players(num_players)

        # Clear old data
        self.controller.team_data = []

        # Show TeamCreationFrame
        self.controller.show_frame("TeamCreationFrame")


# ------------------------- Page 2: Team Creation -------------------------
class TeamCreationFrame(tk.Frame):
    """
    Collect data for each player. Must have exactly one leader.
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

        confirm_next_button = tk.Button(
            self,
            text="Confirm & Go To Challenge",
            font=('Montserrat', 12),
            command=self.confirm_and_next
        )
        confirm_next_button.pack(pady=10)

        back_button = tk.Button(
            self,
            text="Back to Main",
            font=('Montserrat', 12),
            command=lambda: self.controller.show_frame("MainFrame")
        )
        back_button.pack(pady=10)

    def set_num_players(self, num_players):
        self.num_players = num_players

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

            role_cb = ttk.Combobox(
                row_frame,
                values=["Leader", "Member"],
                state="readonly",
                width=8
            )
            role_cb.set("Member")
            role_cb.pack(side="left", padx=5)
            self.role_comboboxes.append(role_cb)

    def confirm_and_next(self):
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

        # Enforce exactly one leader
        for idx, player in enumerate(team_data):
            if player["leader"]:
                leader_count += 1
                if leader_index < 0:
                    leader_index = idx

        if leader_count == 0:
            team_data[0]["leader"] = True
        elif leader_count > 1:
            for idx, player in enumerate(team_data):
                if idx != leader_index:
                    player["leader"] = False

        self.controller.team_data = team_data
        print("Finalized Team Data:")
        for p in team_data:
            print(p)

        # Next: ChallengeFrame
        challenge_frame = self.controller.frames["ChallengeFrame"]
        challenge_frame.set_team_data(team_data)
        self.controller.show_frame("ChallengeFrame")


# ------------------------- Page 3: Choose Challenge -------------------------
class ChallengeFrame(tk.Frame):
    """
    Pick the challenge type and which player attempts it.
    If 'Mathematics' -> go to MathChallengeFrame.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.team_data = []
        self.challenge_type = tk.StringVar(value="Mathematics")  # default
        self.selected_player_idx = tk.IntVar(value=0)

        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(self, text="Choose a Challenge & Player", font=('Montserrat', 16), bg="#cceeff")
        header.pack(fill="x", pady=20)

        # Challenge options
        challenge_frame = tk.LabelFrame(self, text="Challenge Type", font=('Montserrat', 12))
        challenge_frame.pack(pady=10)

        challenges = [
            ("Mathematics", "Mathematics"),
            ("Logic", "Logic"),
            ("Chance", "Chance"),
            ("Père Fouras’ Riddle", "Riddle"),
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
        self.team_data = team_data

        # Clear old radio buttons
        for widget in self.players_frame.winfo_children():
            widget.destroy()

        self.selected_player_idx.set(0)  # default first player

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

        if chosen_challenge == "Mathematics":
            # Go to MathChallengeFrame
            math_frame = self.controller.frames["MathChallengeFrame"]
            math_frame.set_chosen_player(chosen_player)
            self.controller.show_frame("MathChallengeFrame")
        else:
            # Placeholder for other challenge types
            tk.Label(
                self,
                text=f"'{chosen_challenge}' is not implemented yet!",
                font=('Montserrat', 12),
                fg="red"
            ).pack()


# ------------------------- Page 4: Math Challenge Frame -------------------------
class MathChallengeFrame(tk.Frame):
    """
    Randomly picks one of the math sub-challenges (factorial, roulette, or linear eqn).
    The user enters the answer in an Entry, clicks Submit, and sees the result.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.chosen_player = None
        self.challenge_text = ""
        self.correct_answer = None

        self.instruction_label = None
        self.answer_entry = None
        self.result_label = None

        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(self, text="Mathematics Challenge", font=('Montserrat', 16), bg="#ffd1d1")
        header.pack(fill="x", pady=20)

        self.instruction_label = tk.Label(self, text="", font=('Montserrat', 12))
        self.instruction_label.pack(pady=10)

        self.answer_entry = tk.Entry(self, font=('Montserrat', 12), width=15)
        self.answer_entry.pack(pady=5)

        submit_button = tk.Button(
            self,
            text="Submit",
            font=('Montserrat', 12),
            command=self.check_answer
        )
        submit_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=('Montserrat', 12))
        self.result_label.pack(pady=5)

        back_button = tk.Button(
            self,
            text="<- Back to Challenge Selection",
            font=('Montserrat', 12),
            command=lambda: self.controller.show_frame("ChallengeFrame")
        )
        back_button.pack(pady=10)

    def set_chosen_player(self, player):
        self.chosen_player = player
        self.init_challenge()

    def init_challenge(self):
        self.result_label.config(text="")
        self.answer_entry.delete(0, tk.END)

        self.challenge_text, self.correct_answer = random_math_challenge()
        self.instruction_label.config(text=self.challenge_text)

    def check_answer(self):
        user_input_str = self.answer_entry.get().strip()
        if not user_input_str:
            self.result_label.config(text="Please enter a number!", fg="red")
            return

        try:
            # If correct_answer is int, parse user as int
            if isinstance(self.correct_answer, int):
                user_val = int(user_input_str)
                if user_val == self.correct_answer:
                    self.result_label.config(text="Well Done! You won a key.", fg="green")
                else:
                    self.result_label.config(text="You failed...", fg="red")
            else:
                # correct_answer is float
                user_val = float(user_input_str)
                if abs(user_val - self.correct_answer) < 1e-7:
                    self.result_label.config(text="Well Done! You won a key.", fg="green")
                else:
                    self.result_label.config(
                        text=f"You failed... (Correct was {self.correct_answer:.2f})",
                        fg="red"
                    )
        except ValueError:
            self.result_label.config(text="Invalid number format!", fg="red")


# ------------------------- Run the Application -------------------------
if __name__ == "__main__":
    app = FortBoyardApp()
    app.mainloop()
