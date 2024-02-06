import requests
from bs4 import BeautifulSoup
import json
import os
# ссылка на картинки
url_img = 'http://www2.bigpi.biysk.ru/wwwsite'
# ссылка на страницы
base_url = "http://www2.bigpi.biysk.ru/wwwsite/news.php?rowstart="
# папка для хранения картинок
img_folder = 'img'
# Проверяем, существует ли папка
if not os.path.exists(img_folder):
    os.makedirs(img_folder)

# Словарь для хранения данных о картинках
images_data = {}
# Путь к папке для сохранения JSON файла
json_file = "images_data.json"
Start = 100     # с какой страницы начать качать картинки
End = 104       # на какой странице закончить качать картинки
x =4*( Start -1)
y = x +(End -Start)*4
# Цикл по значениям параметра rowstart от 0 до 1206 с шагом 4(нумерация страниц имеет такой шаг), перебираем страницы с 4мя картинками
# для начала второй параметр укажем небольшое число например 16
for rowstart in range(x, y, 4):
    url = base_url + str(rowstart)
    # Загрузка страницы
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # каждая картинка нахрдятся в табличном элементе <td class='newsnews'>
        # Поиск всех элементов <td class='newsnews'> как news_td(обычно их 4 элемента) на странице - в каждом есть картинка в теге img
        news_tds = soup.find_all('td', class_='newsnews')
        for news_td in news_tds: # перебор картинок из каждого элемента <td>
            img_src = url_img+'/'+news_td.find('img')['src'] # формируем ссылку на скачивание картинки
            img_name = img_src.split('/')[-1]                # получаем имя картинки с расширением jpg, png
            with open(os.path.join(img_folder, img_name), 'wb') as f:
                img_response = requests.get(img_src)  # получаем картинку
                f.write(img_response.content)         # сохраняем картинку
            images_data[img_name] = img_src           # собираем словарь для json
        # Сохранение данных о картинках в JSON файле
        with open(json_file, 'w') as file:
            json.dump(images_data, file,  indent=4)
    else:
        print(f"Не удалось загрузить страницу: {url}")
