import os
from CRUD import *
from datetime import datetime
from tabulate import tabulate

def clean():
    os.system("cls")

def show_tasks():
    tasks=watch_tasks()
    headers=["ID", "Task Name", "Date", "Status"]
    data=[]
    for x, obj in tasks.items():
        new_row = []
        new_row.append(x)
        for y in obj:
            new_row.append(obj[y])
        data.append(new_row)
    print(" ")
    print("🚨 Hey! Your tasks list is:")
    print(tabulate(data, headers=headers, tablefmt="grid"))

def add_new_task():
    name = input("What is the task that you want to add? ")
    print("If your task is still undone -> Type Pending")
    print("If your task is done -> Type Done")
    status = input("Please, type the task status: ")
    print(add_task(name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status))

def edit_task():
    #Initial version (forgetting that kwargs transports a dict to the CRUD)
    '''
    name=""
    date=None
    status=""
    show_tasks()
    task_id = input("Please, select the ID of the task that you want to modify: ")
    name = input("Type the new name of your task (if you don't want to modify, please ENTER to continue): ")
    print("If your task is still undone -> Type Pending")
    print("If your task is done -> Type Done")
    status = input("Type the new status of your task (if you don't want to modify, please ENTER to continue): ")
    if (name == "" and status == ""):
        print("No updates detected.")
    elif (name != "" and status == ""):
        print(update_task(task_id, title = name, date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    elif (name == "" and status != ""):
        print(update_task(task_id,  date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status = status))
    else:
        print(update_task(task_id, title = name, date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), status = status))
    '''
    #Official version (kwargs as dictionary + exceptions management: )
    show_tasks()

    task_id = input("Please, select the ID of the task that you want to modify: ")

    name = input(
        "Type the new name of your task "
        "(press ENTER to keep the current one): "
    )

    print("If your task is still undone -> Type Pending")
    print("If your task is done -> Type Done")

    status = input(
        "Type the new status of your task "
        "(press ENTER to keep the current one): "
    )

    fields = {}

    if name:
        fields["title"] = name

    if status:
        fields["status"] = status

    if fields:
        fields["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(update_task(task_id, **fields))
    else:
        print("No updates detected.")
        
def delete_current_task():
    show_tasks()
    task_id = input("Please, type the ID of the task that you want to delete: ")
    print(delete_task(task_id))

def show_cli():
    while True:
        clean()
        print("===  My Task Manager (CLI VERSION) ===")
        print("1. Watch all your tasks 🔍")
        print("2. Create your own task ✅")
        print("3. Edit your task ✏️")
        print("4. Remove a task ❌")
        print("5. Exit the Task Manager 👋😭")
        option = input("Please choose an option: ")

        if option == "1":
            show_tasks()
            input("\nPress ENTER to continue...")

        elif option == "2":
            add_new_task()
            input("\nPress ENTER to continue...")

        elif option == "3":
            edit_task()
            input("\nPress ENTER to continue...")

        elif option == "4":
            delete_current_task()
            input("\nPress ENTER to continue...")

        elif option == "5":
            print("👋 Bye bye, see you next time 💜")
            break
