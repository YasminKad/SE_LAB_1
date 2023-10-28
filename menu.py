from colorama import Fore, Style

from task import Task
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
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.remove_task()
            elif choice == "3":
                self.mark_task_completed()
            elif choice == "4":
                self.task_list.show_tasks()
            elif choice == "5":
                self.add_category()
            elif choice == "6":
                self.task_list.show_categories()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def add_task(self):
        task_description = input("Enter task description: ")
        category_name = input("Enter category name: ")
        if category_name not in self.task_list.categories:
            print("Category does not exist. Creating a new category.")
            self.task_list.add_category(category_name)
        task = Task(task_description, self.task_list.categories[category_name])
        self.task_list.add_task(task)

    def remove_task(self):
        if not self.task_list.tasks:
            print("No tasks to remove.")
            return

        print("Tasks:")
        self.task_list.show_tasks()
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(self.task_list.tasks):
            self.task_list.remove_task(self.task_list.tasks[task_index])
        else:
            print("Invalid task number.")

    def mark_task_completed(self):
        if not self.task_list.tasks:
            print("No tasks to mark as completed.")
            return

        print("Tasks:")
        self.task_list.show_tasks()
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(self.task_list.tasks):
            task = self.task_list.tasks[task_index]
            task.toggle_completed()
            status = "completed" if task.completed else "uncompleted"
            print(f"{Fore.GREEN}Task marked as {status}.{Style.RESET_ALL}")
        else:
            print("Invalid task number.")

    def add_category(self):
        category_name = input("Enter category name: ")
        self.task_list.add_category(category_name)