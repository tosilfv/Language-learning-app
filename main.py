###################################################
#                                                 #
#              LANGUAGE LEARNING APP              #
#                                                 #
###################################################

from tkinter import Tk, Canvas, Label, Button, Entry, CENTER

window = Tk()
window.title("Language Learning App")
window.config(padx=40, pady=40, bg="white")

# Canvas
canvas = Canvas(width=200, height=200, bg="white")

# Word
word = Label(text="PUT_WORD_HERE", bg="white")
word.place(relx=0.5, rely=0.5, anchor=CENTER)

# Translation
translation = Label(text="PUT_TRANSLATION_HERE", bg="white")
translation.place(relx=0.5, rely=0.5, anchor=CENTER)

# Open file
open_file = Button(text="Open File", bg="white", highlightthickness=0)
open_file.place(relx=0.5, rely=0.5, anchor=CENTER)

# Previous word
previous_word = Button(text="Previous Word", bg="white", highlightthickness=0)
previous_word.place(relx=0.5, rely=0.5, anchor=CENTER)

# Next word
next_word = Button(text="Next Word", bg="white", highlightthickness=0)
next_word.place(relx=0.5, rely=0.5, anchor=CENTER)

# Sort by a to z
sort_by_atoz = Button(text="Sort by A to Z", bg="white", highlightthickness=0)
sort_by_atoz.place(relx=0.5, rely=0.5, anchor=CENTER)

# Sort by z to a
sort_by_ztoa = Button(text="Sort by Z to A", bg="white", highlightthickness=0)
sort_by_ztoa.place(relx=0.5, rely=0.5, anchor=CENTER)

# Show/hide translation
show_hide_trans = Button(
        text="Show/Hide\nTranslation", bg="white", highlightthickness=0
    )
show_hide_trans.place(relx=0.5, rely=0.5, anchor=CENTER)

# Sort by mixed
sort_by_mixed = Button(text="Sort by Mixed", bg="white", highlightthickness=0)
sort_by_mixed.place(relx=0.5, rely=0.5, anchor=CENTER)

# User input label
user_input_label = Label(text="Translation", bg="white")
user_input_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# User input
user_input = Entry(width=30)
user_input.place(relx=0.5, rely=0.5, anchor=CENTER)

# Check input
check_input = Button(text="Ok", bg="white", highlightthickness=0)
check_input.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()
