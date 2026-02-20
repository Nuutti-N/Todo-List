# Todo list


import sys
from colorama import Fore
import json


def headlines():

    print("=== TODO LIST ==")

    return


def read():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        print(data.items())
        return data
    except FileNotFoundError:
        return []


def menu():
    print("Todo list, includes these functions.")
    print("1. Add task")
    print("2. Remove task")
    print("3. Mark complete")
    print("4. View all tasks")
    print("0. Exit")
    choose = int(input("Enter you choice: "))

    return choose


def add(Line):
    Add = input("Enter add the task: ")
    if Add == "":
        print("Task cannot be empty!")
    else:
        Line.append(Add)
        print("✔ Task added!")

    return Line


def Remove(Line):
    try:
        # Firstly, asking what you want to remove, or nothing.
        Remove = int(input("Enter Remove the number: "))
        if Remove == "":
            print("Task cannot be empty!")
        else:
            Line.pop(Remove - 1)
            print("Task removed")
    except Exception:
        print("error, check the task")

    return Line


def Mark(Line):
    mark = int(input("Enter the task number to mark as done: "))
    if 0 <= mark < len(Line):
        Line[mark-1] = "✔ " + Line[mark-1]
        print("Task marked done!")
    else:
        print("Invalid task number.")
    return Line


def View(Line):
    if len(Line) == 0:
        print("No Tasks yet! ✘")
    else:
        for numbers, tasks in enumerate(Line, 1):
            print("📋 Tasks!")
            print(f"{numbers}. {tasks}")

    return Line


def write(Line):
    with open("data.json", "w") as f:
        json.dump(Line, f)

    return


def main():
    Line = read()
    write(Line)
    while True:
        choose = menu()
        if choose == 1:
            add(Line)
            write(Line)
            print()
        elif choose == 2:
            Remove(Line)
            write(Line)
            print()
        elif choose == 3:
            Mark(Line)
            write(Line)
            print()
        elif choose == 4:
            View(Line)
            print()
        elif choose == 0:
            write(Line)
            print("You regret the decision to EXIT!")
            break
    print("Glad you completed your tasks for the day.")
    return


# main() # If I put this only, this will work right away
if __name__ == "__main__":
    main()
