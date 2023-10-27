from colorama import init

from menu import Menu

if __name__ == "__main__":
    init(autoreset=True)
    menu = Menu()
    menu.main_menu()
