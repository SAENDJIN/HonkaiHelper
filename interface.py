import tkinter as tk


root = tk.Tk()
root.title('Star Rail Helper')

window_width = 800
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


selected_option = tk.StringVar()
choices = ['Passerby of Wandering Cloud',
    'Musketeer of Wild Wheat',
    'Hunter of Glacial Forest',
    'Knight of Purity Palace',
    'Band of Sizzling Thunder',
    'Champion of Streetwise Boxing',
    'Thief of Shooting Meteor',
    'Guard of Wuthering Snow',
    'Genius of Brilliant Stars',
    'Eagle of Twilight Line',
    'Firesmith of Lava-Forging',
    'Wastelander of Banditry Desert']
dropdown_menu = tk.OptionMenu(root, selected_option, *choices)
selected_option.set(choices[0])  # Set the default option
dropdown_menu.pack()



root.mainloop()
