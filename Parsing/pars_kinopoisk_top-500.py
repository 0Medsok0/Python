import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import os



driver = webdriver.Firefox()

for i in range(1, 11):
    driver.get(f"https://www.kinopoisk.ru/lists/movies/top500/?page={i}")
    time.sleep(5)
    # name = driver.find_elements(By.CLASS_NAME, "styles_root__ti07r") # полная обложка
    link = driver.find_elements(By.CLASS_NAME, "base-movie-main-info_link__YwtP1") # сслыка
    name_philm = driver.find_elements(By.CLASS_NAME, "styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj") # название фильма
    descrip_1 = driver.find_elements(By.CLASS_NAME, "desktop-list-main-info_secondaryTitleSlot__mc0mI")
    descrip_2 = driver.find_elements(By.CLASS_NAME, "desktop-list-main-info_additionalInfo__Hqzof")
    descrip_3 = driver.find_elements(By.CLASS_NAME, "desktop-list-main-info_additionalInfo__Hqzof")
    reiting_kinopoisk = driver.find_elements(By.CLASS_NAME, 'styles_srRoot__WgbFG')
    number_of_ratings = driver.find_elements(By.CLASS_NAME, 'styles_kinopoiskCount__PT7ZX')

    # get_attribute или text
    # метод page_source возвращает исходный код текущей страницы.
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    page_data = []
    for n in link:
        res = [n.text.replace('\n', ' ')]
        page_data.append(res)


    # Получаем 10 файлов json, каждый файл это страница
    with open(f"page_{i}.json", "w", encoding="utf-8") as f:
        json.dump(page_data, f, ensure_ascii=False, indent=4)


driver.quit()
