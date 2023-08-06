import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class HonkaiHelper(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("StarRail Helper")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

        for FrameClass in (MainPage, CharactersInfo, ArtifactInfo):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(MainPage)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class MainPage(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        character_button = ttk.Button(
            self,
            text="Character INFO",
            command=lambda: controller.show_frame(CharactersInfo)
        )
        character_button.grid(column=0, row=0, columnspan=1, sticky="EW")

        relict_button = ttk.Button(
            self,
            text="Relict INFO",
            command=lambda: controller.show_frame(CharactersInfo)
        )
        relict_button.grid(column=0, row=1, columnspan=1, sticky="EW",  )


class CharactersInfo(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        character_button = ttk.Button(
            self,
            text="Back",
            command=lambda: controller.show_frame(MainPage)
        )
        character_button.grid(column=1, row=4, columnspan=2, sticky="NSEW")


class ArtifactInfo(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller
        character_button = ttk.Button(
            self,
            text="Back",
            command=lambda: controller.show_frame(MainPage)
        )
        character_button.grid(column=1, row=4, columnspan=2, sticky="EW")

        # Create a label to display the selected artifact image
        self.image_label = tk.Label(self)
        self.image_label.grid()

        # Call the show_relict_info method to initialize the dropdown menu
        self.show_relict_info()

    def show_relict_info(self):
        artifacts = ["Band of Sizzling Thunder",
                     "Champion of Streetwise Boxing",
                     "Eagle of Twilight Line",
                     "Firesmith of Lava-Forging",
                     "Genius of Brilliant Stars",
                     "Guard of Wuthering Snow",
                     "Hunter of Glacial Forest",
                     "Knight of Purity Palace",
                     "Longevous Disciple",
                     "Messenger Traversing Hackerspace",
                     "Musketeer of Wild Wheat",
                     "Passerby of Wandering Cloud",
                     "Thief of Shooting Meteor",
                     "Wastelander of Banditry Desert"]

        var = tk.StringVar(self)
        var.set(artifacts[0])  # Set the default artifact

        option_menu = tk.OptionMenu(self, var, *artifacts)
        option_menu.grid(pady=10)

        var.trace("w", lambda *args: self.relict_info(var.get()))

        # Call relict_info to initialize the image
        self.relict_info(var.get())

    def relict_info(self, selected_option):
        image_filename = f"/Users/veronika/PycharmProjects/HonkaiHelper/image_relict/{selected_option}.png"
        image = Image.open(image_filename)
        image = image.resize((200, 200))  # Resize the image if needed
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference to prevent garbage collection



root = HonkaiHelper()
root.mainloop()
