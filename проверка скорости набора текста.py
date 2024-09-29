import time
import random

# Список текстов для тестирования
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an interpreted, high-level, general-purpose programming language.",
    "Practice makes perfect."
]

# Выбор случайного текста
text = random.choice(texts)

# Отображение текста для набора
print("Type the following text:")
print(text)

# Запуск таймера
start_time = time.time()

# Ввод текста пользователем
user_input = input("Your text: ")

# Остановка таймера
end_time = time.time()

# Вычисление времени набора
elapsed_time = end_time - start_time

# Вычисление скорости набора
words = len(text.split())
speed = words / (elapsed_time / 60)

# Вывод результатов
print(f"Time taken: {elapsed_time:.2f} seconds")
print(f"Speed: {speed:.2f} words per minute")
