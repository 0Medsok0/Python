import os
import requests
from bs4 import BeautifulSoup
import json

# Скачиваем страницу
# url = 'https://rus.hitmotop.com/songs/top-today'
# response = requests.get(url)
# with open('music.html', 'w', encoding='utf-8') as file:
#     file.write(response.text)

# Открываем страницу

# with open('music.html', 'r', encoding='utf-8') as file:
#     src = file.read()
#     src = BeautifulSoup(src, 'lxml')
    # print(src.text)

# Проходим пагинацию
list_music = []
for i in range(1, 12):
    pages = {}
    pages = (f'/songs/top-today/start/{i * 48}')
    url = f'https://rus.hitmotop.com{pages}'
    response = requests.get(url)
    with open('music.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    with open('music.html', 'r', encoding='utf-8') as file:
        src = file.read()
        src = BeautifulSoup(src, 'lxml')
        all_links_music = src.find_all('a', class_='track__download-btn')
        for j in all_links_music:
            res = {}
            res['name'] = j['href']
            # list_music.append(res) !!
            if res['name'] != '':
                list_music.append(res)
with open('music.json', "w") as g:
    json.dump(list_music, g, indent=4, ensure_ascii=False)

path = "D:/music/"
os.makedirs(path, exist_ok=True)
with open('music.json', 'r') as f:
    data = json.load(f)
    for item in data:
        file_name = item['name'].split('/')[-1]
        file_path = os.path.join(path, file_name)
        # print(file_path)
        with open(file_path, 'w') as file:
            file.write(item['name'])

