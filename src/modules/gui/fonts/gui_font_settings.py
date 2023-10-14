import tkinter as tk
from tkinter import font
import json

from files.config import FilePaths


class FontSettings:
    __SETTINGS_FILE_FILEPATH = FilePaths().settings_filepath

    def __init__(self, text: tk.Text):
        self.text = text
        self.font_size = self.__load_font_details()["default-settings"]["font_size"]

        self.text.bind("<Control-MouseWheel>", self.change_font_size)

        # Get the initial font information
        font_info = font.nametofont(text.cget("font"))

        # Create a separate font configuration to control the size
        self.font_size = font_info.actual()["size"]
        self.text_font = font.nametofont(text.cget("font"))


    def __load_font_details(self):
        """
        Retrieves the font details from config file.
        """
        with open(self.__SETTINGS_FILE_FILEPATH) as settings_file:
            settings = json.load(settings_file)
            return settings


    def change_font_size(self, event):
        if event.delta > 0:
            self.font_size += 1
        else:
            self.font_size -= 1

        # Create a new font with the updated size
        font_name = self.text.cget("font")
        font_name = font.nametofont(font_name)
        font_name.configure(size=self.font_size)

        # Update the text widget's font
        self.text.configure(font=font_name)
        # Saving user's choice
        self.save_user_font()


    def save_user_font(self):
        settings = {
            "default-settings": {
                "font_size": self.font_size,
            }
        }

        with open(self.__SETTINGS_FILE_FILEPATH, 'w') as settings_file:
            json.dump(settings, settings_file)


    @property
    def get_font_size(self):
        return self.font_size

    @property
    def get_font_family(self):
        pass
