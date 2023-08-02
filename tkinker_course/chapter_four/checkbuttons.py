import tkinter as tk
from tkinter import ttk
from tkinker_course.chapter_three.windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

check_button = ttk.Checkbutton(root, text="Check me!")
check_button.pack()

check_button["state"] = "disabled"  # "normal" is the counterpart

selected_option = tk.StringVar()


def print_current_option():
    print(selected_option.get())


check = ttk.Checkbutton(root, text="Check example", variable=selected_option,
                        command=print_current_option, onvalue="On", offvalue="Off")
check.pack()

root.mainloop()
