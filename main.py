
###############################################################################
#                                                                             #
#                          LANGUAGE LEARNING APP 2025                         #
#                                                                             #
###############################################################################


import json
from random import choice
from tkinter import Tk, filedialog, DISABLED, NORMAL, N, NE, E, SE, S, SW, W,\
    NW
from utils.constants import COLORS, INTEGERS, STRINGS, STYLES, TYPES
from utils.helpers import check_attempt, check_data_key_index, clear_input,\
    create_button, create_entry, create_frame, create_image, create_label,\
    create_style, list_data_keys, random_data_key, set_config, set_data_key,\
    set_grid, set_index, stop_released

# Variables
data = TYPES["none"]
data_keys = list(data.keys()) if data is not TYPES["none"] else TYPES["none"]
data_key = choice(data_keys) if data is not TYPES["none"] else TYPES["none"]
data_key_index = data_keys.index(data_key) if data is not TYPES["none"] else\
    TYPES["none"]
play_counter = INTEGERS["zero"]
stop_here = TYPES["false"]

## Button functions
def open_file():
    global data, data_keys, data_key, data_key_index, play_counter
    opened_file = filedialog.askopenfilename(
        title=STRINGS["select_file"],
        filetypes=[("Text files", "*.txt")]
    )
    if opened_file:
        with open(opened_file, STRINGS["read"], encoding=STRINGS["utf_8"])\
                as json_file:
            data = json.load(json_file)
            data_keys = list_data_keys(data)
            data_key = random_data_key(data_keys)
            data_key_index = set_index(data_keys, data_key)
            set_config(word, data_key)
            play_counter = INTEGERS["zero"]
            play_btn["state"] = NORMAL
            rand_btn["state"] = NORMAL
            stop_btn["state"] = NORMAL
            set_config(solution, STRINGS["empty_string"])
            set_config(attempt, STRINGS["empty_string"])
            root.bind(STRINGS["return"], lambda _: next_word())
    clear_input(user_input)
    return

def next_word():
    global data_keys, data_key, data_key_index, play_counter, stop_here
    if stop_here:
        data_keys, data_key, data_key_index, play_counter, stop_here =\
            stop_released(data_key, data_keys, solution, attempt, data,\
                          user_input, word, stop_btn)
        return
    if play_counter == INTEGERS["one"]:
        set_config(word, data_key)
        play_counter = INTEGERS["zero"]
        set_config(solution, STRINGS["empty_string"])
        set_config(attempt, STRINGS["empty_string"])
    else:
        set_config(solution, data[data_key])
        set_config(attempt, user_input.get())
        play_counter += INTEGERS["one"]
        data_key_index = set_index(data_keys, data_key)
        data_key_index = check_data_key_index(data_keys, data_key_index)
    check_attempt(solution, attempt)
    data_key = set_data_key(data_keys, data_key_index)
    clear_input(user_input)
    return

def rand_word():
    global data_keys, data_key, data_key_index, play_counter, stop_here
    if stop_here:
        data_keys, data_key, data_key_index, play_counter, stop_here =\
            stop_released(data_key, data_keys, solution, attempt, data,\
                          user_input, word, stop_btn)
        return
    data_key = random_data_key(data_keys)
    data_key_index = set_index(data_keys, data_key)
    set_config(word, data_key)
    play_counter = INTEGERS["zero"]
    set_config(solution, STRINGS["empty_string"])
    set_config(attempt, STRINGS["empty_string"])
    clear_input(user_input)
    return

def stop_words():
    global stop_here, play_counter
    if not stop_here:
        stop_here = TYPES["true"]
        stop_btn["state"] = DISABLED
    set_config(solution, STRINGS["empty_string"])
    set_config(attempt, STRINGS["empty_string"])
    clear_input(user_input)
    return

# Setup
root = Tk()
root.title("Language Learning App")
root.wm_resizable(TYPES["false"], TYPES["false"])
style = create_style(STYLES["mainframe"])
style = create_style(STYLES["word"], COLORS["white"])
style = create_style(STYLES["correct"], COLORS["green"])
style = create_style(STYLES["incorrect"])
mainframe = create_frame(root)
user_input = create_entry(mainframe)
app_img = create_image('app.ico')
open_img = create_image('open.png')
play_img = create_image('play.png')
rand_img = create_image('rand.png')
stop_img = create_image('stop.png')
root.iconphoto(TYPES["false"], app_img)
word = create_label(mainframe, data_key, STYLES["word"])
solution = create_label(mainframe, STRINGS["empty_string"], STYLES["correct"])
attempt = create_label(mainframe, STRINGS["empty_string"],\
            STYLES["incorrect"], INTEGERS["five"])
open_btn = create_button(mainframe, open_img, (INTEGERS["fifty"],\
    INTEGERS["one_hundred"]), open_file)
play_btn = create_button(mainframe, play_img, (INTEGERS["fifty"],\
    INTEGERS["fifty"]), next_word, DISABLED)
rand_btn = create_button(mainframe, rand_img, (INTEGERS["fifty"],\
    INTEGERS["one_hundred"]), rand_word, DISABLED)
stop_btn = create_button(mainframe, stop_img, (INTEGERS["fifty"],\
    INTEGERS["fifty"]), stop_words, DISABLED)
set_grid(mainframe, INTEGERS["zero"], INTEGERS["zero"], (NE, SE, SW, NW))
set_grid(user_input, INTEGERS["one"], INTEGERS["one"], (E, W))
set_grid(word, INTEGERS["one"], INTEGERS["zero"], N)
set_grid(solution, INTEGERS["one"], INTEGERS["zero"], S)
set_grid(attempt, INTEGERS["one"], INTEGERS["one"], S)
set_grid(open_btn, INTEGERS["zero"], INTEGERS["zero"], NW)
set_grid(play_btn, INTEGERS["two"], INTEGERS["one"], SE)
set_grid(rand_btn, INTEGERS["two"], INTEGERS["zero"], NE)
set_grid(stop_btn, INTEGERS["zero"], INTEGERS["one"], SW)

root.mainloop()
