import json
from datetime import date

try:

    with open("tasks.json", "r", encoding="utf-8") as f:
        todo = json.load(f)

except FileNotFoundError:
    todo = []

while True:

    while True:
        print("=" * 50)
        print("Menu".center(45))
        print("=" * 50)


        print("\n[1] List tasks")
        print("[2] List completed tasks")
        print("[3] List pending tasks")
        print("[4] Add task")
        print("[5] Complete task")
        print("[6] Edit task")
        print("[7] Delete task")
        print("[0] exit\n")


        try:
            command = int(input("Choose an action: "))

            if command not in range(0, 9):
                print("\n" + "=" * 50)
                print("Invalid command".center(45))
                print("=" * 50 + "\n")
            else:
                break

        except ValueError:
            print("\n" + "=" * 50)
            print("You need to enter an integer".center(45))
            print("=" * 50 + "\n")

    match command:

        case 1:

            priority_order = {"high": 3, "medium": 2, "low": 1}
            priority_icons = {"high": "🔴", "medium": "🟡", "low": "🟢"}
            done = sum(1 for t in todo if t["status"])
            undone = len(todo) - done

            if not todo:
                print("=" * 50)
                print("There are no tasks".center(45))
                print("=" * 50)
            else:
                print("=" * 35)
                for task in sorted(todo, key=lambda t: priority_order[t["priority"]], reverse=True):
                    markup = "[x]" if task["status"] else "[ ]"
                    icon = priority_icons[task["priority"]]
                    print(f"{markup} {task['description']} {icon}")
                print("=" * 35)
                print(f"\n✅ {done} Completed tasks | ⏳ {undone} Pending tasks\n")

        case 2:

            priority_icons = {"high": "🔴", "medium": "🟡", "low": "🟢"}

            if not todo:
                print("=" * 50)
                print("There are no tasks".center(45))
                print("=" * 50)
            else:
                count = 0
                print("=" * 50)
                for task in todo:
                    if task["status"]:
                        icon = priority_icons[task["priority"]]
                        print(f"[x] {task['description']} {icon}")
                    else:
                        count += 1
                if count == len(todo):
                    print("There are no completed tasks".center(45))
                print("=" * 50)
                print(f"\n✅ {len(todo) - count} Completed tasks\n")

        case 3:

            priority_icons = {"high": "🔴", "medium": "🟡", "low": "🟢"}

            if not todo:
                print("=" * 50)
                print("There are no tasks".center(45))
                print("=" * 50)
            else:
                count = 0
                print("=" * 35)
                for task in todo:
                    if not task["status"]:
                        icon = priority_icons[task["priority"]]
                        print(f"[ ] {task['description']} {icon}")
                    else:
                        count += 1
                if count == len(todo):
                    print("There are no pending tasks".center(35))
                print("=" * 35)
                print(f"\n⏳ {len(todo) - count} Pending tasks\n")

        case 4:

            while True:

                # Preciso validar a entrada dos meses e dos dias

                try:
                    valid = False
                    user_date = None
                    current_year = date.today().year
                    current_date = date.today()
                    desc = input("Enter a description: ").strip().title()
                    priority = input("Enter priority (high | medium | low): ").strip().lower()
                    date_confirmation = input("Do you want add a date for complete your task? [y/n]: ").strip().lower()

                    if date_confirmation in ["y", "yes"]:
                        try:
                            while True:
                                year = int(input("\nEnter a year: "))

                                if year < current_year:
                                    print("Enter a valid year\n")
                                else:
                                    break

                            while True:
                                month = int(input("Enter a month: "))

                                if month > 12 or month < 1:
                                    print("Enter a valid month\n")
                                else:
                                    break

                            while True:
                                day = int(input("Enter a day: "))
                                print()

                                if day < 1 or day > 31:
                                    print("Enter a valid day\n")
                                else:
                                    break

                            user_date = date(year, month, day)

                            if user_date < current_date:
                                raise ValueError
                            else:
                                valid = True



                        except ValueError:
                            print("Enter a valid date")
                    else:
                        todo.append(
                            {"description": desc, "status": False, "priority": priority,})
                        print(f"➕ Task '{desc}' added with priority '{priority}'")
                        print()
                        break

                    if valid:
                        todo.append(
                            {"description": desc, "status": False, "priority": priority,
                             "date_to_complete": str(user_date)})
                        print(f"➕ Task '{desc}' added with priority '{priority}'")
                        print()
                        break

                    if priority not in ["high", "medium", "low"] or not priority:
                        raise ValueError

                    if not desc:
                        raise ValueError

                except ValueError:
                    print("=" * 50)
                    print("Please enter a valid description or priority".center(45))
                    print("=" * 50)



        case 5:

            try:

                count = 0

                for task in todo:
                    if task["status"]:
                        count += 1
                if count == len(todo) and todo:
                    print("\n" + "=" * 50)
                    print("All tasks are completed, good job!".center(45))
                    print("=" * 50 + "\n")
                else:
                    done = input("Enter the task name: ")
                    found = False
                    for task in todo:
                        if task["description"] == done:
                            task["status"] = True
                            print(f"✅ Task '{task["description"]}' marked as completed\n")

                            found = True
                            break
                    if not found:
                        print("=" * 50)
                        print("Task not found.".center(45))
                        print("=" * 50)
            except Exception:
                print("=" * 50)
                print("Error while removing task".center(45))
                print("=" * 50)

        case 6:

            try:

                edit = int(input("Enter the task number: "))
                new_description = input("Enter a new description: ").strip().title()
                new_priority = input("Enter a new priority (high | medium | low): ").strip().lower()
                confirmation = input("Do you really want to edit the task? [y/n]: ").strip().lower()

                if new_priority not in ["high", "medium", "low"] or not new_priority:
                    print("=" * 50)
                    print("Invalid priority".center(45))
                    print("=" * 50)
                elif not new_description:
                    print("=" * 50)
                    print("Description cannot be empty".center(45))
                    print("=" * 50)
                elif confirmation in ["y", "yes"]:
                    todo[edit - 1]["description"] = new_description
                    todo[edit - 1]["status"] = False
                    todo[edit - 1]["priority"] = new_priority
                    print(f"✏️ Task updated to: {new_description}\n")
                elif confirmation in ["n", "no"]:
                    print("=" * 50)
                    print("Task not edited".center(45))
                    print("=" * 50)
                else:
                    print("=" * 50)
                    print("Invalid option".center(45))
                    print("=" * 50)

            except (ValueError, IndexError):
                print("=" * 50)
                print("Invalid task".center(45))
                print("=" * 50)

        case 7:
            try:
                if not todo:
                    print("=" * 50)
                    print("There are no tasks".center(45))
                    print("=" * 50)
                else:
                    remove = input("Enter the task name: ").strip().title()
                    found = False

                    for i, task in enumerate(todo):
                        if task["description"] == remove:
                            confirmation = input("Do you really want to remove the task? [y/n]: ").strip().lower()

                            if confirmation in ["y", "yes"]:
                                todo.pop(i)
                                print(f"🗑️ Task '{task["description"]}' removed successfully\n")
                            elif confirmation in ["n", "no"]:
                                print("=" * 50)
                                print("Task not removed".center(45))
                                print("=" * 50)
                            else:
                                print("=" * 50)
                                print("Invalid option".center(45))
                                print("=" * 50)

                            found = True
                            break

                    if not found:
                        print("=" * 50)
                        print("Task not found.".center(45))
                        print("=" * 50)

            except Exception:
                print("=" * 50)
                print("Error while removing task".center(45))
                print("=" * 50)

        case 0:
            print("💾 Tasks saved successfully! Goodbye.")
            break

with open("tasks.json", "w", encoding="utf-8") as f:
    json.dump(todo, f, indent=4, ensure_ascii=False)
