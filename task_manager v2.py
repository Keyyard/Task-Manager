import PySimpleGUI as sg

tasks = []

def read_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            tasks.extend(file.read().splitlines())
    except FileNotFoundError:
        pass

def write_tasks_to_file():
    with open("tasks.txt", "w") as file:
        for idx, task in enumerate(tasks, start=1):
            file.write(f"{idx}. {task}\n")

read_tasks_from_file()

layout = [
    [sg.InputText(key='task_input', expand_x=True), sg.Button("Add")],
    [sg.Text("Current tasks:")],
    [sg.Listbox(values=tasks, expand_x=True, expand_y=True, key='task_list')],
    [sg.Button("Remove Selected Task(s)", expand_x=True, size=(20, 1))],
    [sg.Button("Exit")]
]

sg.theme('DarkGreen')
window = sg.Window("Task Manager", layout, size=(400, 400))

run = True
while run:
    events, values = window.read()
    selected_task_indexes = window['task_list'].get_indexes()
    if events == sg.WINDOW_CLOSED or events == "Exit":
        run = False
    elif (events == "Add") or (events == 'task_input' and sg.WINDOW_KEYS['Return']):
        task = values['task_input']
        tasks.append(task)
        tasks.sort()
        write_tasks_to_file()
        window['task_input'].update('')
        window['task_list'].update(values=tasks)
    elif events == "Remove Selected Task(s)":
        try:
            for idx in selected_task_indexes:
                tasks.pop(idx)
        except:
            pass
        write_tasks_to_file()
        window['task_list'].update(values=tasks)

window.close()
