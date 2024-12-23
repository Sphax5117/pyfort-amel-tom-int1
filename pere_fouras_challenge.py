# app_frames.py (example location for your frame)
import tkinter as tk
from tkinter import ttk
import json
import random
import os


class PereFourasFrame(tk.Frame):
    """
    This frame presents a random Père Fouras riddle from data/PFRiddles.json.
    The user has 3 attempts to guess it.
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

        # Automatically load a random riddle at frame creation
        self.load_new_riddle()

    def load_new_riddle(self):
        """
        Pick a new random riddle from 'data/PFRiddles.json', reset attempts, and update the UI.
        """
        riddles = self.load_json("data/PFRiddles.json")
        chosen_riddle = random.choice(riddles)

        # Because each entry is a dict like {"riddle": "...", "answer": "..."}
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
        # In case we run from a different working directory, ensure the path is correct
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
        Compare the user's input to the riddle's correct answer.
        """
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.current_riddle_answer.strip().lower()

        # If correct
        if user_answer == correct_answer:
            self.result_label.config(text="Well done, you won a key!", fg="green")
        else:
            # Decrement attempts
            self.attempts_left -= 1
            self.update_attempt_label()

            if self.attempts_left <= 0:
                self.result_label.config(
                    text=f"You lost... The answer was: '{self.current_riddle_answer}'",
                    fg="red"
                )
            else:
                self.result_label.config(text="Wrong answer, try again!", fg="red")
