import tkinter as tk
from tkinter import ttk
from tkinker_course.chapter_three.windows import set_dpi_awareness
set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

text = tk.Text(root, height=8)
text.pack()

text.insert("1.0", "Please enter a comment...")
text["state"] = "normal"  # disable



def abc():
    text_content = text.get("1.0", "end")
    print(text_content)


button = ttk.Button(root, text="print", command=abc)
button.pack()

quick_btn = ttk.Button(root, text="Quit", command=root.destroy)
quick_btn.pack()

root.mainloop()
