###################################################
#                                                 #
#              LANGUAGE LEARNING APP              #
#                                                 #
###################################################

import os
import tkinter as tk
from random import choice
from tkinter import Tk, ttk, PhotoImage, N, NE, E, SE, S, SW, W, NW
from files.en_fi import data

decider = ["UserInput.TLabel", "Solution.TLabel"]
data_keys = list(data.keys())
learn_word = choice(data_keys)
data_key_index = data_keys.index(learn_word)
play_counter = 0

def next_data_key():
    global play_counter, learn_word, data_key_index
    if play_counter == 1:
        word.config(text=learn_word)
        solution.config(text="")
        attempt.config(text=user_input.get())
        play_counter = 0
    else:
        solution.config(text=data[learn_word])
        attempt.config(text=user_input.get())
        play_counter += 1
        data_key_index = data_keys.index(learn_word)
        if data_key_index + 1 == len(data_keys):
            data_key_index = 0
        else:
            data_key_index += 1
    learn_word = data_keys[data_key_index]
    user_input.delete(0, tk.END)

def rand_data_key():
    global play_counter, learn_word, data_key_index
    learn_word = choice(data_keys)
    data_key_index = data_keys.index(learn_word)
    word.config(text=learn_word)
    attempt.config(text=user_input.get())
    solution.config(text="")
    play_counter = 0
    user_input.delete(0, tk.END)

root = Tk()
root.title("Language Learning App")
root.bind('<Return>', lambda event: next_data_key())
root.wm_resizable(False, False)

style = ttk.Style()
style.configure(
    "MainFrame.TFrame",
    background="#1B4DD6")
style.configure(
    "Word.TLabel",
    font=("Arial", 24, "bold"),
    foreground="white",
    background="#1B4DD6")
style.configure(
    "Solution.TLabel",
    font=("Arial", 24, "bold"),
    foreground="#00FF00",
    background="#1B4DD6")
style.configure(
    "UserInput.TLabel",
    font=("Arial", 24, "bold"),
    background="#1B4DD6")

app_img = PhotoImage(
    file=os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'images', 'll_app.ico')
    )
open_img = PhotoImage(
    file=os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'images', 'open.png')
    )
play_img = PhotoImage(
    file=os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'images', 'play.png')
    )
rand_img = PhotoImage(
    file=os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'images', 'rand.png')
    )
stop_img = PhotoImage(
    file=os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), 'images', 'stop.png')
    )

root.iconphoto(False, app_img)
mainframe = ttk.Frame(
    root,
    padding=(0),
    style="MainFrame.TFrame")
mainframe.grid(
    column=0,
    row=0,
    sticky=(NE, SE, SW, NW))

open = ttk.Button(
    mainframe,
    image=open_img,
    padding=(50, 100)
    )
open.grid(column=0, row=0, sticky=NW)
play = ttk.Button(
    mainframe,
    image=play_img,
    padding=(50, 50),
    command=next_data_key
    )
play.grid(column=2, row=1, sticky=SE)
rand = ttk.Button(
    mainframe,
    image=rand_img,
    padding=(50, 100),
    command=rand_data_key
    )
rand.grid(column=2, row=0, sticky=NE)
stop = ttk.Button(
    mainframe,
    image=stop_img,
    padding=(50, 50)
    )
stop.grid(column=0, row=1, sticky=SW)

word = ttk.Label(
        mainframe,
        text=learn_word,
        style="Word.TLabel",
        width=0
        )
word.grid(column=1, row=0, sticky=N)
solution = ttk.Label(
        mainframe,
        text="",
        style="Solution.TLabel",
        width=0
        )
attempt = ttk.Label(
        mainframe,
        text="",
        style=decider[0],
        padding=(5),
        width=0
        )
attempt.grid(column=1, row=1, sticky=(S))

solution.grid(column=1, row=0, sticky=(S))
user_input = ttk.Entry(
        mainframe,
        font=("Arial", 24, "bold"),
        justify="center"
        )
user_input.grid(column=1, row=1, sticky=(E, W))
user_input.focus()

root.mainloop()
