import requests
from bs4 import BeautifulSoup

def get_fuel_prices():
    # Исходя из анализа, таблица с ценами находится на странице /t-belokuriha
    url = "https://fuelprice.ru/t-belokuriha" 
    
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
    
    # Ищем таблицу по ID, найденному при анализе страницы
    table = soup.select_one('#price_table')

    if not table:
        print("Не удалось найти таблицу с ценами (#price_table). Возможно, структура сайта изменилась.")
        return

    # Проходим по строкам тела таблицы
    rows = table.select('tbody > tr')
    
    data = []
    for row in rows:
        cols = row.select('td')
        
        # Ожидаем 5 колонок: Название, Бренд, Топливо, Цена, Обновлено
        if len(cols) < 5:
            continue
        
        station_name = cols[0].get_text(strip=True)
        brand = cols[1].get_text(strip=True)
        fuel_type = cols[2].get_text(strip=True)
        price = cols[3].get_text(strip=True)
        updated = cols[4].get_text(strip=True)
        
        entry = {
            'station': station_name,
            'brand': brand,
            'fuel_type': fuel_type,
            'price': price,
            'updated': updated
        }
        data.append(entry)

    # Вывод результатов
    if not data:
        print("Данные не найдены.")
        return

    print(f"Найдено записей: {len(data)}")
    
    # DEBUG: Print first row HTML to understand structure if headers are missing
    if rows:
        print("DEBUG: HTML первой строки:")
        print(rows[0].prettify())

    print("-" * 85)
    print(f"{'АЗС':<30} | {'Топливо':<10} | {'Цена':<10} | {'Обновлено':<15} | {'Бренд'}")
    print("-" * 85)
    
    for item in data:
        print(f"{item['station']:<30} | {item['fuel_type']:<10} | {item['price']:<10} | {item['updated']:<15} | {item['brand']}")


if __name__ == "__main__":
    get_fuel_prices()
