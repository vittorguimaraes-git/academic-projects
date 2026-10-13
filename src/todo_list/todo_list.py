# ============================================================
# Refatoração - Funções prioritárias a criar
# ============================================================

# 🔴 Alta prioridade (primeiro a implementar)
# 1. print_centered(msg, width=50)
#    - Centraliza mensagens e imprime separadores.
#    - Evita repetição de print("=" * 50) e .center(45).

# 2. get_warning(task)
#    - Retorna aviso sobre status da tarefa:
#      * "Task completed" se concluída
#      * "No due date set" se sem prazo
#      * "That task is overdue!" se atrasada
#      * "Due: YYYY-MM-DD" se prazo válido
#    - Centraliza lógica usada em vários cases.

# 3. validate_priority(priority)
#    - Verifica se prioridade está entre ["high", "medium", "low"].
#    - Evita duplicação de if priority not in [...]

# 🟡 Prioridade média (depois de limpar o básico)
# 4. add_task(desc, priority, date_to_complete=None)
#    - Encapsula lógica de adicionar tarefa.
#    - Facilita manutenção e consistência no JSON.

# 5. list_tasks(filter=None, keyword=None)
#    - Generaliza listagem (todas, concluídas, pendentes, por palavra-chave).
#    - Evita blocos repetidos nos cases 1, 2, 3 e 4.

# 🟢 Prioridade baixa (quando já estiver organizado)
# 6. edit_task(index, new_desc, new_priority)
#    - Encapsula edição de tarefa, simplificando case 7.

# 7. remove_task(name)
#    - Encapsula remoção por nome, simplificando case 8.

import json
from datetime import date, datetime

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
        print("[4] List for key word")
        print("[5] Add task")
        print("[6] Complete task")
        print("[7] Edit task")
        print("[8] Delete task")
        print("[0] exit\n")


        try:
            command = int(input("Choose an action: "))
            print("=" * 50)
            print()

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

                print("=" * 50)
                for task in sorted(todo, key=lambda t: priority_order[t["priority"]], reverse=True):
                    if not task["status"]:
                        if task["date_to_complete"] is None:
                            is_late = False
                            warning = "No due date set"
                        else:
                            is_late = datetime.strptime(task["date_to_complete"], "%Y-%m-%d").date() < date.today()
                            warning = "That task is overdue!" if is_late else f"Due: {task['date_to_complete']}"
                    else:
                        warning = "Task completed"

                    markup = "[x]" if task["status"] else "[ ]"
                    icon = priority_icons[task["priority"]]
                    print(f"{markup} {task['description'].title()} {icon} {("| " if warning else "") + warning}")
                print("=" * 50)
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
                        warning = "That task is complete"
                        icon = priority_icons[task["priority"]]
                        markup = "[x]" if task["status"] else "[ ]"
                        print(f"{markup} {task['description'].title()} {icon} | {warning}")
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
                        print(f"[ ] {task['description'].title()} {icon}")
                    else:
                        count += 1
                if count == len(todo):
                    print("There are no pending tasks".center(35))
                print("=" * 35)
                print(f"\n⏳ {len(todo) - count} Pending tasks\n")

        case 4:

            if not todo:
                print("=" * 50)
                print("There are no tasks".center(45))
                print("=" * 50)
            else:

                count = 0
                priority_order = {"high": 3, "medium": 2, "low": 1}
                priority_icons = {"high": "🔴", "medium": "🟡", "low": "🟢"}

                key_word = input("Enter a keyword: ").strip().lower()
                print("=" * 50)
                for task in sorted(todo, key= lambda t: priority_order[t["priority"]], reverse=True):
                    if key_word in task["description"]:

                        if task["date_to_complete"] is None:
                            is_late = False
                            warning = "No due date set"
                        else:
                            is_late = datetime.strptime(task["date_to_complete"], "%Y-%m-%d").date() < date.today()
                            warning = "That task is overdue!" if is_late else f"Due: {task['date_to_complete']}"

                        markup = "[x]" if task["status"] else "[ ]"
                        icon = priority_icons[task["priority"]]
                        print(f"{markup} {task['description'].title()} {icon} {("| " if warning else "") + warning }")
                    else:
                        count += 1
                if count == len(todo):
                    print(f"There are no tasks with the keyword '{key_word}'")
                print("=" * 50)



        case 5:

            while True:

                try:
                    valid = False
                    user_date = None
                    current_year = date.today().year
                    current_date = date.today()
                    print(" [ Adding Tasks ] ".center(60, "="))
                    desc = input("Enter a description: ").strip().lower()

                    for task in todo:
                        while desc == task["description"]:
                            print()
                            print(f"There already a task with the name '{desc}'")
                            print()
                            desc = input("Enter a description: ").strip().lower()

                    priority = input("Enter priority (high | medium | low): ").strip().lower()
                    date_confirmation = input("Do you want add a date for complete your task? [y/n]: ").strip().lower()
                    print("=" * 60)
                    print()

                    while date_confirmation not in ["y", "n"]:
                        print("=" * 50)
                        print("Please enter 'y' or 'n'".center(45))
                        print("=" * 50 + "\n")
                        date_confirmation = input("Do you want add a date for complete your task? [y/n]: ").strip().lower()

                    if date_confirmation in "y":
                        try:
                            while True:
                                year = int(input("Enter a year: "))

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
                    elif date_confirmation in ["n", "no"]:
                        todo.append(
                            {"description": desc, "status": False, "priority": priority, "date_to_complete": user_date})
                        print(f"➕ Task '{desc}' added with priority '{priority}'")
                        print()
                        break

                    if valid:
                        todo.append(
                            {"description": desc, "status": False, "priority": priority,
                             "date_to_complete": user_date})
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

        case 6:

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

        case 7:

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

        case 8:
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
    json.dump(todo, f, indent=4, ensure_ascii=False, default= lambda obj: obj.isoformat())
