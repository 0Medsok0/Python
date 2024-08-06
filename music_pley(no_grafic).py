import pygame
import os

pygame.init()

path = "D:/music" # Путь для песен
if not os.path.exists(path):
    os.mkdir(path)

# Инициализировать музыкальный проигрыватель
pygame.mixer.init()

# Загружаем и воспроизводим музыку
for i in os.listdir(path):
    pygame.mixer.music.load(os.path.join(path, i))  # Заменяем на актуальный путь
    pygame.mixer.music.play()

    stop = input("Поставим паузу?")
    if stop == "Да".lower():
        pygame.mixer.music.pause()
        contin = input(" Возпроизводить дальше? ")
        if contin == "Да".lower():
            pygame.mixer.music.unpause()

# Запускать программу до тех пор, пока музыка не закончится.
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(25)
    print(f'Сейчас играет: {i}')
    next_music = input("Следующая композиция? ")
    if next_music == "Да".lower:
        continue
    else:
        break

pygame.quit()

