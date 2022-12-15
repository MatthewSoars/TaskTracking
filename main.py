# Simple Time task tracking app
import pandas as pd
import numpy as np

todo_list = pd.read_excel(r'List.xlsx')
todo_list_np = todo_list.to_numpy()
running = True


def Welcome():
    # Welcome messages and instructions
    print("Welcome to the Time Tracker App")
    print("1. Start a new task")
    print("2. Stop a task")
    print("3. View all tasks")
    print("4. Exit")
    print("Please select an option from the list above (1, 2, 3, or 4):")
    return input()


def StartTask():
    # Starts a new task and add it to the list
    item = input(print("Enter the name of the task:"))
    return item


def StopTask():
    # Stops a task removing it from the list
    ViewTasks()
    item_loc = input("Enter the number of the task you wish to delete:")
    return item_loc


def ViewTasks():
    # Displays all tasks in the list
    print(todo_list_np)
    print(' ')
    return


while running:
    Response = Welcome()
    if Response == "1":
        value = StartTask()
        # todo_list.loc[len(todo_list)] = value
        todo_list_np = np.append(todo_list_np, value)

    elif Response == "2":
        value = int(StopTask()) - 1
        todo_list_np = np.delete(todo_list_np, value)

    elif Response == "3":
        ViewTasks()

    elif Response == "4":
        todo_list = pd.DataFrame(todo_list_np)
        todo_list.to_excel(r'List.xlsx', index=False)
        running = False
