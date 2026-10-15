def get_warning(task):
    from datetime import datetime, date

    is_late = False
    warning = ""

    if task["due_date"]:
        is_late = datetime.strptime(task["due_date"], "%Y-%m-%d").date() < date.today()
        if not task["status"]:
            warning = "That task is overdue!" if is_late else f"Due: {task['due_date']}"
        else:
            warning = f"That task it's complete" if task["status"] else f"Due: {task['due_date']}"

    elif not task["due_date"]:
        warning = "No due date set" if not task["status"] else f"That task it's complete"

    return warning

def get_priority_order(task):
    priority_order = {"high": 3, "medium": 2, "low": 1}
    return priority_order[task["priority"]]



def get_priority_icon(task):
    icons = {"high": "🔴", "medium": "🟡", "low": "🟢"}
    return icons[task["priority"]]

