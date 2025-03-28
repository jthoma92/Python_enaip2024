import tkinter as tk

# Function to update the input field
def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying the input/output
entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create and add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=evaluate)
    else:
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14), command=lambda t=text: click_button(t))
    button.grid(row=row, column=col)

# Adding clear button
clear_button = tk.Button(root, text="C", width=10, height=2, font=("Arial", 14), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the application
root.mainloop()