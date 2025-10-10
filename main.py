###############################################################################
#                                                                             #
#                          LANGUAGE LEARNING APP 2025                         #
#                                                                             #
###############################################################################

import json
from typing import Union
from ttkwidgets import tooltips  # type: ignore
from tkinter import Tk, filedialog, DISABLED, NORMAL, N, NE, E, SE, S, SW, W,\
    NW
from utils.constants import COLORS, INTEGERS, STRINGS, STYLES, TYPES
from utils.helpers import check_attempt, check_data_key_index, clear_input,\
    create_button, create_entry, create_frame, create_image, create_label,\
    create_style, list_data_keys, random_data_key, set_config, set_data_key,\
    set_grid, set_index, stop_released

## Variables
data: Union[bool | None] = TYPES["none"]
data_keys: Union[list[str] | bool | None] = TYPES["none"]
data_key: Union[str | bool | None] = TYPES["none"]
data_key_index: Union[int | None] = TYPES["none"]
play_counter: int = INTEGERS["zero"]
stop_here: Union[bool | None] = TYPES["false"]

## Buttons
# Open
def open_file():
    global data, data_keys, data_key, data_key_index, play_counter, stop_here
    opened_file = filedialog.askopenfilename(
        title=STRINGS["select_file"],
        filetypes=[("Text files", "*.txt")]
    )
    if opened_file:
        with open(opened_file, STRINGS["read"], encoding=STRINGS["utf_8"])\
                as json_file:
            
            if stop_here:
                stop_here = TYPES["false"]
                stop_btn["state"] = NORMAL
            data = json.load(json_file)
            data_keys = list_data_keys(data)
            data_key = random_data_key(data_keys)
            data_key_index = set_index(data_keys, data_key)
            play_btn["state"] = NORMAL
            rand_btn["state"] = NORMAL
            stop_btn["state"] = NORMAL
            play_counter = INTEGERS["zero"]
            set_config(word, data_key)
            set_config(solution, STRINGS["empty_string"])
            set_config(attempt, STRINGS["empty_string"])
            root.bind(STRINGS["return"], lambda _: next_word())
    clear_input(user_input)
    return TYPES["none"]

# Play
def next_word():
    global data_keys, data_key, data_key_index, play_counter, stop_here
    if stop_here:
        data_keys, data_key, data_key_index, play_counter, stop_here =\
            stop_released(data_key, data_keys, solution, attempt, data,\
                          user_input, word, stop_btn)
        return TYPES["none"]
    if play_counter == INTEGERS["one"]:
        play_counter = INTEGERS["zero"]
        set_config(word, data_key)
        set_config(solution, STRINGS["empty_string"])
        set_config(attempt, STRINGS["empty_string"])
    else:
        data_key_index = set_index(data_keys, data_key)
        data_key_index = check_data_key_index(data_keys, data_key_index)
        play_counter += INTEGERS["one"]
        set_config(solution, data[data_key])
        set_config(attempt, user_input.get())
    check_attempt(solution, attempt)
    data_key = set_data_key(data_keys, data_key_index)
    clear_input(user_input)
    return TYPES["none"]

# Random
def rand_word():
    global data_keys, data_key, data_key_index, play_counter, stop_here
    if stop_here:
        data_keys, data_key, data_key_index, play_counter, stop_here =\
            stop_released(data_key, data_keys, solution, attempt, data,\
                          user_input, word, stop_btn)
        return TYPES["none"]
    data_key = random_data_key(data_keys)
    data_key_index = set_index(data_keys, data_key)
    play_counter = INTEGERS["zero"]
    set_config(word, data_key)
    set_config(solution, STRINGS["empty_string"])
    set_config(attempt, STRINGS["empty_string"])
    clear_input(user_input)
    return TYPES["none"]

# Stop
def stop_words():
    global stop_here, play_counter
    if not stop_here:
        stop_here = TYPES["true"]
        stop_btn["state"] = DISABLED
    set_config(solution, STRINGS["empty_string"])
    set_config(attempt, STRINGS["empty_string"])
    clear_input(user_input)
    return TYPES["none"]

## Setup
# Frame and user input
root = Tk()
root.title("Language Learning App")
root.wm_resizable(TYPES["false"], TYPES["false"])  # type: ignore
mainframe = create_frame(root)
user_input = create_entry(mainframe)

# Style
style = create_style(STYLES["mainframe"])
style = create_style(STYLES["word"], COLORS["white"])
style = create_style(STYLES["correct"], COLORS["green"])
style = create_style(STYLES["incorrect"])

# Images
app_img = create_image('app.ico')
open_img = create_image('open.png')
play_img = create_image('play.png')
rand_img = create_image('rand.png')
stop_img = create_image('stop.png')
root.iconphoto(TYPES["false"], app_img)  # type: ignore

# Labels
word = create_label(mainframe, data_key, STYLES["word"])  # type: ignore
solution = create_label(mainframe, STRINGS["empty_string"], STYLES["correct"])
attempt = create_label(mainframe, STRINGS["empty_string"],\
            STYLES["incorrect"], INTEGERS["five"])

# Buttons
open_btn = create_button(mainframe, open_img, (INTEGERS["fifty"],\
    INTEGERS["one_hundred"]), open_file)  # type: ignore
play_btn = create_button(mainframe, play_img, (INTEGERS["fifty"],\
    INTEGERS["fifty"]), next_word, DISABLED)  # type: ignore
rand_btn = create_button(mainframe, rand_img, (INTEGERS["fifty"],\
    INTEGERS["one_hundred"]), rand_word, DISABLED)  # type: ignore
stop_btn = create_button(mainframe, stop_img, (INTEGERS["fifty"],\
    INTEGERS["fifty"]), stop_words, DISABLED)  # type: ignore

# Grid
set_grid(mainframe, INTEGERS["zero"], INTEGERS["zero"], (NE, SE, SW, NW))
set_grid(user_input, INTEGERS["one"], INTEGERS["one"], (E, W))
set_grid(word, INTEGERS["one"], INTEGERS["zero"], N)
set_grid(solution, INTEGERS["one"], INTEGERS["zero"], S)
set_grid(attempt, INTEGERS["one"], INTEGERS["one"], S)
set_grid(open_btn, INTEGERS["zero"], INTEGERS["zero"], NW)
set_grid(play_btn, INTEGERS["two"], INTEGERS["one"], SE)
set_grid(rand_btn, INTEGERS["two"], INTEGERS["zero"], NE)
set_grid(stop_btn, INTEGERS["zero"], INTEGERS["one"], SW)

# Tooltips
open_btn.configure(tooltip="Open File (JSON)")  # type: ignore
play_btn.configure(tooltip="Next Word")  # type: ignore
rand_btn.configure(tooltip="Random Word")  # type: ignore
stop_btn.configure(tooltip="Repeat Word")  # type: ignore
user_input.configure(tooltip="Type Translation Here")  # type: ignore

## Loop
root.mainloop()
