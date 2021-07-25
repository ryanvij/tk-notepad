import os
import webbrowser
from pathlib import Path
from tkinter import Tk, Button, Frame, Label, filedialog, scrolledtext, constants


# NotePad class
class NotePad:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.saved = False
        self.root = Tk()  # Initializing root window.

        self.about = None
        self.github_link = None
        self.info = None

        # Setting filename as "Untitled and creating empty file_path variable. To be updated after file is saved. "
        self.filename = "Untitled"
        self.file_path = ""

        # status_bar frame located at North-West.
        self.status_bar = Frame(self.root)
        self.status_bar.pack(side="top", anchor="nw")

        # Buttons on status_bar frame.
        self.new = Button(self.status_bar, width=7, height=1, text="New", command=self.new_file)
        self.open = Button(self.status_bar, width=7, height=1, text="Open", command=self.open_file)
        self.save_as = Button(self.status_bar, width=7, height=1, text="Save As", command=self.save_as_textfile)
        self.save = Button(self.status_bar, width=7, height=1, text="Save", command=self.save_existing)
        self.about_page = Button(self.status_bar, width=7, height=1, text="About", command=self.about_page)

        # text_area using ScrolledText, to facilitate scrolling. wrap="word" and undo=True"
        self.text_area = scrolledtext.ScrolledText(self.root, wrap="word", undo=True)

        # Labels on about window.
    def update_title(self, title):
        self.root.title(f"{title} - Notepad")

    # Opens github repository on default browser.
    @staticmethod
    def callback(url):
        webbrowser.open_new(url)

    # Called when About button is clicked.
    def about_page(self):
        self.about = Tk()
        self.about.resizable(width=True, height=False)
        self.about.title("About")
        self.about.geometry("400x300")

        self.info = Label(self.about, text="This a Notepad program developed by ryanvij, using Tkinter.")
        self.github_link = Label(self.about, text="Github Repository", fg="blue", font="Verdana 7 underline")
        # Packing info and github_link
        self.info.pack()
        self.github_link.pack()

        # Binding github_link to github repo.
        self.github_link.bind("<Button-1>", lambda e: self.callback("https://github.com/ryanvij/tk-notepad"))
        self.about_page.mainloop()

    # Opens already existing file.
    def open_file(self):
        self.file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=(("Text File", "*.txt"),))
        with open(self.file_path, "r+") as f:
            text = f.read()

        # Clear text_are
        self.text_area.delete('1.0', constants.END)
        self.update_title(os.path.basename(self.file_path))
        self.text_area.insert("1.0", text)

    # Destroy root and create new window.
    def new_file(self):
        self.root.destroy()
        nt = NotePad(800, 600)
        nt.run()

    # Overwrite existing file.
    def save_existing(self):
        try:
            if self.saved:
                # Opening file with "w" mode.
                with open(self.file_path, "w") as f:
                    # Truncating file to clear it.
                    f.truncate(0)
                    f.write(self.text_area.get("1.0", constants.END))
            else:
                self.save_as_textfile()
        except FileNotFoundError:
            pass

    # Save as a new text file.
    def save_as_textfile(self):
        # Using asksaveasfilename from tkinter.filedialog to save .txt filepath
        self.file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text File", "*.txt"),))
        try:
            # Opening file with "w+" mode.
            with open(self.file_path, "w+") as f:
                f.write(self.text_area.get("1.0", constants.END))
            # Getting filename from filepath and setting the title.
            self.update_title(os.path.basename(self.file_path))
            self.saved = True
        except FileNotFoundError:
            pass

    def run(self):
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

        # Packing text_area.
        self.text_area.pack(expand=True, fill="both")

        self.root.mainloop()


notepad = NotePad(800, 600)
notepad.run()

