from category import Category


class TaskList:
    def __init__(self):
        self.tasks = []
        self.categories = {}

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def add_category(self, name):
        if name not in self.categories:
            self.categories[name] = Category(name)

    def show_categories(self):
        if not self.categories:
            print("No categories.")
            return

        print("Categories:")
        for name in self.categories:
            print(name)