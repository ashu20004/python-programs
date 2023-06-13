# Write a program to create a button and a label inside the frame widget. Button
# should change the color upon hovering over the button and label should
# disappear on clicking the button.

import tkinter as tk

def change_color(event):
    if event.type == 'Enter':
        button.config(bg='green')  
    elif event.type == 'Leave':
        button.config(bg='SystemButtonFace')  
def hide_label():
    label.pack_forget() 

root = tk.Tk()
root.title("Button and Label")

frame = tk.Frame(root)
frame.pack(pady=20)

button = tk.Button(frame, text="Hover Me")
button.pack(padx=10, pady=5)

label = tk.Label(frame, text="Click the button to hide me!")
label.pack(padx=10, pady=5)

button.bind("<Enter>", change_color)
button.bind("<Leave>", change_color)
button.config(command=hide_label)

root.mainloop()
