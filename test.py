import tkinter as tk

def show_dropdown():
    hide_buttons()
    dropdown_menu.pack()

def show_input():
    hide_buttons()
    input_frame.pack()

def hide_buttons():
    button1.pack_forget()
    button2.pack_forget()

def show_buttons():
    button1.pack()
    button2.pack()

def reset_all():
    input_field.delete(0, tk.END)
    dropdown_menu.pack_forget()
    input_frame.pack_forget()
    show_buttons()

root = tk.Tk()
root.title("Toggle Buttons and Show/Hide Widgets")

# Dropdown options
choices = ["Option 1", "Option 2", "Option 3", "Option 4"]
selected_option = tk.StringVar()

# Create a constant frame to hold the "Reset All" button
reset_frame = tk.Frame(root)
reset_frame.pack()

# Reset Button (on all pages)
reset_button = tk.Button(reset_frame, text="Reset All", command=reset_all)
reset_button.pack()

# Buttons Frame
buttons_frame = tk.Frame(root)
buttons_frame.pack()

# Buttons
button1 = tk.Button(buttons_frame, text="Show Dropdown", command=show_dropdown)
button2 = tk.Button(buttons_frame, text="Show Input", command=show_input)
button1.pack()
button2.pack()

# Dropdown Menu Frame
dropdown_frame = tk.Frame(root)
dropdown_frame.pack()

# Dropdown Menu
dropdown_menu = tk.OptionMenu(dropdown_frame, selected_option, *choices)

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack()

# Input Field
input_field = tk.Entry(input_frame)

# Start with the buttons frame visible
buttons_frame.tkraise()


window_width = 800
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.mainloop()
