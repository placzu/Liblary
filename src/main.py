import tkinter as tk
from library_main_menu import LibraryMenuApp

if __name__ == '__main__':
    root = tk.Tk()
    app = LibraryMenuApp(root)
    root.bind('<Escape>', app.back_to_main_menu)
    root.mainloop()
