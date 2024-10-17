import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Создание заметки
def create_note():
    def save_note():
        filename = entry_filename.get() + ".txt"
        content = text_content.get("1.0", tk.END)
        if filename:
            try:
                with open(filename, "w") as f:
                    f.write(content)
                messagebox.showinfo("Успех", "Заметка сохранена")
                window.destroy()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при сохранении: {e}")
        else:
            messagebox.showerror("Ошибка", "Введите название файла")

    window = tk.Toplevel(root)
    window.title("Создать заметку")

    label_filename = tk.Label(window, text="Название файла:")
    label_filename.grid(row=0, column=0, padx=5, pady=5)

    entry_filename = tk.Entry(window)
    entry_filename.grid(row=0, column=1, padx=5, pady=5)

    label_content = tk.Label(window, text="Содержимое:")
    label_content.grid(row=1, column=0, padx=5, pady=5)

    text_content = tk.Text(window, height=10, wrap=tk.WORD)
    text_content.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    button_save = tk.Button(window, text="Сохранить", command=save_note)
    button_save.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Просмотр содержимого заметки
def view_note():
    def close_window():
        window.destroy()

    filename = entry_filename.get() + ".txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read()
        window = tk.Toplevel(root)
        window.title("Просмотр заметки")
        text_content = tk.Text(window, height=10, wrap=tk.WORD)
        text_content.insert(tk.END, content)
        text_content.pack(padx=10, pady=10)
        text_content.config(state=tk.DISABLED)
        button_close = tk.Button(window, text="Закрыть", command=close_window)
        button_close.pack()
    else:
        messagebox.showerror("Ошибка", "Файл не найден")

# Удаление заметки
def delete_note():
    filename = entry_filename.get() + ".txt"
    if os.path.exists(filename):
        if messagebox.askyesno("Подтверждение", f"Удалить заметку {filename}?"):
            os.remove(filename)
            messagebox.showinfo("Успех", "Заметка удалена")
        else:
            messagebox.showinfo("Отмена", "Удаление отменено")
    else:
        messagebox.showerror("Ошибка", "Файл не найден")

# Редактирование заметки
def edit_note(entry_filename):
    def save_changes():
        filename = entry_filename.get() + ".txt"
        new_content = text_content.get("1.0", tk.END)
        if new_content:
            try:
                with open(filename, "w") as f:
                    f.write(new_content)
                messagebox.showinfo("Успех", "Заметка отредактирована")
                window.destroy()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Ошибка при сохранении: {e}")
        else:
            messagebox.showerror("Ошибка", "Введите новое содержимое")

    filename = entry_filename.get() + ".txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            content = f.read()
        window = tk.Toplevel(root)
        window.title("Редактирование заметки")
        label_filename = tk.Label(window, text="Название файла:")
        label_filename.grid(row=0, column=0, padx=5, pady=5)
        entry_filename = tk.Entry(window, state=tk.DISABLED)
        entry_filename.insert(0, filename[:-4])
        entry_filename.grid(row=0, column=1, padx=5, pady=5)
        label_content = tk.Label(window, text="Содержимое:")
        label_content.grid(row=1, column=0, padx=5, pady=5)
        text_content = tk.Text(window, height=10, wrap=tk.WORD)
        text_content.insert(tk.END, content)
        text_content.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        button_save = tk.Button(window, text="Сохранить", command=save_changes)
        button_save.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    else:
        messagebox.showerror("Ошибка", "Файл не найден")

# Главное меню
root = tk.Tk()
root.title("Блокнот")
root.geometry("300x200")

label_filename = tk.Label(root, text="Название файла:")
label_filename.grid(row=0, column=0, padx=5, pady=5)

entry_filename = tk.Entry(root)
entry_filename.grid(row=0, column=1, padx=5, pady=5)

def create_note_button():
    create_note()

def view_note_button():
    view_note()

def delete_note_button():
    delete_note()

def edit_note_button():
    edit_note(entry_filename)

button_create = tk.Button(root, text="Создать заметку", command=create_note_button)
button_create.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

button_view = tk.Button(root, text="Просмотреть заметку", command=view_note_button)
button_view.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

button_delete = tk.Button(root, text="Удалить заметку", command=delete_note_button)
button_delete.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

button_edit = tk.Button(root, text="Редактировать заметку", command=edit_note_button)
button_edit.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()