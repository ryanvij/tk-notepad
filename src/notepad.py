from tkinter import Tk, Button
from pathlib import Path
from tkinter.scrolledtext import ScrolledText
import os


class NotePad:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.filename = "Untitled"
        self.save = Button(self.root, width=7, height=1, text="")
        self.text_area = ScrolledText(self.root, wrap="word")


    def configure(self):
        # Checks whether if "notepad_icon.ico" exists.
        if os.path.exists(Path(__file__).parent / "icons" / "notepad_icon.ico"):
            # Sets iconbitmap as notepad_icon.ico
            self.root.iconbitmap(Path(__file__).parent / "icons" / "notepad_icon.ico")
        # Defaults to tkinter icon
        else:
            pass

        # Geometry and Title
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title(f"{self.filename} - Notepad")
        self.save.pack(side="top", anchor="nw")
        self.text_area.pack(fill="both", expand=True, padx=0, pady=0)



    def run(self):
        self.root.mainloop()


notepad = NotePad(800, 600)
notepad.configure()
notepad.run()
