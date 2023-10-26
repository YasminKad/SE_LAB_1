from task_list import TaskList


class Menu:
    def __init__(self):
        self.task_list = TaskList()

    def display_main_menu(self):
        print("Options:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. Show tasks")
        print("5. Add a category")
        print("6. Show categories")
        print("7. Quit")

    def main_menu(self):
        return 0

    def add_task(self):
        return 0

    def remove_task(self):
        return 0

    def mark_task_completed(self):
        return 0

    def add_category(self):
        return 0
