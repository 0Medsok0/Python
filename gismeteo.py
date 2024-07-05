from bs4 import BeautifulSoup
import requests
import json
import fake_useragent


url = 'https://www.gismeteo.ru/' 

ua = fake_useragent.UserAgent()

headers = {
    "User-Agent": ua.random,
    'Accept': '*/*'
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'lxml')
    
# Название города
list = []
city = soup.find_all('div', class_='city')
for i in city:
    city_name = i.find('a', class_='city-link link')
    res_head = {}    
    list.append(res_head)

# Основная информация о погоде
main = soup.find_all('div', class_='frame-now') 
for j in main:
    city_time = j.find('div', class_='current-time').text.strip()
    temperature = j.find('div', class_='weather-info-header').text.strip()
    it_feels_like = j.find('div', class_='weather-item weather-feeling').text.strip()
    wind = j.find('div', class_='weather-item weather-wind').text.strip()
    pressure = j.find('div', class_='weather-item weather-pressure').text.strip()
    humidity = j.find('div', class_='weather-item weather-humidity').text.strip()
    gm_activity = j.find('div', class_='weather-item weather-geomagnetic').text.strip()
    water = j.find('div', class_='weather-item weather-water').text.strip()
    
    res_main = {
    'city_time': city_time,
    'temperature': temperature,
    'it_feels_like': it_feels_like,
    'wind': wind,
    'pressure': pressure,
    'humidity': humidity,
    'gm_activity': gm_activity,
    'water': water
    }

    list.append(res_main)
    
fot = soup.find_all('div', class_='frame-forecast') 
for y in fot:
    times = y.find('div', class_='widget-row widget-row-time').text
    for z in y.find_all('span', class_='unit unit_temperature_c'):
        temp = z.text
        wind = y.find('span', class_='wind-unit unit unit_wind_m_s').text
        
        res_fot = {
            'times': times,
            'temp': temp,
            'wind_m/s': wind
        }
        list.append(res_fot)
        print(res_fot)