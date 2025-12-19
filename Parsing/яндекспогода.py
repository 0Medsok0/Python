import requests
from bs4 import BeautifulSoup
import sys

def get_weather(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Ошибка при получении страницы: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Пытаемся найти текущую погоду по разным силекторам
    # Yandex часто меняет классы, поэтому используем несколько вариантов
    
    # 1. Температура
    temp = None
    temp_element = soup.select_one('.temp__value.temp__value_with-unit')
    if not temp_element:
        temp_element = soup.select_one('.fact__temp .temp__value')
    
    if temp_element:
        temp = temp_element.text.strip()
    
    # 2. Состояние (облачность, осадки)
    condition = None
    condition_element = soup.select_one('.link__condition')
    if not condition_element:
        condition_element = soup.select_one('.fact__condition')
        
    if condition_element:
        condition = condition_element.text.strip()
        
    # Вывод результатов
    if temp:
        print(f"Температура: {temp}")
    else:
        print("Не удалось найти информацию о температуре.")
        # Debug: print logic to see what we got if failed
        # print(soup.prettify()[:1000]) 

    if condition:
        print(f"Погода: {condition}")
    else:
        print("Не удалось найти информацию о погодных условиях.")

if __name__ == "__main__":
    url = "https://yandex.ru/pogoda/ru/belokurikha"
    get_weather(url)
