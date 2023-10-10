import os
from time import sleep

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
while option != "3":
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
