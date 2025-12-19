import requests
import json


def picture():
    for i in range(1, 4):
        headers = {
            'sec-ch-ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
            'Referer': f'https://ru.freepik.com/search?ai=excluded&format=search&last_filter=page&last_value=2&page=2&query=%D1%84%D1%80%D1%83%D0%BA%D1%82&type=photo',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.get(
            f'https://ru.freepik.com/api/regular/search?filters[ai-generated][excluded]=1&filters[content_type]=photo&locale=ru&page={i}&term=%D1%84%D1%80%D1%83%D0%BA%D1%82',
            headers=headers,
        ).json()

        # print(response)


# Достаем ссылку на картнку, название картинки, id -- картинки

        products = []
        for pixel in response['items']:
            products.append({
                "Название": pixel['name'],
                "Ссылка": pixel['url'],
                "ID": pixel['id']
                })

        with open("pixel.json", "w", encoding="utf-8") as file:
            json.dump(products, file, indent=4, ensure_ascii=False)

picture()

