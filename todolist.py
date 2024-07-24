import tkinter as tk
from tkinter import messagebox
def add_task():
    task=task_entry.get()
    if task:
        tasks.append(task)
        update_tasks()
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("warning","please enter a task")
def update_tasks():
    task_listbox.delete(0,tk.END)
    for task in tasks:
        tasks_listbox.insert(tk.END,task)

root= tk.Tk()
root.title("TO DO LIST")
tasks=[]
task_entry=tk.Entry(root,width=50)
task_entry.grid(row=0,column=0,padx=10,pady=10)
add_button=tk.Button(root,text="Add Task",command=add_task)
add_button.grid(row=0,column=1,padx=10,pady=10)
root.mainloop()