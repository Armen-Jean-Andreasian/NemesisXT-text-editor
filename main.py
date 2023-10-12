import tkinter as tk
from tkinter import filedialog, messagebox

file_dialog_open = False


def open_file():
    global file_dialog_open
    if not file_dialog_open:
        file_dialog_open = True
        file_path = filedialog.askopenfilename()
        file_dialog_open = False
        if file_path:
            with open(file_path, 'r') as file:
                text.delete('1.0', tk.END)
                text.insert('1.0', file.read())


def save_file():
    global file_dialog_open
    if not file_dialog_open:
        file_dialog_open = True
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        file_dialog_open = False
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text.get('1.0', tk.END))


def clear_text():
    text.delete('1.0', tk.END)


def on_closing():
    if len(text.get("1.0", "end-1c")) > 0:
        response = messagebox.askyesnocancel("Save Changes", "Do you want to save the changes before closing?")
        if response is True:
            save_file()
            root.destroy()
        elif response is False:
            root.destroy()
    else:
        root.destroy()


root = tk.Tk()
root.title("Text Editor")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=on_closing)

edit_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear_text)

text = tk.Text(root)
text.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
