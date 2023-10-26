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
        return 0

    def add_category(self, name):
        return 0

    def show_categories(self):
        return 0