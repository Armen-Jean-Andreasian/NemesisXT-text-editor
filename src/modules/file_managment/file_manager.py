import tkinter as tk
from tkinter import filedialog, messagebox  # Frame, Button, X


class FileManager:
    FILE_DIALOG_OPEN = False

    def __init__(self, text: tk.Text, root: tk.Tk):
        self.text = text
        self.root = root

    def open_file(self):
        """
        Open a new file in text editor.
        """
        if not self.FILE_DIALOG_OPEN:
            self.FILE_DIALOG_OPEN = True
            file_path = filedialog.askopenfilename()
            self.FILE_DIALOG_OPEN = False
            if file_path:
                with open(file_path, 'r') as file:
                    self.text.delete('1.0', tk.END)
                    self.text.insert('1.0', file.read())

    def save_file(self):
        """
        Saves the text as a file.
        """
        if not self.FILE_DIALOG_OPEN:
            self.FILE_DIALOG_OPEN = True
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt", filetypes=[("Text Files", "*.txt")], initialfile="NemesisXT-Note.txt")


            self.FILE_DIALOG_OPEN = False
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(self.text.get('1.0', tk.END))

    def on_closing(self):
        """
        Asks the user if he wants to save the changes on closing.
        """
        if len(self.text.get("1.0", "end-1c")) > 0:
            response = messagebox.askyesnocancel("Save Changes", "Do you want to save the changes before closing?")
            if response is True:
                self.save_file()
                self.root.destroy()
            elif response is False:
                self.root.destroy()
        else:
            self.root.destroy()
