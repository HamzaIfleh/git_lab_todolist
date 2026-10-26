"""Simple command-line To-Do List."""

from tasks import add_task, get_tasks
from completion import complete_task, uncomplete_task
from removal import remove_task

MENU = """
1. List all tasks
2. List pending tasks
3. Add task
4. Complete task
5. Uncomplete task
6. Remove task
0. Quit
"""


def show(tasks):
    if not tasks:
        print("No tasks.")
    for task in tasks:
        mark = "x" if task["done"] else " "
        print(f"[{mark}] {task['id']}. {task['title']}")


def ask_id():
    text = input("Task id: ").strip()
    if not text.isdigit():
        raise ValueError("Task id must be a number")
    return int(text)


def main():
    tasks = []
    while True:
        print(MENU)
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                show(get_tasks(tasks))
            elif choice == "2":
                show(get_tasks(tasks, done=False))
            elif choice == "3":
                add_task(tasks, input("Title: "))
            elif choice == "4":
                complete_task(tasks, ask_id())
            elif choice == "5":
                uncomplete_task(tasks, ask_id())
            elif choice == "6":
                remove_task(tasks, ask_id())
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
