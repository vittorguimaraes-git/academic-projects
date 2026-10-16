def add_task(desc, priority, due_date = None, todo = None):

    if todo is None:
        todo = list()

    for task in todo:
        if desc == task["description"]:
            raise ValueError

    if priority not in ["high", "medium", "low"]:
        raise ValueError

    new_task = {
        "description": desc,
        "priority": priority,
        "due_date": due_date,
        "status": False}

    todo.append(new_task)
    print(f"➕ Task '{desc}' added with priority '{priority}'")

    return new_task


def list_tasks(tasks: list, filtration = None, keywords = None):
    from src.todo_list.helpers.getters import get_priority_order, get_priority_icon, get_warning

    if not filtration and not keywords:

        done = sum(1 for t in tasks if t["status"])
        undone = len(tasks) - done

        print("All tasks".center(45))
        print("=" * 50)
        for task in sorted(tasks, key=get_priority_order, reverse = True):
            markup = "[x]" if task["status"] else "[ ]"
            icon = get_priority_icon(task)
            print(f"{markup} {task['description'].title()} {icon} | {get_warning(task)}")
        print("=" * 50)
        print(f"\n✅ {done} Completed tasks | ⏳ {undone} Pending tasks\n")
        print()

    elif keywords:
        count = 0

        print(f"Tasks with '{keywords}'".center(45))
        print("=" * 50)
        for task in sorted(tasks, key=get_priority_order, reverse=True):
            if keywords in task["description"]:
                markup = "[x]" if task["status"] else "[ ]"
                icon = get_priority_icon(task)
                print(f"{markup} {task['description'].title()} {icon} {get_warning(task)}")
            else:
                count += 1
        if count == len(tasks):
            print(f"There are no tasks with the keyword '{keywords}'")
        print("=" * 50)
        print()

    elif filtration:
        if filtration not in ["completed", "pending"]:
            raise ValueError
        elif filtration in ["completed", "pending"]:
            if filtration == "completed":
                completed = sum(1 for t in tasks if t["status"])
                count = 0

                print("Completed tasks".center(45))
                print("=" * 50)
                for task in tasks:
                    if task["status"]:
                        icon = get_priority_icon(task)
                        markup = "[x]" if task["status"] else "[ ]"
                        print(f"{markup} {task['description'].title()} {icon} | {get_warning(task)}")
                    else:
                        count += 1

                if count == len(tasks):
                    print("There are no completed tasks".center(45))
                print("=" * 50)
                print(f"\n✅ {completed} Completed tasks\n")
                print()

            if filtration == "pending":
                pending = sum(1 for t in tasks if not t["status"])
                count = 0

                print("Pending tasks".center(45))
                print("=" * 50)
                for task in tasks:
                    if not task["status"]:
                        icon = get_priority_icon(task)
                        print(f"[ ] {task['description'].title()} {icon} | {get_warning(task)}")
                    else:
                        count += 1
                if count == len(tasks):
                    print("There are no pending tasks".center(45))
                print("=" * 50)
                print(f"\n⏳ {pending} Pending tasks\n")

        else:
            print("=" * 50)
            print("invalid option".center(45))
            print("=" * 50)


def edit_task(tasks, name: str, new_description: str, new_priority: str, new_due_date = None):

    if new_priority not in ["high", "medium", "low"]:
        raise ValueError

    if not new_description:
        raise ValueError

    seen = 0
    for task in tasks:
        if name == task["description"]:
            old_description = task["description"]
            task["description"] = new_description
            task["priority"] = new_priority
            task["due_date"] = new_due_date
            task["status"] = False
            print(f"✏️ Task '{old_description}' edited successfully\n")
            return task
        else:
            seen += 1

    if len(tasks) == seen:
        print("=" * 50)
        print("Task not found".center(45))
        print("=" * 50)

    return None


def remove_task(tasks, name: str):
    for task in tasks:
        if name == task["description"]:
            while True:
                confirmation = input("Do you really want to remove this task? [y/n]: ").strip().lower()
                if confirmation in ["y", "yes", "n", "no"]:
                    break
                else:
                    print("=" * 50)
                    print("Invalid option".center(45))
                    print("=" * 50)

            if confirmation in ["y", "yes"]:
                tasks.remove(task)
                print(f"🗑️ Task '{task["description"]}' removed successfully\n")
                break

            elif confirmation in ["n", "no"]:
                print("=" * 50)
                print("Task not removed".center(45))
                print("=" * 50)
                break

    return name














