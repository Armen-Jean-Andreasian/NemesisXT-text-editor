import tkinter as tk
from tkinter import filedialog, messagebox

file_dialog_open = False


class TextEditor:
    def __init__(self):
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
        self.text.pack()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def open_file(self):
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
        global file_dialog_open
        if not file_dialog_open:
            file_dialog_open = True
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            file_dialog_open = False
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(self.text.get('1.0', tk.END))

    def clear_text(self):
        self.text.delete('1.0', tk.END)

    def on_closing(self):
        if len(self.text.get("1.0", "end-1c")) > 0:
            response = messagebox.askyesnocancel("Save Changes", "Do you want to save the changes before closing?")
            if response is True:
                self.save_file()
                self.root.destroy()
            elif response is False:
                self.root.destroy()
        else:
            self.root.destroy()
