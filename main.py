###################################################
#                                                 #
#              LANGUAGE LEARNING APP              #
#                                                 #
###################################################

import os
from tkinter import Tk, ttk, PhotoImage, N, NE, E, SE, S, SW, W, NW

decider = ["Answer.TLabel", "Solution.TLabel"]
en_fi = {
    "I": "minä",
    "you": "sinä"
}
en_fi_keys = list(en_fi.keys())

root = Tk()
root.title("Language Learning App")

style = ttk.Style()
style.configure(
    "Mainframe.TFrame",
    background="#1B4DD6")
style.configure(
    "Word.TLabel",
    font=("Arial", 24, "bold"),
    foreground="white",
    background="#1B4DD6")
style.configure(
    "Solution.TLabel",
    font=("Arial", 16, "bold"),
    foreground="#00FF00",
    background="#1B4DD6")
style.configure(
    "Answer.TLabel",
    font=("Arial", 16, "bold"),
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
    style="Mainframe.TFrame")
mainframe.grid(
    column=0,
    row=0,
    sticky=(NE, SE, SW, NW))

open = ttk.Button(
    mainframe,
    image=open_img,
    padding=(50, 100)
    ).grid(column=0, row=0, sticky=NW)
play = ttk.Button(
    mainframe,
    image=play_img,
    padding=(50, 50)
    ).grid(column=2, row=1, sticky=SE)
rand = ttk.Button(
    mainframe,
    image=rand_img,
    padding=(50, 100)
    ).grid(column=2, row=0, sticky=NE)
stop = ttk.Button(
    mainframe,
    image=stop_img,
    padding=(50, 50)
    ).grid(column=0, row=1, sticky=SW)

word = ttk.Label(
        mainframe,
        text=en_fi_keys[1],
        style="Word.TLabel",
        padding=(100, 20)
        ).grid(column=1, row=0, sticky=N)
solution = ttk.Label(
        mainframe,
        text="",#"Solution",
        style="Solution.TLabel",
        padding=(170, 30)
        ).grid(column=1, row=0, sticky=(E, W))
answer = ttk.Label(
        mainframe,
        text="",#"Answer",
        style=decider[0],
        padding=(80, 20)
        ).grid(column=1, row=0, sticky=(S))
translation = ttk.Entry(
        mainframe,
        font=("Arial", 24, "bold"),
        justify="center"
        ).grid(column=1, row=1, sticky=(E, W))

root.mainloop()
