from tkinter import *

root = Tk()
root.title('MiniCalculi')

# width and height
root.geometry("400x550")

# font
font = ('Helvetica', 20)
display = Entry(root, font=font)
display.grid(row=0, column=0, columnspan=4, pady=10, sticky=N + E + W + S)

# button colors based on operations
button_colors = {
    'numeric':'#4CAF50',  # Green
    'operator':'#2196F3',  # Blue
    'equal': '#FF9800',  # Orange
    'clear': '#FF0000',  # Red
    'utility': '#9E9E9E'  # Gray
}

# Function to create buttons with specific colors
def create_button(text, row, column, width=1, height=1, command=None, color='numeric'):
    button = Button(root, text=text, width=width, height=height, command=command, bg=button_colors[color], font=('Helvetica', 16))
    button.grid(row=row, column=column, padx=5, pady=5, sticky=N + S + E + W)
    return button

def getvariables(num):
    global i
    display.insert(i, num)
    i += 1

def calculate():
    input = display.get()
    try:
        result = eval(input)
        clear()
        display.insert(0, result)
    except Exception:
        clear()
        display.insert(0, "Error")

def operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def clear():
    display.delete(0, END)

def backspace():
    input = display.get()
    if len(input):
        newinput = input[:-1]
        clear()
        display.insert(0, newinput)
    else:
        clear()
        display.insert(0, "Error")

# button layout
buttonlayout = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2, 2, 1, calculate, 'equal'),
    ('+', 4, 3),
    ('(', 5, 0, 1, 1, lambda: operation("("), 'operator'),
    (')', 5, 1, 1, 1, lambda: operation(")"), 'operator'),
    ('AC', 5, 2, 1, 1, clear, 'clear'),
    ('<-', 5, 3, 1, 1, backspace, 'utility')
]

# Creating buttons
for button in buttonlayout:
    text, row, column = button[:3]
    width = button[3] if len(button) > 3 else 1
    height = button[4] if len(button) > 4 else 1
    command = button[5] if len(button) > 5 else lambda b=text: getvariables(b) if b.isdigit() or b in ".pi" else operation(b)
    color = button[6] if len(button) > 6 else 'numeric' if text.isdigit() or text == '.' else 'operator'
    create_button(text, row, column, width, height, command, color)

# Seting row and column weights for proper resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
