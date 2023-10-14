import tkinter as tk
from tkinter import font
import os
import json


class TextSettings:
    __SETTINGS_FILE_FILEPATH = os.path.abspath(os.path.join(os.getcwd(), "files/settings.json"))

    def __init__(self, text: tk.Text):
        self.text = text
        with open(self.__SETTINGS_FILE_FILEPATH) as settings_file:
            settings = json.load(settings_file)

            default_settings = settings["default-settings"]  # Set your initial font size here

        self.font_size = default_settings["font_size"]
        self.text.bind("<Control-MouseWheel>", self.change_font_size)

        # Get the initial font information
        font_info = font.nametofont(text.cget("font"))

        # Create a separate font configuration to control the size
        self.font_size = font_info.actual()["size"]
        self.text_font = font.nametofont(text.cget("font"))

    def tab_forward(self, _):
        """
        Inserts 4 spaces when the Tab key is pressed.

        Args:
            _ : An argument to capture the event (not used).

        Returns:
            str: 'break' to prevent the default tab behavior in the text widget.
        """
        self.text.insert(tk.INSERT, chars="    ")
        return 'break'

    def tab_backward(self, event):
        """
        Remove 4 spaces when the combination Shift + Tab is pressed.

        Args:
            event: An argument that captures the event.

        Returns:
            str: 'break' to prevent the default behavior.
        """
        current_position = self.text.index(tk.INSERT)

        # Check if the cursor is at the beginning of the line
        if current_position.endswith(".0"):
            return 'break'

        prev_char_index = self.text.index(f"{current_position} - 4 chars")

        # Check if the previous 4 characters are spaces, and if they are, remove them
        if self.text.get(prev_char_index, current_position) == "    ":
            self.text.delete(prev_char_index, current_position)
            self.text.mark_set(tk.INSERT, prev_char_index)

        return 'break'

    def clear_text(self):
        """
        Clears the content of the text widget.
        """
        self.text.delete('1.0', tk.END)

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
