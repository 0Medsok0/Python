import time
import socket
import random

def internet_speed_test():
    """Проверяет скорость интернета без использования библиотеки speedtest."""

    # Определение URL-адреса для тестирования
    test_url = "google.com"

    # Генерирование случайных пакетов данных
    data_sizes = [1024, 2048, 4096, 8192]
    data_size = random.choice(data_sizes)

    # Создание сокета
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Подключение к серверу
        sock.connect((test_url, 80))

        # Отправка данных
        start_time = time.time()
        sock.send(bytes("GET / HTTP/1.1\nHost: " + test_url + "\n\n", "ascii"))

        # Получение данных
        sock.recv(data_size)
        end_time = time.time()

        # Вычисление скорости
        download_speed = data_size / (end_time - start_time)

        # Преобразование скорости в Мбит/с
        download_speed_mbps = download_speed / 1024 / 1024 * 8

        # Вывод результата
        print("Скорость интернета: {:.2f} Мбит/с".format(download_speed_mbps))

    except Exception as e:
        print("Ошибка при тестировании:", e)

    finally:
        # Закрытие сокета
        sock.close()

if __name__ == "__main__":
    internet_speed_test()
