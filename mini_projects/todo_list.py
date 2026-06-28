"""
Mini Project: To-Do List
--------------------------
A simple command-line to-do list manager with add, view, complete,
and delete functionality. Persists tasks to a JSON file.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks, title):
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added: '{title}'")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "✔" if task["done"] else "✗"
        print(f"[{status}] {task['id']}. {task['title']}")
    print()


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Marked task {task_id} as done.")
            return
    print(f"No task found with id {task_id}.")


def delete_task(tasks, task_id):
    updated_tasks = [t for t in tasks if t["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        print(f"No task found with id {task_id}.")
        return
    save_tasks(updated_tasks)
    print(f"Deleted task {task_id}.")
    return updated_tasks


def run_menu():
    tasks = load_tasks()

    menu = """
=== To-Do List ===
1. View tasks
2. Add task
3. Mark task as done
4. Delete task
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ").strip()
            if title:
                add_task(tasks, title)
        elif choice == "3":
            try:
                task_id = int(input("Enter task id to complete: "))
                complete_task(tasks, task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task id to delete: "))
                result = delete_task(tasks, task_id)
                if result is not None:
                    tasks = result
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


def demo():
    print("--- Demo mode (no input required) ---")
    tasks = []
    add_task(tasks, "Learn Python basics")
    add_task(tasks, "Build a REST API")
    add_task(tasks, "Write unit tests")
    view_tasks(tasks)
    complete_task(tasks, 1)
    view_tasks(tasks)
    delete_task(tasks, 2)
    view_tasks(tasks)

    # Clean up the demo file so re-running stays fresh
    if os.path.exists(TASKS_FILE):
        os.remove(TASKS_FILE)


if __name__ == "__main__":
    demo()
    # Uncomment to run interactively:
    # run_menu()
