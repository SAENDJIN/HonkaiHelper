import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
def greet():
    print(f'Hey, {user_name.get() or "World"}')


root = tk.Tk()
# root.geometry("200x150")

root.columnconfigure(0, weight=1)

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.grid(row=0, column=0, sticky="EW")

name_lbl = ttk.Label(input_frame, text="Name: ")
name_lbl.grid(row=0, column=0, padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=30, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()

# ttk.Label(root, text="Hello", padding=(30, 10)).pack()

buttons = ttk.Frame(root, padding=(20, 10))
buttons.grid(row=1, column=0, sticky="EW")

buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW")

quick_btn = ttk.Button(buttons, text="Quit", command=root.destroy)
quick_btn.grid(row=0, column=1, sticky="EW")

root.mainloop()
