from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.get("https://market.yandex.ru/catalog--gazonokosilki/18033929/list?suggest_text=газонокосилка&hid=15646095&rs=eJwz4gxgrGLl6P-9i92pjEuai4ODUUBBgkuBS4BNijMlNS2xNKck3liBQYMBLsmowIgsaQiWtABLCkmwKLAICEgpJicWlybmxCcnFuWXFqfmxBelFhfk5xVnlqXGF6cmFiVnKLz7xqlxcnM7owCjF4e5sWVSUpK5UZCRobmRkaGJqYGBiaGBob5JmomBWXKqsZmpUaJRcpJBooFlqrEFUIGFYaqBmYGBvqG-IQCjTS8j&rt=9")
time.sleep(5)
name = driver.find_elements(By.CLASS_NAME, "m4M-1")
subs = driver.find_elements(By.CLASS_NAME, '_1PMpd')
price_1 = driver.find_elements(By.CLASS_NAME, "_1ArMm") # цена со скидкой
price_2 = driver.find_elements(By.CLASS_NAME, "_3gYEe") # цена без скидки

# метод page_source возвращает исходный код текущей страницы.
soup = BeautifulSoup(driver.page_source, 'html.parser')
list = []
for n in name:
    res_name = {n.text}
    list.append(res_name)
for s in subs:
    subs_name = {s.text}
    list.append(subs_name)
for pr_1 in price_1:
    pr_1_money = {pr_1.text}
    list.append(pr_1_money)
for pr_2 in price_2:
    pr_2_money = {pr_2.text}
    list.append(pr_2_money)

print(list)
driver.quit()
