#PASSWORD GENERATOR

import tkinter as tk
import random
import string

def generate_password():
    password_length_str = length_entry.get()
    
    if not password_length_str.isnumeric():
        password_label.config(text="Please enter a valid length", fg="red")
        return
    
    password_length = int(password_length_str)
    
    if password_length < 1:
        password_label.config(text="Please enter a valid length", fg="red")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text="Generated Password:", fg="black")
    password_output.config(text=password)
    regenerate_button.config(state=tk.NORMAL)
    accept_button.config(state=tk.NORMAL)

def accept_password():
    name = name_entry.get()
    password = password_output.cget("text")
    output_text = f"Hello, {name}! Your password is:\n{password}"
    password_label.config(text="Password Accepted:", fg="green")
    password_output.config(text=output_text)
    regenerate_button.config(state=tk.DISABLED)
    accept_button.config(state=tk.DISABLED)

def regenerate_password():
    generate_password()
    accept_button.config(state=tk.NORMAL)

def clear_password():
    password_label.config(text="", fg="#f0f0f0")
    password_output.config(text="")
    regenerate_button.config(state=tk.DISABLED)
    accept_button.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Adyasha's Password Generator")
app.geometry("400x350")
app.configure(bg="#89CFF0")

title_label = tk.Label(app, text="Adyasha's Password Generator", bg="#89CFF0", font=("Arial", 16, "bold"), fg="#0A4876")
title_label.pack(pady=10)

frame = tk.Frame(app, borderwidth=2, relief="ridge", bg="#C6E2FF")
frame.pack(pady=20)

name_label = tk.Label(frame, text="Enter Your Name:", bg="#C6E2FF")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(frame, bg="white", relief="solid")
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

length_label = tk.Label(frame, text="Enter Password Length:", bg="#C6E2FF")
length_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

length_entry = tk.Entry(frame, bg="white", relief="solid")
length_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

generate_button = tk.Button(frame, text="Generate Password", command=generate_password, bg="#47A6C2", fg="white", relief="raised")
generate_button.grid(row=2, columnspan=2, pady=10)

password_label = tk.Label(frame, text="", bg="#C6E2FF", font=("Arial", 12, "bold"), fg="#0A4876")
password_label.grid(row=3, columnspan=2, pady=10)

password_output = tk.Label(frame, text="", bg="white", relief="solid", font=("Arial", 12), width=24)
password_output.grid(row=4, columnspan=2, pady=10)

regenerate_button = tk.Button(frame, text="Regenerate", command=regenerate_password, state=tk.DISABLED, bg="#47A6C2", fg="white", relief="raised")
regenerate_button.grid(row=5, column=0, padx=10, pady=10)

accept_button = tk.Button(frame, text="Accept", command=accept_password, state=tk.DISABLED, bg="#47A6C2", fg="white", relief="raised")
accept_button.grid(row=5, column=1, padx=10, pady=10)

clear_button = tk.Button(frame, text="Clear", command=clear_password, bg="#E53535", fg="white", relief="raised")
clear_button.grid(row=6, columnspan=2, pady=10)

app.mainloop()
