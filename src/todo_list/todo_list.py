import json
from datetime import date
from src.todo_list.helpers.visual import make_line, print_centered, show_menu
from src.todo_list.helpers.functions import add_task, list_tasks, edit_task, remove_task
from src.todo_list.helpers.validators import validate_date

try:
    with open("tasks.json", "r", encoding="utf-8") as f:
        todo = json.load(f)

except FileNotFoundError:
    todo = []

while True:
    while True:
        show_menu()

        try:
            command = int(input("Choose an action: "))
            make_line("=", 50)
            print()

            if command not in range(0, 9):
                print()
                make_line("=", 50)
                print_centered("Invalid command", 45)
                make_line("=", 50)
                print()
            else:
                break

        except ValueError:
            print()
            make_line("=", 50)
            print_centered("You need to enter an integer", 45)
            make_line("=", 50)
            print()

    match command:
        case 1:
            if not todo:
                make_line("=", 50)
                print_centered("There are no tasks", 45)
                make_line("=", 50)
            else:
                list_tasks(todo)

        case 2:
            if not todo:
                make_line("=", 50)
                print_centered("There are no tasks", 45)
                make_line("=", 50)
            else:
                list_tasks(todo, "completed")

        case 3:
            if not todo:
                make_line("=", 50)
                print_centered("There are no tasks", 45)
                make_line("=", 50)
            else:
                list_tasks(todo, "pending")

        case 4:
            if not todo:
                make_line("=", 50)
                print_centered("There are no tasks", 45)
                make_line("=", 50)
            else:
                key_word = input("Enter a keyword: ").strip().lower()
                list_tasks(todo, keywords=key_word)

        case 5:
            while True:
                try:
                    current_year = date.today().year
                    current_date = date.today()


                    print_centered(" [ Adding Tasks ] ", 60, "=")
                    desc = input("Enter a description: ").strip().lower()

                    if not desc:
                        raise ValueError

                    for task in todo:
                        while desc == task["description"]:
                            print()
                            print(f"There already a task with the name '{desc}'")
                            print()
                            desc = input("Enter a description: ").strip().lower()

                    priority = input("Enter priority (high | medium | low): ").strip().lower()

                    if priority not in ["high", "medium", "low"] or not priority:
                        raise ValueError

                    date_confirmation = input("Do you want add a date for complete your task? [y/n]: ").strip().lower()
                    make_line("=", 60)
                    print()

                    while date_confirmation not in ["y", "n"]:
                        make_line("=", 50)
                        print_centered("Please enter 'y' or 'n'", 45)
                        make_line("=", 50)
                        print()
                        date_confirmation = input("Do you want add a date for complete your task? [y/n]: ").strip().lower()

                    if date_confirmation in "y":
                        valid, user_date = validate_date()

                        if valid:
                            add_task(desc, priority, user_date, todo=todo)
                            break

                    elif date_confirmation in ["n", "no"]:
                        add_task(desc, priority, todo=todo)
                        break

                except ValueError:
                    make_line("=", 50)
                    print_centered("Please enter a valid description or priority", 45)
                    make_line("=", 50)

        case 6:
            try:
                count = 0
                for task in todo:
                    if task["status"]:
                        count += 1
                if count == len(todo) and todo:
                    print()
                    make_line("=", 50)
                    print_centered("All tasks are completed, good job!", 45)
                    make_line("=", 50)
                    print()
                else:
                    done = input("Enter the task name: ").lower().strip()
                    found = False
                    for task in todo:
                        if task["description"] == done:
                            task["status"] = True
                            print(f"✅ Task '{task["description"]}' marked as completed\n")
                            found = True
                            break
                    if not found:
                        make_line("=", 50)
                        print_centered("Task not found.", 45)
                        make_line("=", 50)
            except Exception:
                make_line("=", 50)
                print_centered("Error while removing task", 45)
                make_line("=", 50)

        case 7:
            try:
                seen = 0
                name = input("Enter the task name: ")

                for task in todo:
                    if not name == task["description"]:
                        seen += 1
                if seen == len(todo):
                    make_line("=", 50)
                    print_centered(f"There are no task named '{name}'", 45)
                    make_line("=", 50)
                else:
                    confirmation = input("Do you really want to edit the task? [y/n]: ").strip().lower()

                    if confirmation in ["y", "yes"]:
                        print()
                        make_line("=", 50)
                        print_centered(f"Editing the task '{name}'", 45)
                        make_line("=", 50)
                        print()

                        new_description = input("Enter a new description: ").strip().lower()

                        if not new_description:
                            make_line("=", 50)
                            print_centered("Description cannot be empty", 45)
                            make_line("=", 50)

                        new_priority = input("Enter a new priority (high | medium | low): ").strip().lower()

                        if new_priority not in ["high", "medium", "low"] or not new_priority:
                            make_line("=", 50)
                            print_centered("Invalid priority", 45)
                            make_line("=", 50)

                        date_confirmation = input("Do you want add a date for complete your task? [y/n]: ").strip().lower()
                        print()

                        while date_confirmation not in ["y", "n"]:
                            make_line("=", 50)
                            print_centered("Please enter 'y' or 'n'", 45)
                            make_line("=", 50)
                            print()
                            date_confirmation = input("Do you want add a date for complete your task? [y/n]: ").strip().lower()

                        if date_confirmation in "y":
                            valid, user_date = validate_date()

                            if valid:
                                edit_task(tasks=todo, name=name, new_description=new_description, new_priority=new_priority, new_due_date= user_date)

                        elif date_confirmation in ["n", "no"]:
                            edit_task(tasks=todo, name=name, new_description=new_description, new_priority=new_priority)

                    elif confirmation in ["n", "no"]:
                        make_line("=", 50)
                        print_centered("Task not edited", 45)
                        make_line("=", 50)
                        break
                    else:
                        make_line("=", 50)
                        print_centered("Invalid option", 45)
                        make_line("=", 50)

            except ValueError:
                make_line("=", 50)
                print_centered("Enter a valid description or a valid priority", 45)
                make_line("=", 50)

        case 8:
            try:
                if not todo:
                    make_line("=", 50)
                    print_centered("There are no tasks", 45)
                    make_line("=", 50)
                else:
                    remove = input("Enter the task name: ").strip().lower()
                    remove_task(todo, remove)

            except Exception:
                make_line("=", 50)
                print_centered("Error while removing task", 45)
                make_line("=", 50)

        case 0:
            print("💾 Tasks saved successfully! Goodbye.")
            break

with open("tasks.json", "w", encoding="utf-8") as f:
    json.dump(todo, f, indent=4, ensure_ascii=False, default=lambda obj: obj.isoformat())
