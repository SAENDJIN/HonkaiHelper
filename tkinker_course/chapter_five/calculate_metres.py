import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from tkinker_course.chapter_three.windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)

metres_value = tk.StringVar()
feet_value = tk.StringVar()

def calculate_feet(*args):
    try:
        metres = float(metres_value.get())
        feet = metres * 3.28084
        feet_value.set(f"{feet:3f}")
    except ValueError:
        pass



main = ttk.Frame(root, padding=(60, 30))
main.grid()

root.columnconfigure(0, weight=1)


metres_label = ttk.Label(main, text="Metres:")
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Segoe UI", 15))
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, text="Feet shown here", textvariable=feet_value)
calc_btn = ttk.Button(main, text="Calculate", command=calculate_feet)

metres_label.grid(column=0, row=0, sticky="w")
metres_input.grid(column=1, row=0, sticky="ew")
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="w")
feet_display.grid(column=1, row=1, sticky="ew")

calc_btn.grid(column=0, row=2, columnspan=2, sticky="ew")

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)


root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()
