# Находим HTML теги, в которых находится информация по товарам (Название книги, цена).
# Вывести полное наименование книги (из тега a атрибута title)
# Выводим результат в DataFarme

import pandas as pd
from bs4 import BeautifulSoup
import requests

# Create an URL object
url = 'http://books.toscrape.com/catalogue/page-1.html'

# Create object page
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# Find HTML tags containing information about products
tags = soup.find_all('article', class_='product_pod')

# Create lists to store the book titles and prices
titles = []
prices = []

# Extract the titles and prices from the tags
for tag in tags:
    title = tag.find('h3').find('a')['title']
    price = tag.find('p', class_='price_color').text[2:]
    titles.append(title)
    prices.append(price)

# Create a DataFrame from the extracted data
df = pd.DataFrame({'Title': titles, 'Price': prices})

# Print the DataFrame
print(df)
