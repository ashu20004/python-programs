# Write a program to create a window that disappears automatically after 5
# seconds

import tkinter as tk

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Auto Close Window")

# Set the window to be visible for 5 seconds
root.after(5000, close_window)

root.mainloop()
