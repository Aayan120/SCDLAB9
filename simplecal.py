import tkinter as tk

# Function to update expression in the entry box
def press(num):
    entry_text.set(entry_text.get() + str(num))

# Function to evaluate the expression
def equalpress():
    try:
        total = str(eval(entry_text.get()))
        entry_text.set(total)
    except:
        entry_text.set("Error")

# Function to clear the entry
def clear():
    entry_text.set("")

# GUI setup
window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg="grey")
window.geometry("300x400")

entry_text = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_text, font=('Arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right', fg='blue')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for btn in buttons:
    action = lambda x=btn: press(x) if x not in ['C', '='] else equalpress() if x == '=' else clear()
    tk.Button(window, text=btn, padx=20, pady=20, font=('Arial', 14), bg='lightgrey', fg='blue', command=action).grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Make the layout flexible
for i in range(5):
    window.rowconfigure(i, weight=1)
    window.columnconfigure(i % 4, weight=1)

window.mainloop()
