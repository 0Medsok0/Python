import tkinter as tk
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, 'r') as file:
            text.delete('1.0', tk.END)
            text.insert('1.0', file.read())

def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath:
        with open(filepath, 'w') as file:
            file.write(text.get('1.0', tk.END))

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Simple Text Editor")

text = tk.Text(root)
text.pack()

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()