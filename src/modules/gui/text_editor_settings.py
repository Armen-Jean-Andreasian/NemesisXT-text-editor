import tkinter as tk


class TextSettings:
    def __init__(self, text: tk.Text):
        self.text = text

    def insert_spaces(self, _):
        """
        Inserts 4 spaces when the Tab key is pressed.

        Args:
            _ : An argument to capture the event (not used).

        Returns:
            str: 'break' to prevent the default tab behavior in the text widget.
        """
        self.text.insert(tk.INSERT, chars="    ")
        return 'break'

    def clear_text(self):
        """
        Clears the content of the text widget.
        """
        self.text.delete('1.0', tk.END)
