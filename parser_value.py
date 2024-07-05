from bs4 import BeautifulSoup
import requests
import json
import fake_useragent

url = 'https://www.banki.ru/products/currency/' # valuti_str_one 

ua = fake_useragent.UserAgent()

headers = {
    "User-Agent": ua.random,
    'Accept': '*/*'
}

res = requests.get(url, headers=headers)

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')
    # print(soup.text)
    
    
def value():

    list = []
    title = soup.find_all('div', class_='FlexboxGrid__sc-akw86o-0 gXguwc')
    for i in title:
        name = i.find('div', class_='Text__sc-j452t5-0 gfTHqP').text.strip() 
        des = i.find('div', class_='Text__sc-j452t5-0 dJGHYE').text.strip()
    
        for item in soup.find_all('div', class_='FlexboxGrid__sc-akw86o-0 dELgzc'):
            buy = item.find('div', class_='Text__sc-j452t5-0 gJcAhr').get_text()
            sell = item.find('div', class_='Text__sc-j452t5-0 jzaqdw').get_text()
            
            data = {
                'Название': name,
                'Описание': des,
                'Покупка': buy,
                'Продажа': sell
            }
            list.append(data)
        
         
    with open("value.json", "w") as file:
        json.dump(list, file, indent=4, ensure_ascii=False)
        
value()
