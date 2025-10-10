import os
import tkinter as tk
from typing import Union
from tkinter import ttk, PhotoImage
from random import choice
from tkinter import Tk, NORMAL
from utils.constants import COLORS, FONTS, INTEGERS, STYLES, TYPES

def check_attempt(solution: ttk.Label, attempt: ttk.Label) -> None:
    if solution.cget("text") == attempt.cget("text"):
        attempt.config(style=STYLES["correct"])
    else:
        attempt.config(style=STYLES["incorrect"])
    return None

def check_data_key_index(data_keys: list[str], data_key_index: int) -> int:
    if data_key_index + INTEGERS["one"] == len(data_keys):
        data_key_index = INTEGERS["zero"]
    else:
        data_key_index += INTEGERS["one"]
    return data_key_index

def clear_input(user_input: ttk.Entry) -> None:
    user_input.delete(INTEGERS["zero"], tk.END)
    user_input.focus()
    return None

def create_button(mainframe: ttk.Frame, image: PhotoImage,\
        padding: tuple[int, int], command: str, state: str = NORMAL) ->\
        ttk.Button:
    return ttk.Button(
            mainframe,
                image=image,
                    padding=padding,
                        command=command,
                            state=state)

def create_entry(mainframe: ttk.Frame) -> ttk.Entry:
    return ttk.Entry(
            mainframe,
                font=FONTS,
                    justify="center")

def create_frame(root: Tk) -> ttk.Frame:
    return ttk.Frame(
            root,
                padding=INTEGERS["zero"],
                    style=STYLES["mainframe"])

def create_image(image: str) -> PhotoImage:
    return PhotoImage(
            file=os.path.join(
                os.path.dirname(
                    os.path.abspath(__file__)),
                        '..',
                            'images', image))

def create_label(mainframe: ttk.Frame, text: str, style: str,\
        padding: int = INTEGERS["zero"]) -> ttk.Label:
    return ttk.Label(
            mainframe,
                text=text,
                    style=style,
                        padding=padding,
                            width=INTEGERS["zero"])

def create_style(name: str, foreground: str = COLORS["black"]) -> ttk.Style:
    return ttk.Style().configure(
            name,
                foreground=foreground,
                    background=COLORS["custom_blue"],
                        font=FONTS)

def list_data_keys(data: dict[str, str]) -> list[str]:
    return list(data.keys())

def random_data_key(data_keys: list[str]) -> str:
    return choice(data_keys)

def set_config(element: ttk.Label, text: str) -> None:
    element.config(text=text)
    return None

def set_data_key(data_keys: list[str], data_key_index: int) -> str:
    return data_keys[data_key_index]

def set_grid(element: Union[ttk.Frame | ttk.Entry | ttk.Label | ttk.Button],\
        column, row, sticky) -> None:
    element.grid(column=column, row=row, sticky=sticky)
    return None

def set_index(data_keys: list[str], data_key: str) -> int:
    return data_keys.index(data_key)

def stop_released(
        data_key: str, data_keys: list, solution: ttk.Label,\
        attempt: ttk.Label, data: dict[str, str], user_input: ttk.Entry,\
        word: ttk.Label, stop_btn: ttk.Button) -> tuple[list[str], str, int,\
        int, Union[bool | None]]:
    set_config(solution, data[word.cget("text")])
    set_config(attempt, user_input.get())
    check_attempt(solution, attempt)
    data_key_index = set_index(data_keys, data_key)
    data_key_index = check_data_key_index(data_keys, data_key_index)
    data_key = set_data_key(data_keys, data_key_index)
    stop_btn["state"] = NORMAL
    stop_here = TYPES["false"]
    play_counter = INTEGERS["one"]
    clear_input(user_input)
    return data_keys, data_key, data_key_index, play_counter, stop_here
