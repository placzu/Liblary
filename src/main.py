import tkinter as tk
from library_main_menu import LibraryMenuApp
def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
    root = tk.Tk()
    app = LibraryMenuApp(root)
    root.mainloop()
