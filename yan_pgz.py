from bs4 import BeautifulSoup
import json

with open('html/ypz.html', 'r') as f: # открываем файл 
  soup = BeautifulSoup(f, 'lxml')
  
# погода на завтра
weather_tomorrow = soup.find('article', class_="sc-b9164f35-1 ljXkQi")
next_day =  weather_tomorrow.next_sibling
print(next_day.text)    


# температура на сегодня
temperature = soup.find_all('div', class_="sc-ea88bf5a-0 fZDzgU")
result_1 = {}
for i in range(len(temperature)): # слева цифры справа текст
    result_1[i] = temperature[i].text
  
# как она ощущается
feels_like_temperature = soup.find_all('div', class_="sc-ea88bf5a-0 feEFDT")    
result_2 = {}
for i in range(len(feels_like_temperature)): # слева цифры справа текст
    result_2[i] = feels_like_temperature[i].text

# время восхода и заката
sunrise_and_sunset_times = soup.find_all('div', class_='sc-d3866985-3 iijxEx')
result_3 = {}
for i in range(len(sunrise_and_sunset_times)): # слева цифры справа текст
    result_3[i] = sunrise_and_sunset_times[i].text
    
with open("weather.json", "w") as file:
    json.dump((result_1,result_2,result_3), file, indent=4, ensure_ascii=False)
