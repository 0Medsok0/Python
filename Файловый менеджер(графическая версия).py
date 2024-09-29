import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def list_files(path):
    files = os.listdir(path)
    file_list.delete(0, tk.END)
    for file in files:
        file_list.insert(tk.END, file)

def create_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        try:
            os.mkdir(folder_path)
            list_files(folder_path)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def delete_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            os.remove(file_path)
            list_files(os.path.dirname(file_path))
        except Exception as e:
            messagebox.showerror("Error", str(e))

def delete_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        try:
            shutil.rmtree(folder_path)
            list_files(os.path.dirname(folder_path))
        except Exception as e:
            messagebox.showerror("Error", str(e))

def rename_file():
    old_path = filedialog.askopenfilename()
    if old_path:
        new_path = filedialog.asksaveasfilename(initialfile=os.path.basename(old_path))
        if new_path:
            try:
                os.rename(old_path, new_path)
                list_files(os.path.dirname(new_path))
            except Exception as e:
                messagebox.showerror("Error", str(e))

def copy_file():
    src_path = filedialog.askopenfilename()
    if src_path:
        dst_path = filedialog.asksaveasfilename(initialfile=os.path.basename(src_path))
        if dst_path:
            try:
                shutil.copy(src_path, dst_path)
                list_files(os.path.dirname(dst_path))
            except Exception as e:
                messagebox.showerror("Error", str(e))

def move_file():
    src_path = filedialog.askopenfilename()
    if src_path:
        dst_path = filedialog.askdirectory()
        if dst_path:
            try:
                shutil.move(src_path, dst_path)
                list_files(os.path.dirname(src_path))
            except Exception as e:
                messagebox.showerror("Error", str(e))

# Создание графического интерфейса
root = tk.Tk()
root.title("File Manager")

file_list = tk.Listbox(root)
file_list.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

create_folder_button = tk.Button(button_frame, text="Create Folder", command=create_folder)
create_folder_button.pack(side=tk.LEFT)

delete_file_button = tk.Button(button_frame, text="Delete File", command=delete_file)
delete_file_button.pack(side=tk.LEFT)

delete_folder_button = tk.Button(button_frame, text="Delete Folder", command=delete_folder)
delete_folder_button.pack(side=tk.LEFT)

rename_file_button = tk.Button(button_frame, text="Rename File", command=rename_file)
rename_file_button.pack(side=tk.LEFT)

copy_file_button = tk.Button(button_frame, text="Copy File", command=copy_file)
copy_file_button.pack(side=tk.LEFT)

move_file_button = tk.Button(button_frame, text="Move File", command=move_file)
move_file_button.pack(side=tk.LEFT)

list_files("/")

root.mainloop()
