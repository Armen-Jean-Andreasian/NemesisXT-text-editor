import tkinter as tk
import json

from src.modules.gui.themes.theme_manager import ThemeManager

from src.modules.gui.functional import StandAloneFunctions
from src.modules.gui.fonts.gui_font_settings import FontSettings

from src.modules.file_managment.file_manager import FileManager


from src.modules.gui.keyboard.gui_keyboard_settings import Keyboard

from files.config import FilePaths


class TextEditor:
    """
    TextEditor is a simple text editor application built using the tkinter library.

    Attributes:
        __THEMES_FILEPATH (str): The default path to the themes configuration file.
        __LOGO_FILEPATH (str): The default path to logo.

        root (tkinter.Tk): The main application window.
        menu (tkinter.Menu): The menu bar for the application.
        text (tkinter.Text): The text editing widget.
        themes (dict): A dictionary containing color themes for the text editor.

    Methods:
        __init__(self, filepath_=None): Initializes the TextEditor instance.
    """
    __THEMES_FILEPATH = FilePaths().themes_filepath
    __LOGO_FILEPATH = FilePaths().logo_filepath

    def __init__(self):
        # loading themes
        with open(self.__THEMES_FILEPATH) as file:
            self.themes = json.load(file)

        # defining the settings
        self.root = tk.Tk()
        self.root.title("Nemesis-XT")
        self.root.iconbitmap(default=self.__LOGO_FILEPATH)
        self.root.geometry("800x600")  # Set your preferred initial window size

        # main menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # editor widget
        self.text = tk.Text(self.root)
        self.text.pack(fill="both", expand=True)  # full-size

        # initialization of subclasses
        theme_manager = ThemeManager(themes=self.themes, text=self.text)
        file_manager = FileManager(text=self.text, root=self.root)
        text_settings = StandAloneFunctions(text=self.text)
        font_settings = FontSettings(text=self.text)
        keyboard_settings = Keyboard(text=self.text)

        # hotkeys
        self.text.bind("<Tab>", keyboard_settings.tab_forward)  # Bind the Tab key press event to insert 4 spaces
        self.text.bind("<Shift-Tab>", keyboard_settings.tab_backward)  # Bind the Tab key press event to insert 4 spaces
        self.text.bind("<Control-MouseWheel>", font_settings.change_font_size)  # Font size adjustment Ctrl + Wheel

        # File tab
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=file_manager.open_file)
        self.file_menu.add_command(label="Save", command=file_manager.save_file)
        self.file_menu.add_command(label="Exit", command=file_manager.on_closing)

        # Edit tab
        self.edit_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Clear", command=text_settings.clear_text)

        # Themes tab
        self.themes_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Themes", menu=self.themes_menu)
        self.themes_menu.add_command(label="Atom", command=lambda: theme_manager.set_theme(chosen_theme='atom'))
        self.themes_menu.add_command(label="Sublime-Text",
                                     command=lambda: theme_manager.set_theme(chosen_theme='sublime-text'))
        self.themes_menu.add_command(label="Black & White",
                                     command=lambda: theme_manager.set_theme(chosen_theme='black'))
        self.themes_menu.add_command(label="Light", command=lambda: theme_manager.set_theme(chosen_theme='light'))

        # Settings tab
        self.settings_menu = tk.Menu(self.menu, tearoff=False)
        self.settings_menu.add_cascade(label="Settings", menu=self.settings_menu)

        # exit
        self.root.protocol(name="WM_DELETE_WINDOW", func=file_manager.on_closing)


if __name__ == '__main__':
    app = TextEditor()
    app.root.mainloop()
