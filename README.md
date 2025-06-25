# To-Do App

A simple and efficient command-line To-Do list application built with Python. This project was created as part of Task 2 for the Elevate Labs Internship.

## Features

- Add new tasks
- View all tasks
- Remove tasks by number
- Persistent storage (tasks are saved between sessions)
- Simple and intuitive command-line interface
- Error handling for invalid inputs

## How to Use

1. Make sure you have Python installed on your system
2. Clone this repository
3. Run the To-Do app:
   ```bash
   python todo.py
   ```
4. Use the following commands:
   - Press `1` to view all tasks
   - Press `2` to add a new task
   - Press `3` to remove a task
   - Press `4` to exit the application

## Project Structure

- `todo.py`: Main program file containing the To-Do list logic
- `tasks.txt`: File that stores the tasks persistently
- `LICENSE`: Project license file
- `README.md`: This documentation file

## How it Works

The application implements basic task management functionality using Python with the following features:
- File-based storage for persistent data
- List-based task management
- Simple command-line menu interface
- Error handling for file operations and user inputs
- Automatic task numbering for easy reference

### Functions

- `load_tasks()`: Loads existing tasks from the file
- `save_tasks()`: Saves current tasks to the file
- `add_task()`: Adds a new task to the list
- `view_tasks()`: Displays all current tasks
- `remove_task()`: Removes a task by its number

## Data Storage

Tasks are stored in a simple text file (`tasks.txt`), with one task per line. This makes the data easy to read and modify if needed.
