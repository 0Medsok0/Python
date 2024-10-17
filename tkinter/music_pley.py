import pygame
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

pygame.init()

# Инициализировать музыкальный проигрыватель
pygame.mixer.init()

# Функция для загрузки музыки
def load_music():
    global path
    path = filedialog.askdirectory()
    if path:
        music_list.delete(*music_list.get_children())
        for i in os.listdir(path):
            if i.endswith(('.mp3', '.wav')):
                music_list.insert('', 'end', values=(i, path))

# Функция для воспроизведения музыки
def play_music():
    global current_song
    if music_list.selection():
        current_song = music_list.item(music_list.selection()[0], 'values')[0]
        pygame.mixer.music.load(os.path.join(path, current_song))
        pygame.mixer.music.play()
        play_button.config(text='Пауза')

# Функция для паузы/возобновления
def pause_music():
    if play_button['text'] == 'Пауза':
        pygame.mixer.music.pause()
        play_button.config(text='Продолжить')
    else:
        pygame.mixer.music.unpause()
        play_button.config(text='Пауза')

# Функция для остановки музыки
def stop_music():
    pygame.mixer.music.stop()
    play_button.config(text='Играть')

# Функция для перехода к следующей песне
def next_music():
    if music_list.selection():
        current_index = music_list.selection()[0]
        next_index = music_list.next(current_index)
        if next_index:
            music_list.selection_set(next_index)
            play_music()

# Функция для перехода к предыдущей песне
def prev_music():
    if music_list.selection():
        current_index = music_list.selection()[0]
        prev_index = music_list.prev(current_index)
        if prev_index:
            music_list.selection_set(prev_index)
            play_music()

# Создание окна
root = tk.Tk()
root.title("Музыкальный проигрыватель")

# Панель инструментов
toolbar = tk.Frame(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

# Кнопки
load_button = tk.Button(toolbar, text='Загрузить', command=load_music)
load_button.pack(side=tk.LEFT, padx=5)
play_button = tk.Button(toolbar, text='Играть', command=play_music)
play_button.pack(side=tk.LEFT, padx=5)
pause_button = tk.Button(toolbar, text='Пауза', command=pause_music)
pause_button.pack(side=tk.LEFT, padx=5)
stop_button = tk.Button(toolbar, text='Остановить', command=stop_music)
stop_button.pack(side=tk.LEFT, padx=5)
next_button = tk.Button(toolbar, text='Вперёд', command=next_music)
next_button.pack(side=tk.LEFT, padx=5)
prev_button = tk.Button(toolbar, text='Назад', command=prev_music)
prev_button.pack(side=tk.LEFT, padx=5)

# Список песен
music_list = ttk.Treeview(root, columns=('Имя', 'Путь'), show='headings')
music_list.heading('Имя', text='Имя')
music_list.heading('Путь', text='Путь')
music_list.pack(fill=tk.BOTH, expand=True)

# Запуск главного цикла
root.mainloop()