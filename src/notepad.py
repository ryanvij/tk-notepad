import tkinter.filedialog
from tkinter import Tk, Button, Frame, Label
from pathlib import Path
from tkinter.scrolledtext import ScrolledText
import os
import webbrowser


# NotePad class
class NotePad:
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.root = Tk()

        # Setting filename as "Untitled and creating empty file_path variable. To be updated after file is saved. "
        self.filename = "Untitled"
        self.file_path = ""

        # Status bar frame located at North-West.
        self.status_bar = Frame(self.root)
        self.status_bar.pack(side="top", anchor="nw")

        # Save as Save As.. buttons on frame status_bar
        self.new = Button(self.status_bar, width=7, height=1, text="New", command=self.new_file)
        self.open = Button(self.status_bar, width=7, height=1, text="Open", command=self.open_file)
        self.save_as = Button(self.status_bar, width=7, height=1, text="Save As", command=self.save_as_textfile)
        self.save = Button(self.status_bar, width=7, height=1, text="Save", command=self.save_existing)
        self.about_page = Button(self.status_bar, width=7, height=1, text="About", command=self.about_page)

        # text_area using ScrolledText, to facilitate scrolling. wrap="word" and undo=True"
        self.text_area = ScrolledText(self.root, wrap="word", undo=True)

    def callback(self, url):
        webbrowser.open_new(url)

    def about_page(self):
        self.about_page = Tk()
        self.about_page.resizable(width=True, height=False)
        self.about_page.title("About")
        self.about_page.geometry("400x300")
        self.info = Label(self.about_page, text="This a Notepad program developed by ryanvij, using Tkinter.")
        self.info.pack()
        self.github_link = Label(self.about_page, text="Github Repository", fg="blue", font="Verdana 10 underline")
        self.github_link.pack()
        self.github_link.bind("<Button-1>", lambda e: self.callback("https://github.com/ryanvij/tk-notepad"))
        self.about_page.mainloop()

    def open_file(self):
        self.file_path = tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=(("Text File", "*.txt"),))
        with open(self.file_path, "r+") as f:
            text = f.read()
        self.text_area.delete('1.0', tkinter.END)
        self.root.title(f"{os.path.basename(self.file_path)} - Notepad")
        self.text_area.insert("1.0", text)

    def new_file(self):
        self.root.destroy()
        nt = NotePad(800, 600)
        nt.configure()
        nt.run()

    # Overwrite existing file.
    def save_existing(self):

        try:
            # Opening file with "w" mode.
            with open(self.file_path, "w") as f:
                # Truncating file to clear it.
                f.truncate(0)
                f.write(self.text_area.get("1.0", tkinter.END))
        except FileNotFoundError:
            pass

    # Save as a new text file.
    def save_as_textfile(self):
        # Using asksaveasfilename from tkinter.filedialog to save .txt filepath
        self.file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text File", "*.txt"),))
        try:
            # Opening file with "w+" mode.
            with open(self.file_path, "w+") as f:
                f.write(self.text_area.get("1.0", tkinter.END))

            # Getting filename from filepath and setting the title.
            self.filename = os.path.basename(self.file_path)
            self.root.title(f"{self.filename} - Notepad")
        except FileNotFoundError:
            pass

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

        # Packing buttons.
        self.new.pack(side="left")
        self.open.pack(side="left")
        self.save.pack(side="left")
        self.save_as.pack(side="left")
        self.about_page.pack(side="left")
        self.text_area.pack(expand=True, fill="both")


    def run(self):
        self.root.mainloop()


notepad = NotePad(800, 600)
notepad.configure()
notepad.run()
