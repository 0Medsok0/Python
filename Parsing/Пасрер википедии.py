import requests
from bs4 import BeautifulSoup

# URL страницы
url = "https://ru.wikipedia.org/wiki/Заглавная_страница"

# Получаем HTML-код страницы
response = requests.get(url)
response.encoding = 'utf-8'  # Устанавливаем кодировку

# Проверяем, что запрос успешен
if response.status_code == 200:
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим раздел "Хорошая статья"
    good_articles_section = soup.find('div', {'id': 'main-tga'})

    if good_articles_section:
        # Ищем все ссылки на хорошие статьи
        good_articles = good_articles_section.find_all('li')

        print("Хорошие статьи:")
        for article in good_articles:
            title = article.get_text()
            link = article.find('a')['href']
            print(f"- {title}: https://ru.wikipedia.org{link}")
    else:
        print("Раздел 'Хорошая статья' не найден.")
else:
    print(f"Ошибка при запросе страницы: {response.status_code}")