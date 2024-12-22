import tkinter as tk
from tkinter import ttk


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

        # Place each frame in the same row/column, so only one is visible at a time
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.team_creation_frame.grid(row=0, column=0, sticky="nsew")
        self.challenge_frame.grid(row=0, column=0, sticky="nsew")

        # Add frames to dictionary for easy access
        self.frames["MainFrame"] = self.main_frame
        self.frames["TeamCreationFrame"] = self.team_creation_frame
        self.frames["ChallengeFrame"] = self.challenge_frame

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
    Exactly one leader must exist:
      - If 0 leaders chosen, the first player is forced to be Leader.
      - If multiple leaders, keep only the first found.
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
        Validates the "exactly one leader" rule and finalizes the team data.
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


if __name__ == "__main__":
    app = FortBoyardApp()
    app.mainloop()
