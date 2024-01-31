import tkinter as tk
from tkinter import messagebox


def on_click(button_text):
    current_text = entry_var.get()

    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Ошибка")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

root = tk.Tk()
root.title("Калькулятор")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 14), bd=10, insertwidth=4, width=15, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    tk.Button(root, text=button_text, padx=20, pady=20, font=("Arial", 14), command=lambda text=button_text: on_click(text)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
