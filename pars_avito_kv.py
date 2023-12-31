from bs4 import BeautifulSoup
import json
import re
import soupsieve as sv




with open('html/Авито.html', 'r') as f: # открываем файл 
  soup = BeautifulSoup(f, 'lxml')
  
#print(soup)


#!! Достаем цену квартиры
data_1 = {}
spans_in_strong = soup.find_all('strong', class_='styles-module-root-LIAav')
for i in range(len(spans_in_strong)):
  next_tag = spans_in_strong[i].next_element
  if next_tag:
    data_1[spans_in_strong[i].get_text()] = f'{"href"}:{"https://www.avito.ru/biysk/kvartiry/"}'                         
  else:
    data_1[spans_in_strong[i].get_text()] = "No next sibling found"

  
# Достаем цену квартиры за метр.кв

data_2 = {}
for tg_1 in soup.find_all(re.compile("span"), class_='price-root-RA1pj'):
    for tg_2 in tg_1(re.compile('p'), class_='styles-module-root-_KFFt styles-module-size_s-awPvv styles-module-size_s-_P6ZA stylesMarningNormal-module-root-OSCNq stylesMarningNormal-module-paragraph-s-_c6vD styles-module-noAccent-nZxz7'):
        data_2[tg_2.get_text()] = f'{"href"}:{"https://www.avito.ru/biysk/kvartiry/"}'
         
# Достаем маленькое описание с геолокацией

data_3 = {}
for tg_3 in soup.find_all(re.compile("div"), class_='geo-root-zPwRk'):
    data_3[tg_3.get_text()] = 'geolocation'

# Достаем большое описание

data_4 = {}
for tg_4 in soup.find_all(re.compile("div"), class_='iva-item-descriptionStep-C0ty1'):
    data_4[tg_4.get_text()] = 'description'

# Достаем ссылки на квартиры и их описание
data_5 = {} 
links = soup.select_one('div', class_='photo-slider-root-Exoie photo-slider-redesign-q6DEc').select('a')
# print(links)
for link in links:
    i_text = link.text
    item_url = link.get("href")
    data_5[(f"{i_text}")] = f"{item_url}"
    
# all_a = soup.find_all("a")
# print(all_a)
#
# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")
    
    


with open("data.json", "w") as file:
    json.dump((data_1,data_2,data_3,data_4,data_5), file, indent=4, ensure_ascii=False)
