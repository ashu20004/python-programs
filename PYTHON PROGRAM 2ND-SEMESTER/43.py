# Write a program to display a menu on the menu bar.

import tkinter as tk

def dummy_command():
    print("Menu item clicked!")  

root = tk.Tk()
root.title("Menu Example")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=dummy_command)
file_menu.add_command(label="Open", command=dummy_command)
file_menu.add_command(label="Save", command=dummy_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)


root.config(menu=menu_bar)

root.mainloop()
