import tkinter as tk
from tkinter import ttk
from tkinker_course.chapter_three.windows import set_dpi_awareness

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

programming_languages = ("C", "Go", "JS", "Python", "C#", "Rust")

langs = tk.StringVar(value=programming_languages)
langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode="extended")
langs_select.pack()


def handle_selection_change(event):
    selected_indices = langs_select.curselection()
    for selected_indice in selected_indices:
        print(langs_select.get(selected_indice))


langs_select.bind("<<ListboxSelect>>", handle_selection_change)

root.mainloop()

