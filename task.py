class Task:
    def __init__(self, description, category):
        self.description = description
        self.completed = False
        self.category = category

    def toggle_completed(self):
        self.completed = not self.completed
    def __str__(self):
        status = f"{Fore.GREEN}✓{Style.RESET_ALL}" if self.completed else f"{Fore.RED}✗{Style.RESET_ALL}"
        return f"{status} {self.description} ({self.category.name})"