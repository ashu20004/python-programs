# Write a program to create radio-buttons (Male, Female, and Transgender) and
# a label. Default selection should be on Female and the label must display the
# current selection made by user.

import tkinter as tk

def update_label():
    selection = gender_var.get()
    label.config(text=f"Selected option: {selection}")

root = tk.Tk()
root.title("Radio Buttons")

frame = tk.Frame(root)
frame.pack(pady=20)

gender_var = tk.StringVar(value="Female")

male_radio = tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", command=update_label)
male_radio.pack(padx=10, pady=5)

female_radio = tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", command=update_label)
female_radio.pack(padx=10, pady=5)

trans_radio = tk.Radiobutton(frame, text="Transgender", variable=gender_var, value="Transgender", command=update_label)
trans_radio.pack(padx=10, pady=5)

label = tk.Label(root, text="Selected option: Female")
label.pack()

root.mainloop()
