import tkinter as tk
from tkinter import filedialog, messagebox  # Frame, Button, X
import json
import os

file_dialog_open = False


class TextEditor:
    filepath = os.path.join(os.getcwd(), "src/themes.json")

    def __init__(self, filepath_=None):
        if filepath_:
            TextEditor.filepath = filepath_

        with open(TextEditor.filepath) as file:
            self.themes = json.load(file)

        self.root = tk.Tk()
        self.root.title("Text Editor")
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=self.on_closing)

        self.edit_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Clear", command=self.clear_text)
        self.text = tk.Text(self.root)


        self.text.bind("<Tab>", self.insert_spaces)  # Bind the Tab key press event to insert 4 spaces

        self.themes_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Themes", menu=self.themes_menu)
        self.themes_menu.add_command(label="Dark", command=lambda: self.__set_theme(chosen_theme='dark'))
        self.themes_menu.add_command(label="Light", command=lambda: self.__set_theme(chosen_theme='light'))

        self.text.pack()
        self.root.protocol(name="WM_DELETE_WINDOW", func=self.on_closing)

    def insert_spaces(self, _):
        """ Inserts 4 spaces when the Tab key is pressed """
        self.text.insert(tk.INSERT, chars="    ")
        return 'break'  # Prevents default tab behavior

    def __set_theme(self, chosen_theme: str):
        """
        Set the color theme of the Text Editor.

        :param chosen_theme: A string specifying the theme name (e.g., 'light' or 'dark').
        """
        if chosen_theme in self.themes:
            current_theme = self.themes[chosen_theme]

            # [Fix-needed]
            # supposed to set dark theme for header and menus, but only menus are affected
            """
            self.root.configure(bg=current_theme["background"])
            
            self.menu.configure(bg=current_theme["menu_background"], fg=current_theme["menu_foreground"])
            self.file_menu.configure(bg=current_theme["menu_background"], fg=current_theme["menu_foreground"])
            self.edit_menu.configure(bg=current_theme["menu_background"], fg=current_theme["menu_foreground"])
            """

            self.text.configure(bg=current_theme["text_background"], fg=current_theme["text_foreground"])
            self.text.configure(insertbackground=current_theme["text_foreground"])  # Set cursor color to text color

    def open_file(self):
        """
        Open a new file in text editor.
        """
        global file_dialog_open
        if not file_dialog_open:
            file_dialog_open = True
            file_path = filedialog.askopenfilename()
            file_dialog_open = False
            if file_path:
                with open(file_path, 'r') as file:
                    self.text.delete('1.0', tk.END)
                    self.text.insert('1.0', file.read())

    def save_file(self):
        """
        Saves the text as a file.
        """
        global file_dialog_open
        if not file_dialog_open:
            file_dialog_open = True
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            file_dialog_open = False
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(self.text.get('1.0', tk.END))

    def clear_text(self):
        """
        Clears the editor's text field.
        """
        self.text.delete('1.0', tk.END)

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


if __name__ == '__main__':
    app = TextEditor(filepath_='themes.json')
    app.root.mainloop()
