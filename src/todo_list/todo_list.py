# ============================================================
# Refatoração - Funções prioritárias a criar
# ============================================================

# 🔴 Alta prioridade (primeiro a implementar)
# 1. print_centered(msg, width=50)
#    - Centraliza mensagens e imprime separadores.
#    - Evita repetição de make_line("=", 50) e print_centered(...).

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

from src.todo_list.helpers.visual import make_line, print_centered, show_menu
from src.todo_list.helpers.getters import get_warning, get_priority_order, get_priority_icon
from src.todo_list.helpers.functions import add_task
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
            done = sum(1 for t in todo if t["status"])
            undone = len(todo) - done

            if not todo:
                make_line("=", 50)
                print_centered("There are no tasks", 45)
                make_line("=", 50)
            else:
                make_line("=", 50)
                for task in sorted(todo, key=get_priority_order, reverse=True):
                    markup = "[x]" if task["status"] else "[ ]"
                    icon = get_priority_icon(task)
                    print(f"{markup} {task['description'].title()} {icon} | {get_warning(task)}")
                make_line("=", 50)
                print(f"\n✅ {done} Completed tasks | ⏳ {undone} Pending tasks\n")

        case 2:
            if not todo:
                make_line("=", 50)
                print_centered("There are no tasks", 45)
                make_line("=", 50)
            else:
                count = 0
                make_line("=", 50)
                for task in todo:
                    if task["status"]:
                        icon = get_priority_icon(task)
                        markup = "[x]" if task["status"] else "[ ]"
                        print(f"{markup} {task['description'].title()} {icon} | {get_warning(task)}")
                    else:
                        count += 1
                if count == len(todo):
                    print_centered("There are no completed tasks", 45)
                make_line("=", 50)
                print(f"\n✅ {len(todo) - count} Completed tasks\n")

        case 3:
            if not todo:
                make_line("=", 50)
                print_centered("There are no tasks", 45)
                make_line("=", 50)
            else:
                count = 0
                make_line("=", 35)
                for task in todo:
                    if not task["status"]:
                        icon = get_priority_icon(task)
                        print(f"[ ] {task['description'].title()} {icon} | {get_warning(task)}")
                    else:
                        count += 1
                if count == len(todo):
                    print_centered("There are no pending tasks", 35)
                make_line("=", 35)
                print(f"\n⏳ {len(todo) - count} Pending tasks\n")

        case 4:
            if not todo:
                make_line("=", 50)
                print_centered("There are no tasks", 45)
                make_line("=", 50)
            else:
                count = 0
                key_word = input("Enter a keyword: ").strip().lower()
                make_line("=", 50)
                for task in sorted(todo, key=get_priority_order, reverse=True):
                    if key_word in task["description"]:
                        if task["date_to_complete"] is None:
                            is_late = False
                            warning = "No due date set"
                        else:
                            is_late = datetime.strptime(task["date_to_complete"], "%Y-%m-%d").date() < date.today()
                            warning = "That task is overdue!" if is_late else f"Due: {task['date_to_complete']}"

                        markup = "[x]" if task["status"] else "[ ]"
                        icon = get_priority_icon(task)
                        print(f"{markup} {task['description'].title()} {icon} {get_warning(task)}")
                    else:
                        count += 1
                if count == len(todo):
                    print(f"There are no tasks with the keyword '{key_word}'")
                make_line("=", 50)

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
                edit = int(input("Enter the task number: "))
                new_description = input("Enter a new description: ").strip().lower()
                new_priority = input("Enter a new priority (high | medium | low): ").strip().lower()
                confirmation = input("Do you really want to edit the task? [y/n]: ").strip().lower()

                if new_priority not in ["high", "medium", "low"] or not new_priority:
                    make_line("=", 50)
                    print_centered("Invalid priority", 45)
                    make_line("=", 50)
                elif not new_description:
                    make_line("=", 50)
                    print_centered("Description cannot be empty", 45)
                    make_line("=", 50)
                elif confirmation in ["y", "yes"]:
                    todo[edit - 1]["description"] = new_description
                    todo[edit - 1]["status"] = False
                    todo[edit - 1]["priority"] = new_priority
                    print(f"✏️ Task updated to: {new_description}\n")
                elif confirmation in ["n", "no"]:
                    make_line("=", 50)
                    print_centered("Task not edited", 45)
                    make_line("=", 50)
                else:
                    make_line("=", 50)
                    print_centered("Invalid option", 45)
                    make_line("=", 50)

            except (ValueError, IndexError):
                make_line("=", 50)
                print_centered("Invalid task", 45)
                make_line("=", 50)

        case 8:
            try:
                if not todo:
                    make_line("=", 50)
                    print_centered("There are no tasks", 45)
                    make_line("=", 50)
                else:
                    remove = input("Enter the task name: ").strip().lower()
                    found = False

                    for i, task in enumerate(todo):
                        if task["description"] == remove:
                            confirmation = input("Do you really want to remove the task? [y/n]: ").strip().lower()
                            if confirmation in ["y", "yes"]:
                                todo.pop(i)
                                print(f"🗑️ Task '{task["description"]}' removed successfully\n")
                            elif confirmation in ["n", "no"]:
                                make_line("=", 50)
                                print_centered("Task not removed", 45)
                                make_line("=", 50)
                            else:
                                make_line("=", 50)
                                print_centered("Invalid option", 45)
                                make_line("=", 50)

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

        case 0:
            print("💾 Tasks saved successfully! Goodbye.")
            break

with open("tasks.json", "w", encoding="utf-8") as f:
    json.dump(todo, f, indent=4, ensure_ascii=False, default=lambda obj: obj.isoformat())
