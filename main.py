import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("1000x800")
root.resizable(width=False, height=False)

title = tk.Label(root, text="Hello Adventurer, welcome to our Fort Boyard Game !", font=('Montserrat', 26))### label is gonna be part of root, and the label will be helloworld
rule = tk.Label(root, text="To win the game, you must complete challenges in order to earn keys. With 3 keys, you shall open the treasure room !", font=('Montserrat', 20), wraplength=(700))
create_team_prompt = tk.Label(root, text="Now, enter below the number of player you want in your team, and click start !", font=('Montserrat', 26))
numberBox = ttk.Combobox(root, values=["1", "2", "3"], font=('Montserrat', 20), state="readonly")
startButton = tk.Button(root, text="Start", font=('Montserrat', 15), height=5, width=20, )
title.pack(padx=20, pady=20) ## place the label on the root
rule.pack(padx=20, pady=30)
create_team_prompt.pack(padx=20, pady=50)
numberBox.pack(padx=20, pady=55)
startButton.pack(padx=20, pady=20)
root.title("Fort Boyard Game - Amel and Tom ")
root.mainloop()