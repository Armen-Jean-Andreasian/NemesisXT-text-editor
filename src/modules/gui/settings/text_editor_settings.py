import tkinter as tk


class TextSettings:

    def __init__(self, text: tk.Text):
        self.text = text

    def clear_text(self):
        """
        Clears the content of the text widget.
        """
        self.text.delete('1.0', tk.END)
