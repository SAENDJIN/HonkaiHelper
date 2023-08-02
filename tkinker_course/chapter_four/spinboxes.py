import tkinter as tk
from tkinter import ttk
from tkinker_course.chapter_three.windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

inital_value = tk.StringVar(value=20)
spin_box = tk.Spinbox(root, from_=0, to=30, textvariable=inital_value, wrap=False)
spin_box.pack()

print(spin_box.get())

root.mainloop()
