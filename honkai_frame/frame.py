import tkinter as tk
from tkinter import ttk


class HonkaiHelper(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("StarRail Helper")
        self.geometry("600x800")
        self.resizable(False, False)
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky="EW", )

        for FrameClass in (MainPage, CharactersInfo, ArtifactInfo):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW", )

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
        character_button.grid(column=1, row=4, columnspan=2, sticky="EW")

        relict_button = ttk.Button(
            self,
            text="Relict INFO",
            command=lambda: controller.show_frame(CharactersInfo)
        )
        relict_button.grid(column=1, row=3, columnspan=2, sticky="EW", )


class CharactersInfo(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        character_button = ttk.Button(
            self,
            text="Back",
            command=lambda: controller.show_frame(MainPage)
        )
        character_button.grid(column=1, row=4, columnspan=2, sticky="EW")


class ArtifactInfo(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        character_button = ttk.Button(
            self,
            text="Back",
            command=lambda: controller.show_frame(MainPage)
        )
        character_button.grid(column=1, row=4, columnspan=2, sticky="EW")


root = HonkaiHelper()
root.mainloop()
