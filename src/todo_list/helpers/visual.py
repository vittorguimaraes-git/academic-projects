def print_centered(msg: str, width: int, fill: str = " "):
    print(f"{msg.center(width, fill)}")


def make_line(char: str, width: int):
    print(f"{char * width}")

def show_menu():
    make_line("=", 50)
    print_centered("Menu", 45)
    make_line("=", 50)

    print("\n[1] List tasks")
    print("[2] List completed tasks")
    print("[3] List pending tasks")
    print("[4] List for key word")
    print("[5] Add task")
    print("[6] Complete task")
    print("[7] Edit task")
    print("[8] Delete task")
    print("[0] exit\n")