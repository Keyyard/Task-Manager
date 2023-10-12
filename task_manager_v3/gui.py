
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PyPractice\Task Manager\Task_Manager_V3\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
tasks = []
window.geometry("570x452")
window.configure(bg = "#99D67D")


canvas = Canvas(
    window,
    bg = "#99D67D",
    height = 452,
    width = 570,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    285,
    30.0,
    text="TASK MANAGER",
    fill="#FFFFFF",
    font=("Inter", 28 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png")) # this is the entry box image
entry_bg_1 = canvas.create_image(
    238.5,
    66.0,
    image=entry_image_1 # this is the entry box image linked
) 
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
) #this is the entry box
entry_1.place(
    x=17.0,
    y=56.0,
    width=443.0,
    height=18.0
) #this is the entry box placement, it is placed on the canvas

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    287.0,
    240.5,
    image=entry_image_2
)
board = Text(
    bd=0,
    bg="#F7F7F7",
    fg="#000716",
    highlightthickness=0,
    state='disabled'
)
board.place(
    x=19.0,
    y=89.0,
    width=536.0,
    height=301.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_add = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add(),
    relief="flat"
)
button_add.place(
    x=481.0,
    y=56.0,
    width=74.0,
    height=21.0
)    

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png")),
button_remove = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
button_remove.place(
    x=479.0,
    y=405.0,
    width=74.0,
    height=21.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_remove = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: remove(),
    relief="flat"
)
button_remove.place(
    x=17.0,
    y=402.0,
    width=443.0,
    height=19.0
)

def board_update():
    board.config(state='normal')
    board.delete('1.0', 'end')
    for task in tasks:
        board.insert('end', task + '\n')
    board.config(state='disabled')

def add():
    task = entry_1.get()
    if task != '':
        tasks.append(task)
        entry_1.delete(0, 'end')
        board_update()

def remove():
    tasks.pop(0)
    tasks.sort()
    board_update()

board_update()

window.resizable(False, False)
window.mainloop()