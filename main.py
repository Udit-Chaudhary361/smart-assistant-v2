from packages.assistant import (
    set_name,
    add_note,
    view_notes,
    add_task,
    view_tasks
)

from packages.joke_tool import get_joke


def show_menu():
    print("\n🤖 Smart Assistant V2")
    print("1. Set Name")
    print("2. View Notes")
    print("3. Add Note")
    print("4. View Tasks")
    print("5. Add Task")
    print("6. Get Joke")
    print("7. Exit")


def run():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            set_name(name)
            print("Name saved!")

        elif choice == "2":
            print(view_notes())

        elif choice == "3":
            note = input("Enter note: ")
            add_note(note)
            print("Note added!")

        elif choice == "4":
            print(view_tasks())

        elif choice == "5":
            task = input("Enter task: ")
            add_task(task)
            print("Task added!")

        elif choice == "6":
            print(get_joke())

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


run()