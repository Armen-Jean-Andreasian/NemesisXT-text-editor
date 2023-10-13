import tkinter as tk
import json
import os

from src.modules.gui.theme_manager import ThemeManager
from src.modules.gui.text_editor_settings import TextSettings
from src.modules.file_managment.file_manager import FileManager


class TextEditor:
    """
    TextEditor is a simple text editor application built using the tkinter library.

    Attributes:
        __THEMES_FILEPATH (str): The default path to the themes configuration file.
        root (tkinter.Tk): The main application window.
        menu (tkinter.Menu): The menu bar for the application.
        text (tkinter.Text): The text editing widget.
        themes (dict): A dictionary containing color themes for the text editor.

    Methods:
        __init__(self, filepath_=None): Initializes the TextEditor instance.
    """

    __THEMES_FILEPATH = os.path.abspath(os.path.join(os.getcwd(), "files/themes.json"))
    __LOGO_FILEPATH = os.path.abspath(os.path.join(os.getcwd(), "files/token.ico"))

    def __init__(self, filepath_=None, logo_filepath=None):
        if filepath_:
            self.__THEMES_FILEPATH = filepath_

        if logo_filepath:
            self.__LOGO_FILEPATH = logo_filepath


        with open(self.__THEMES_FILEPATH) as file:
            self.themes = json.load(file)

        # defining the settings
        self.root = tk.Tk()
        self.root.title("Nemesis-XT")
        self.root.iconbitmap(default=self.__LOGO_FILEPATH)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.text = tk.Text(self.root)
        self.text.pack()

        # initialization of subclasses
        theme_manager = ThemeManager(themes=self.themes, text=self.text)
        file_manager = FileManager(text=self.text, root=self.root)
        text_settings = TextSettings(text=self.text)

        # typing
        self.text.bind("<Tab>", text_settings.insert_spaces)  # Bind the Tab key press event to insert 4 spaces

        # menu-bar
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=file_manager.open_file)
        self.file_menu.add_command(label="Save", command=file_manager.save_file)
        self.file_menu.add_command(label="Exit", command=file_manager.on_closing)

        self.edit_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Clear", command=text_settings.clear_text)

        # themes
        self.themes_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Themes", menu=self.themes_menu)
        self.themes_menu.add_command(label="Dark", command=lambda: theme_manager.set_theme(chosen_theme='dark'))
        self.themes_menu.add_command(label="Light", command=lambda: theme_manager.set_theme(chosen_theme='light'))

        # exit
        self.root.protocol(name="WM_DELETE_WINDOW", func=file_manager.on_closing)


if __name__ == '__main__':
    app = TextEditor(filepath_='../../files/themes.json', logo_filepath='../../files/logo.ico')
    app.root.mainloop()
