import os
import tkinter as tk
from tkinter import ttk, PhotoImage
from random import choice
from tkinter import NORMAL
from utils.constants import COLORS, FONTS, INTEGERS, STYLES, TYPES

def check_attempt(solution, attempt):
    if solution.cget("text") == attempt.cget("text"):
        attempt.config(style=STYLES["correct"])
    else:
        attempt.config(style=STYLES["incorrect"])
    return

def check_data_key_index(data_keys, data_key_index):
    if data_key_index + INTEGERS["one"] == len(data_keys):
        data_key_index = INTEGERS["zero"]
    else:
        data_key_index += INTEGERS["one"]
    return data_key_index

def clear_input(user_input):
    user_input.delete(INTEGERS["zero"], tk.END)
    user_input.focus()
    return

def create_button(mainframe, image, padding, command, state=NORMAL):
    return ttk.Button(
            mainframe,
                image=image,
                    padding=padding,
                        command=command,
                            state=state)

def create_entry(mainframe):
    return ttk.Entry(
            mainframe,
                font=FONTS,
                    justify="center")

def create_frame(root):
    return ttk.Frame(
            root,
                padding=INTEGERS["zero"],
                    style=STYLES["mainframe"])

def create_image(image):
    return PhotoImage(
            file=os.path.join(
                os.path.dirname(
                    os.path.abspath(__file__)),
                        '..',
                            'images', image))

def create_label(mainframe, text, style, padding=INTEGERS["zero"]):
    return ttk.Label(
            mainframe,
                text=text,
                    style=style,
                        padding=padding,
                            width=INTEGERS["zero"])

def create_style(name, foreground=COLORS["black"]):
    return ttk.Style().configure(
            name,
                foreground=foreground,
                    background=COLORS["custom_blue"],
                        font=FONTS)

def list_data_keys(data):
    return list(data.keys())

def random_data_key(data_keys):
    return choice(data_keys)

def set_config(element, text):
    element.config(text=text)
    return

def set_data_key(data_keys, data_key_index):
    return data_keys[data_key_index]

def set_grid(element, column, row, sticky):
    element.grid(column=column, row=row, sticky=sticky)
    return

def set_index(data_keys, data_key):
    return data_keys.index(data_key)

def stop_released(
        data_key, data_keys, solution, attempt, data, user_input, word,\
        stop_btn):
    set_config(solution, data[word.cget("text")])
    set_config(attempt, user_input.get())
    check_attempt(solution, attempt)
    play_counter = INTEGERS["one"]
    stop_btn["state"] = NORMAL
    set_config(stop_btn, STYLES["white"])
    stop_here = TYPES["false"]
    data_key_index = set_index(data_keys, data_key)
    data_key_index = check_data_key_index(data_keys, data_key_index)
    data_key = set_data_key(data_keys, data_key_index)
    clear_input(user_input)
    return data_keys, data_key, data_key_index, play_counter, stop_here
