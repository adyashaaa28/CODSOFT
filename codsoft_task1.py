#A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists

import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import messagebox
from tkinter import simpledialog

def add_task():
    task = entry.get()
    if task:
        task_with_bullet = "• " + task
        listbox.insert(tk.END, task_with_bullet)
        all_tasks.append(task_with_bullet)
        entry.delete(0, tk.END)
        save_tasks()

def remove_task():
    selected_task_indices = listbox.curselection()
    for index in reversed(selected_task_indices):
        task = listbox.get(index)
        all_tasks.remove(task)
        listbox.delete(index)
        save_tasks()

def mark_done():
    selected_task_indices = listbox.curselection()
    for index in selected_task_indices:
        listbox.itemconfig(index, {'bg': 'light green'})
        listbox.selection_clear(index)
        save_tasks()

def clear_tasks():
    listbox.delete(0, tk.END)
    all_tasks.clear()
    save_tasks()

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines()
            for task in tasks:
                listbox.insert(tk.END, task)
                all_tasks.append(task)
    except FileNotFoundError:
        messagebox.showinfo("Info", "No saved tasks found")

def edit_task():
    selected_task_indices = listbox.curselection()
    if selected_task_indices:
        index = selected_task_indices[0]
        task = listbox.get(index)
        edited_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=task[2:])
        if edited_task:
            all_tasks.remove(task)
            all_tasks.insert(index, "• " + edited_task)
            listbox.delete(index)
            listbox.insert(index, "• " + edited_task)
            save_tasks()

def on_task_select(event):
    selected_task_indices = listbox.curselection()
    if selected_task_indices:
        edit_button.config(state=tk.NORMAL)
    else:
        edit_button.config(state=tk.DISABLED)

def sort_tasks():
    tasks = listbox.get(0, tk.END)
    tasks = sorted(tasks)
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def filter_tasks():
    selected_filter = filter_var.get()
    listbox.delete(0, tk.END)

    if selected_filter == "All":
        tasks = all_tasks
    elif selected_filter == "Active":
        tasks = [task for task in all_tasks if listbox.itemcget(all_tasks.index(task), "bg") != "light green"]
    else:
        tasks = [task for task in all_tasks if listbox.itemcget(all_tasks.index(task), "bg") == "light green"]

    for task in tasks:
        listbox.insert(tk.END, task)

app = tk.Tk()
app.title("Adyasha's To-Do List App")
app.geometry("900x600")  # Adjusted app size
app.configure(bg="#b3b3ff")

font_style = tkfont.Font(family="Times New Roman", size=14)
bold_font_style = tkfont.Font(family="Times New Roman", size=16, weight="bold")

heading_label = tk.Label(app, text="Adyasha's To-Do List", font=bold_font_style, bg="#b3b3ff", fg="purple")
heading_label.pack(pady=10)

entry = tk.Entry(app, font=font_style)
entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task, font=font_style)
add_button.pack()

frame = ttk.Frame(app)
frame.pack(fill=tk.BOTH, expand=True)

listbox_font = tkfont.Font(family="Times New Roman", size=14)
listbox = tk.Listbox(frame, selectmode=tk.SINGLE, bg="#E6E6FA", font=listbox_font)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

button_frame = ttk.Frame(app)
button_frame.pack(pady=10)

remove_button = ttk.Button(button_frame, text="Remove Task", command=remove_task)
done_button = ttk.Button(button_frame, text="Mark as Done", command=mark_done)
clear_button = ttk.Button(button_frame, text="Clear All", command=clear_tasks)
save_button = ttk.Button(button_frame, text="Save Tasks", command=save_tasks)
load_button = ttk.Button(button_frame, text="Load Tasks", command=load_tasks)
sort_button = ttk.Button(button_frame, text="Sort", command=sort_tasks)
edit_button = ttk.Button(button_frame, text="Edit Task", command=edit_task, state=tk.DISABLED)

remove_button.grid(row=0, column=0, padx=5)
done_button.grid(row=0, column=1, padx=5)
clear_button.grid(row=0, column=2, padx=5)
save_button.grid(row=1, column=0, padx=5)
load_button.grid(row=1, column=1, padx=5)
sort_button.grid(row=1, column=2, padx=5)
edit_button.grid(row=0, column=3, padx=5)

filter_label = tk.Label(app, text="Filter:", font=font_style, bg="#b3b3ff")
filter_label.pack()
filter_var = tk.StringVar()
filter_var.set("All")
filter_options = ["All", "Active", "Completed"]
filter_menu = ttk.Combobox(app, textvariable=filter_var, values=filter_options)
filter_menu.pack(pady=10)

filter_button = tk.Button(app, text="Apply Filter", command=filter_tasks, font=font_style)
filter_button.pack()

all_tasks = []

load_tasks()

listbox.bind("<<ListboxSelect>>", on_task_select)

app.mainloop()
