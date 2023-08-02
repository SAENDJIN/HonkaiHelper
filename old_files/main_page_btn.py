import tkinter as tk


def show_buttons():
    button1.pack()
    button2.pack()


def hide_buttons():
    button1.pack_forget()
    button2.pack_forget()


root = tk.Tk()

# Buttons Frame
buttons_frame = tk.Frame(root)
buttons_frame.pack()
# Buttons
button1 = tk.Button(buttons_frame, text="Choose character")
button2 = tk.Button(buttons_frame, text="Choose relict / Planetary Sets")
