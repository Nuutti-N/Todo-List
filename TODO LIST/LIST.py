# Todo list


import sys
from colorama import Fore, Style
import json


def headlines():

    print(Style.BRIGHT + Fore.YELLOW + "=== TODO LIST ==")

    return


def read():
    try:
        with open("data.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        return []
    except FileNotFoundError:
        return []


def menu():
    print(Fore.WHITE + Style.BRIGHT + "Todo list, includes these functions.")
    print(Fore.CYAN + "1. Add task")
    print(Fore.CYAN + "2. Remove task")
    print(Fore.CYAN + "3. Mark complete")
    print(Fore.CYAN + "4. View all tasks")
    print(Fore.CYAN + "0. Exit")
    choose = int(input(Fore.YELLOW + "Enter you choice: "))

    return choose


def add(Line):
    Add = input(Fore.CYAN + "Enter add the task: ")
    if Add == "":
        print(Fore.RED + "Task cannot be empty!")
    else:
        Line.append(Add)
        print(Fore.GREEN + "✔ Task added!")
    return Line


def Remove(Line):
    try:
        # Firstly, asking what you want to remove, or nothing.
        Remove = int(input(Fore.CYAN + "Enter Remove the number: "))
        if Remove == "":
            print(Fore.RED + "Task cannot be empty!")
        else:
            Line.pop(Remove - 1)
            print(Fore.GREEN + "Task removed")
    except Exception:
        print("error, check the task")

    return Line


def Mark(Line):
    mark = int(input(Fore.CYAN + "Enter the task number to mark as done: "))
    if 0 <= mark < len(Line):
        Line[mark-1] = "✔ " + Line[mark-1]
        print(Fore.GREEN + "Task marked done!")
    else:
        print(Fore.RED + "Invalid task number.")
    return Line


def View(Line):
    if len(Line) == 0:
        print(Fore.RED + "No Tasks yet! ✘")
    else:
        print(Fore.YELLOW + Style.BRIGHT + "📋 Tasks!")
        for numbers, tasks in enumerate(Line, 1):
            print(f"{numbers}. {tasks}")

    return Line


def write(Line):
    with open("data.json", "w", encoding="UTF-8") as file:
        json.dump(Line, file)

    return


def main():
    headlines()
    Line = read()
    write(Line)
    while True:
        choose = menu()
        if choose == 1:
            Line = add(Line)
            write(Line)
            print()
        elif choose == 2:
            Line = Remove(Line)
            write(Line)
            print()
        elif choose == 3:
            Line = Mark(Line)
            write(Line)
            print()
        elif choose == 4:
            View(Line)
            print()
        elif choose == 0:
            write(Line)
            print(Fore.MAGENTA + "You regret the decision to EXIT!")
            break
    print(Fore.GREEN + Style.BRIGHT +
          "Glad you completed your tasks for the day.")
    return


# main() # If I put this only, this will work right away
if __name__ == "__main__":
    main()
