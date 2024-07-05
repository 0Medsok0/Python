from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

# Собираем все ссылки на новсти, и описание новости
url = 'https://lenta.ru/' 

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')

# Маленькие новости
def head_news():
    
    description = soup.find_all('a', class_='card-mini _longgrid')
    list = []
    for des in description:
        for div in des.find_all('div', class_='card-mini__text'):
            result = {}
            f = des['href']
            result['link'] = 'https://lenta.ru/' + f
            result['description'] = div.text
            list.append(result)
            
        with open("mini-news.json", "w") as file:
            json.dump(list, file, indent=4, ensure_ascii=False)

# Большие новости 
def main_news():
        
    description_big = soup.find_all('a', class_='card-big _longgrid')
    list_1 = []
    for des_b in description_big:
        for div_b in des_b.find_all('div', class_='card-big__titles'):
            result_1 = {}
            f = des_b['href']
            result_1['link'] = 'https://lenta.ru/' + f
            result_1['description'] = div_b.text
            list_1.append(result_1)
            
        with open("big-news.json", "w") as file:
            json.dump(list_1, file, indent=4, ensure_ascii=False)
         
# Слайдер важное
def the_slider_is_important():
    news_list = soup.find_all('a', class_='card-big _slider _partners _news')
    list_2 = []
    for news in news_list:
        result_2 = {} 
        news_link = 'https://lenta.ru/' + news['href']
        news_text = news.text.strip()
        result_2['link'] = news_link
        result_2['text'] = news_text
        list_2.append(result_2)
            
        with open("slider-important.json", "w") as file:
            json.dump(list_2, file, indent=4, ensure_ascii=False)

# Популярное
def popular_photo():
    news_list = soup.find_all('a', class_='card-big _slider _dark _popular _article')
    list_3 = []
    for news_p in news_list:
        result_3 = {} 
        news_link = 'https://lenta.ru/' + news_p['href']
        news_text = news_p.text.strip()
        result_3['link'] = news_link
        result_3['text'] = news_text
        list_3.append(result_3)
            
        with open("slider-popular.json", "w") as file:
            json.dump(list_3, file, indent=4, ensure_ascii=False)

        
def main():
    print("Какие новости с сайта Lenta.ru хотите получить? ")
    print('Введите номер для получения информации')
    question = int(input(f' 1 -- Маленькие новости,\n 2 -- Большие новости,\n 3 -- Слайдер важные новости,\n 4 -- Слайдер популярные новости\n'))  
    if question == 1:
        head_news()
    if question == 2:
        main_news()
    if question == 3:
        the_slider_is_important()
    if question == 4:
        popular_photo()
        
if __name__ == '__main__':
    main()