from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, Spinbox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\PyPractice\Task Manager\Task_Manager_V3\assets\frame0")
TASKS_FILE = OUTPUT_PATH / "tasks.txt"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def save_tasks_to_file():
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def load_tasks_from_file():
    if TASKS_FILE.exists():
        with open(TASKS_FILE, 'r') as file:
            return [line.strip() for line in file]
    return []

window = Tk()
tasks = load_tasks_from_file()
window.geometry("570x452")
window.configure(bg="#99D67D")

canvas = Canvas(
    window,
    bg="#99D67D",
    height=452,
    width=570,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_text(
    285,
    30.0,
    text="TASK MANAGER",
    fill="#FFFFFF",
    font=("Inter", 28 * -1)
)

entry_bg_1 = canvas.create_rectangle(
    17.0, 56.0, 460.0, 74.0,
    fill="#FFFFFF",
    outline=""
)
task_input = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
task_input.place(
    x=17.0,
    y=56.0,
    width=443.0,
    height=18.0
)

entry_bg_2 = canvas.create_rectangle(
    19.0, 89.0, 555.0, 390.0,
    fill="#F7F7F7",
    outline=""
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

button_add = Button(
    bg="#4096C6",
    fg="#FFFFFF",
    text="ADD",
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

button_remove = Button(
    bg="#4096C6",
    fg="#FFFFFF",
    text="REMOVE",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: remove(),
    relief="flat",
)
button_remove.place(
    x=17.0,
    y=402.0,
    width=443.0,
    height=19.0
)

task_select = Spinbox(
    from_=0.0,
    to=100.0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
task_select.place(
    x=515.0,
    y=402.0,
    width=40.0,
    height=19.0
)
spinbox_text = canvas.create_text(
    490.0,
    410.0,
    text="Task no.",
    fill="#ffffff",
    font=("Inter", 10)
)

def board_update():
    board.config(state='normal')
    board.delete('1.0', 'end')
    for task in tasks:
        board.insert('end', task + '\n')
    board.config(state='disabled')

def add():
    task = task_input.get()
    if task != '':
        tasks.append(task)
        task_input.delete(0, 'end')
        save_tasks_to_file()
        board_update()

def remove():
    if tasks:
        try:
            tasks.pop(
                int(task_select.get()) - 1
            )
        except:
            pass
        tasks.sort()
        save_tasks_to_file()
        board_update()

board_update()

window.resizable(False, False)
window.mainloop()
