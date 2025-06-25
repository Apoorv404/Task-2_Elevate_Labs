TASK_FILE = "tasks.txt"

def load_tasks(tasks):
    try:
        with open(TASK_FILE, "r") as file:
            tasks.extend([line.strip() for line in file.readlines()])
    except FileNotFoundError:
        print("No existing tasks found.")

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter a task to add: ").strip()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        idx = int(input("Enter task number to remove: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

tasks = []
load_tasks(tasks)
while True:
    print("\nOptions: [1] View [2] Add [3] Remove [4] Exit")
    choice = input("Select an option: ").strip()
    if choice == "1":
        view_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        print("Exiting. Bye!")
        break
    else:
        print("Invalid choice. Try again.")
