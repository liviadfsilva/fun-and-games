from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "ivory2"
row = 0
completed_tasks_row = 1

window = Tk()
window.title("To-Do List")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

def new_task():
    def view_tasks():
        try:
            with open("completed_tasks.txt", "r") as data_file:
                data = data_file.read()
        except FileNotFoundError:
            with open("completed_tasks.txt", "a") as data_file:
                data_file.write("")
        else:
            messagebox.showinfo(message=f"{data}\n")

    def task_done():
        def strike(text):
            result = ''
            for i in text:
                result = result + i + '\u0336'
            return result

        entry_info = entry.get()

        if entry.info == "":
            messagebox.showinfo(title="Error", message="There's no task to be checked.")
        else:
            with open("completed_tasks.txt", "a") as data_file:
                data_file.write(strike(entry_info) + "\n")

            new_text = strike(entry_info)
            entry.delete(0, END)
            entry.insert(0, new_text)

    global row, completed_tasks_row
    row += 1
    completed_tasks_row += 1
    checkbox_button = Checkbutton(highlightbackground=BACKGROUND_COLOR, highlightthickness=0, background=BACKGROUND_COLOR,
                            command=task_done)
    checkbox_button.grid(row=row, column=1)
    checkbox_button.config(padx=10, pady=10)

    entry = Entry(width=21)
    entry.grid(row=row, column=2)
    entry.focus_set()

    new_task_button.config(text="New Task")
    new_task_button.grid(row=row, column=3, padx=10, pady=10)

    view_completed_tasks_button = Button(text="View Completed Tasks", background=BACKGROUND_COLOR, highlightthickness=0,
                                         highlightbackground=BACKGROUND_COLOR, command=view_tasks)
    view_completed_tasks_button.grid(row=completed_tasks_row, column=2)

new_task_button = Button(text="Get Started", background=BACKGROUND_COLOR, highlightthickness=0,
                    highlightbackground=BACKGROUND_COLOR, command=new_task)
new_task_button.grid(row=0, column=2)

window.mainloop()