import os
from time import sleep
import PySimpleGUI as sg
tasks = []

def read_tasks_from_file():
    try: # Try to read from file
        with open("tasks.txt", "r") as file:
            tasks.extend(file.read().splitlines())
    except FileNotFoundError: # If file doesn't exist, just
        pass

def write_tasks_to_file():
    with open("tasks.txt", "w") as file: # write mode overwrites the file
        for task in tasks:
            file.write(f"{task}\n")

def add_task():
    os.system('cls')
    task = input("Enter a task: ")
    tasks.append(task)
    tasks.sort()
    write_tasks_to_file()

def remove_task():
    os.system('cls')
    task = int(input("Enter task's number: "))
    try:
        tasks.pop(task - 1)
        tasks.sort()
        write_tasks_to_file()
    except IndexError:
        print("Task not found.")
        sleep(1)

def menu():
    print("1 - Add task")
    print("2 - Remove task")
    print("3 - Exit")

def display_tasks():
    print("Current tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

read_tasks_from_file()
option = None
'''while option != "3":
    os.system('cls')
    menu()
    display_tasks()
    option = input("Enter your option: ")
    if option == "1":
        add_task()
    elif option == "2":
        remove_task()
    elif option == "3":
        write_tasks_to_file()  # Write tasks to file before exiting
        os.system('cls')
        '''
layout = [
        [sg.Text("Current tasks:")],
        [sg.Listbox(values=tasks, expand_x=True,expand_y=True, key='task_list')],
        [sg.InputText(key='task_input',expand_x=True)],
        [sg.Button("Add"), sg.Button("Remove",disabled=True), sg.Button("Exit")]
]
window = sg.Window("Task Manager", layout,size=(400,400))

run = True
while run:
    events, values = window.read()

    if events == sg.WINDOW_CLOSED or events == "Exit":
        run = False
    elif (events == "Add") or (events == 'task_input' and sg.WINDOW_KEYS['Return']):
        task = values['task_input']
        tasks.append(task)
        tasks.sort()
        write_tasks_to_file()
        window['task_input'].update('')
        window['task_list'].update(values=tasks)
    
    selected_task_indexes = window['task_list'].get_indexes()
    if len(selected_task_indexes) == 0:
        window['Remove'].update(disabled=True)
    else: 
        window["Remove"].update(disabled=False)

    if events == "Remove":
        try:
            tasks.pop(selected_task_indexes)
        except:
            pass
        write_tasks_to_file()
        window['task_list'].update(values=tasks)


window.close()