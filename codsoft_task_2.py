#Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.Perform the calculation and display the result.

import tkinter as tk
import math
from tkinter import font as tkfont

def add_digit(digit):
    current_text = entry.get()
    if current_text == "0":
        entry.delete(0, tk.END)
    entry.insert(tk.END, digit)

def add_decimal():
    current_text = entry.get()
    if "." not in current_text:
        entry.insert(tk.END, ".")

def clear_entry():
    entry.delete(0, tk.END)
    entry.insert(0, "0")

def perform_operation():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def backspace():
    current_text = entry.get()
    entry.delete(len(current_text) - 1)

app = tk.Tk()
app.title("Adyasha's Calculator App")
app.geometry("500x700")

app.configure(bg="black")
font_style = tkfont.Font(family="Helvetica", size=20, weight="bold")

title_label = tk.Label(app, text="Adyasha's Calculator App", font=font_style, bg="black", fg="white")
title_label.grid(row=0, column=0, columnspan=5)

entry = tk.Entry(app, font=font_style, justify="right", bd=10)
entry.insert(0, "0")
entry.grid(row=1, column=0, columnspan=5)

button_texts = [
    "7", "8", "9", "/", "(", ")",
    "4", "5", "6", "*", "^", 
    "1", "2", "3", "-", "sqrt",
    "0", ".", "=", "+", "C",
    "←"  
]

row_val = 2
col_val = 0

for button_text in button_texts:
    if button_text == "C":
        clear_button = tk.Button(app, text=button_text, font=font_style, height=2, width=5, command=clear_entry)
        clear_button.grid(row=row_val, column=col_val)
    elif button_text == "←":
        backspace_button = tk.Button(app, text=button_text, font=font_style, height=2, width=5, command=backspace)
        backspace_button.grid(row=row_val, column=col_val)
    else:
        button = tk.Button(app, text=button_text, font=font_style, height=2, width=5, command=lambda text=button_text: add_digit(text) if text != "=" else perform_operation())
        button.grid(row=row_val, column=col_val)
        button.config(fg="white", bg="black")  
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

app.mainloop()
