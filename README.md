# TODO LIST CLI 📋 

A simple command-line todo list application built with python. 


## Features 
- Add tasks
- Remove tasks
- Mark tasks as complete
- View all tasks
- Saves tasks automatically to JSON

## Requirements

- Python 3.xx
- colorama (`pip install colorama`)

## Usage 
choose an option from the menu 
- `1` Add task
- `2` Remove task
- `3` Mark complete
- `4` View all tasks
- `0` Exit
  
## Commands

Add a task:
python todo.py add "Buy groceries"

List all tasks:
python todo.py list

Mark as done:
python todo.py done 1

Delete a task:
python todo.py delete 1

## Installation 
git clone https://github.com/your-username/todo-cli.git
cd todo-cli
pip install colorama

## File structure
```
todo/
├── todo.py
├── data.json   # created automatically
└── README.md
