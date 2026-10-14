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
