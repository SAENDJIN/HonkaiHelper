import tkinter as tk
from tkinter import ttk
from tkinker_course.chapter_three.windows import set_dpi_awareness
from PIL import Image, ImageTk

set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

image = Image.open("C:\\Users\\andre\\PycharmProjects\\HonkaiHelper\\img_char\\Clara.webp"). \
    resize((128, 128))
photo = ImageTk.PhotoImage(image)

label = ttk.Label(root, text="Hello, world!", padding=20)
label.config(font=("Segot UI", 20))
label.pack()

label_img = ttk.Label(root, text="Clara", image=photo, padding=5, compound="top")
label_img.pack()

quick_btn = ttk.Button(root, text="Quit", command=root.destroy)
quick_btn.pack()

root.mainloop()
