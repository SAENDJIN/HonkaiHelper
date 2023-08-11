import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

name = ttk.Label(root, text="Hello, world!")
entry = ttk.Entry(root, width=15)
name.pack()

style.configure("TLabel", font=("Segoe UI", 20))

root.mainloop()
