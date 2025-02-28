import tkinter as tk

def button_click(value):
    entry_field.insert(tk.END, value)

def clear():
    entry_field.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, result)
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry_field = tk.Entry(root, width=20, font=('Arial', 18), bd=8, relief=tk.SUNKEN)
entry_field.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), bg="lightgreen",
                        command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), bg="lightcoral",
                        command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                        command=lambda value=text: button_click(value))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
