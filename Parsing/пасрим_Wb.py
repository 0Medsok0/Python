import requests
import json

def min_max():
    for i in range(1, 3):

        price_min = 200
        price_max = 1000

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://www.wildberries.ru',
            'Referer': f'https://www.wildberries.ru/catalog/detyam/shkola/shkolnye-prinadlezhnosti/bumazhnaya-produktsiya?sort=popular&page={i}&xsubject=745',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'ab_testing': 'false',
            'appType': '1',
            'cat': '130054',
            'curr': 'rub',
            'dest': '-1255987',
            'page': '1',
            'sort': 'popular',
            'spp': '30',
            'xsubject': '745',
        }

        response = requests.get('https://catalog.wb.ru/catalog/school5/v2/catalog',
                                params=params,
                                headers=headers).json()
        # print(response)

        # float("inf"): Это значение, присвоенное ключу "price". Вот что это означает:
        # float: Это означает, что значение является числом с плавающей запятой, используемым для представления десятичных чисел.
        # "inf": Эта специальная строка в функции float() представляет положительную бесконечность.
        # Почему значение float("inf")?
        # Цель кода - найти самый дешевый продукт из списка.
        # При инициализации значения "цена" cheapest_product равным бесконечности,
        # логика гарантирует, что любая фактическая цена из данных о продукте будет ниже бесконечности.
        # Таким образом, первый попавшийся товар автоматически становится "самым дешевым"
        # до тех пор, пока не будет найден товар по более низкой цене.
        products = []
        cheapest_product = {"price": float("inf")}
        most_expensive_product = {"price": 0}
        for product in response['data']['products']:

            price = product['sizes'][0]['price']['basic'] // 100
            if price < cheapest_product["price"]:
                cheapest_product = {
                    "Название": product['name'],
                    "Описание": product['colors'],  # product['imt']['text'][0]
                    "ID": product['id'],
                    "Цена": str(product['sizes'][0]['price']['basic'] // 100) + " " + str(
                        product['sizes'][0]['price']['total'] // 100),
                    "price": price
                }
            if price > most_expensive_product["price"]:
                most_expensive_product = {
                    "Название": product['name'],
                    "Описание": product['colors'],  # product['imt']['text'][0]
                    "ID": product['id'],
                    "Цена": str(product['sizes'][0]['price']['basic'] // 100) + " " + str(
                        product['sizes'][0]['price']['total'] // 100),
                    "price": price
                }
        products.append(cheapest_product)
        products.append(most_expensive_product)
        with open("all_products.json", "w", encoding="utf-8") as file:
            json.dump(products, file, indent=4, ensure_ascii=False)

def all_results():
    for i in range(1, 3):

        price_min = 200
        price_max = 1000

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://www.wildberries.ru',
            'Referer': f'https://www.wildberries.ru/catalog/detyam/shkola/shkolnye-prinadlezhnosti/bumazhnaya-produktsiya?sort=popular&page={i}&xsubject=745',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'ab_testing': 'false',
            'appType': '1',
            'cat': '130054',
            'curr': 'rub',
            'dest': '-1255987',
            'page': '1',
            'sort': 'popular',
            'spp': '30',
            'xsubject': '745',
        }

        response = requests.get('https://catalog.wb.ru/catalog/school5/v2/catalog',
                                params=params,
                                headers=headers).json()
        # print(response)


        # Достаем имя товара,описание товара,достаем id,
        # цену товара(со скидкой и без скидки)

        products = []
        for product in response['data']['products']:
            products.append({
                "Название": product['name'],
                "Описание": product['colors'],
                "ID": product['id'],
                "Цена без скидки": str(product['sizes'][0]['price']['basic'] // 100),
                "Цена со скидкой": str(product['sizes'][0]['price']['total'] // 100)
            })
        with open("min_max.json", "w", encoding="utf-8") as file:
            json.dump(products, file, indent=4, ensure_ascii=False)

def main():
    print('1--Получить дорогой товар/дешевый товар')
    print('2--Получить все товары')

    count = int(input("Введите число для получениия резултата: "))
    if count == 1:
        min_max()
    if count == 2:
        all_results()

if __name__ == "__main__":
    main()

