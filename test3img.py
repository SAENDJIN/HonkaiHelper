import tkinter as tk
from PIL import Image, ImageTk

# Dropdown menu options
options = ["Clara", "Natasha", "Sushang", "Trailblazer (Physical)",
           "Asta", "Himeko", "Hook", "Trailblazer (Fire)", "Gepard",
           "Herta", "March 7", "Pela", "Yanqing", "Arlan", "Bailu",
           "Jing Yuan", "Serval", "Tingyun", "Blade", "Bronya",
           "Dan Heng", "Sampo", "Qingque", "Seele", "Silver Wolf",
           "Luocha", "Welt", "Yukong"]

def update_image(selected_option, image_label):
    image_filename = f"img_char/{selected_option}.webp"
    image = Image.open(image_filename)
    image = image.resize((200, 200))  # Resize the image if needed
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference to prevent garbage collection

# Create the Tkinter window
root = tk.Tk()
root.title("Image Display")

# Explanation text label
explanation_label = tk.Label(root, text="Please select an option from the dropdown to see the corresponding image")
explanation_label.pack(pady=10)

# Create a StringVar to store the selected option
var = tk.StringVar(root)
var.set(options[0])  # Set the default option

# Dropdown menu
option_menu = tk.OptionMenu(root, var, *options)
option_menu.pack(pady=10)

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack()

# Update the image when the dropdown selection changes
var.trace("w", lambda *args: update_image(var.get(), image_label))

# Load and display the default image
update_image(var.get(), image_label)

root.mainloop()
