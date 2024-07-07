from bs4 import BeautifulSoup
import requests
import json
import fake_useragent


url = 'https://biysk.hh.ru/search/vacancy?from=suggest_post&area=1217&hhtmFrom=main&hhtmFromLabel=vacancy_search_line&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&L_save_area=true&text=Системный+администратор' 

ua = fake_useragent.UserAgent()

headers = {
    "User-Agent": ua.random,
    'Accept': '*/*'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')
    # print(soup.text)
    
# Парсим вакансии Сис-админ город Бийск


vak = []
des = []
name_kompany = []
city_list = []

# Название вакансии
name_vakans = soup.find_all('span', class_='vacancy-name--c1Lay3KouCl7XasYakLk serp-item__title-link')
for i in name_vakans:
    res = {}
    res["Назваание проффесии"] = i.text
    vak.append(res)
# Зарплата и опыт работы 
vakans = soup.find_all('main', class_='vacancy-serp-content')
for desc in vakans:
    money = {}
    year = {}
    for descr in desc.find_all('span', class_='fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh'):
        des.append(descr.text)
        money["Платят денег"] = descr.text.replace('\u202f', ' ').replace('\xa0', ' ')
        des.append(money)
            
    for descr in desc.find_all('span', class_='label--rWRLMsbliNlu_OMkM_D3 label_light-gray--naceJW1Byb6XTGCkZtUM'):
        des.append(descr.text)
        year["Нужно лет опыта"] = descr.text
        des.append(year)   
# Название компаний
for city in vakans:
    for city_in_city in city.find_all('span', class_='company-info-text--vgvZouLtf8jwBmaD1xgp'):
        res_city = {}
        res_city['Компания'] = city_in_city.text
        name_kompany.append(res_city)
# Наваание города
c = soup.find_all('span', attrs={"data-qa": "vacancy-serp__vacancy-address"})
for f in c:
    town = {}
    f.find_next('span', class_='fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni')
    town['Город'] = f.text
    city_list.append(town)

list_main = [
    vak,
    des,
    name_kompany,
    city_list,
]

with open('hh.json', 'w') as f:
    json.dump(list_main, f, ensure_ascii=False, indent=4)    

        
                        