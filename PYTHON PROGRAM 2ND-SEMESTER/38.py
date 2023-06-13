# Write a program to create an arithmetic calculator using tkinter.

import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equals():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


window = tk.Tk()
window.title("Arithmetic Calculator")


entry = tk.Entry(window, width=30, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


number_buttons = []
for i in range(9):
    number_buttons.append(tk.Button(window, text=str(i+1), padx=20, pady=10, command=lambda i=i: button_click(i+1)))
    number_buttons[i].grid(row=1 + i // 3, column=i % 3)


operators = ['+', '-', '*', '/']
operator_buttons = []
for i in range(len(operators)):
    operator_buttons.append(tk.Button(window, text=operators[i], padx=20, pady=10, command=lambda i=i: button_click(operators[i])))
    operator_buttons[i].grid(row=1 + i, column=3)


button_0 = tk.Button(window, text='0', padx=20, pady=10, command=lambda: button_click(0))
button_clear = tk.Button(window, text='C', padx=20, pady=10, command=button_clear)
button_equals = tk.Button(window, text='=', padx=20, pady=10, command=button_equals)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equals.grid(row=4, column=2)


window.mainloop()
