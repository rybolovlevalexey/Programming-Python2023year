import bs4
import requests
import json
import html5lib
import lxml

# URL = "какая-то ссылка"
# response = requests.get(URL)
# soup = bs4.BeautifulSoup(response.text, "lxml")
# result = soup.find("div", class_="item").find_all("li")
# получение всех тегов li в блоке div класса item, так же можно искать и по id=''
# поиск по атрибутам передаётся в словаре после названия тега
# soup.find("span", {"name": "count"}).text  атрибут name со значением count
# for inf in result: в переменной inf тег лежит целиком
#     data = inf.text получение только текста внутри тега
# метод .text можно применить к результату .find() но не .find_all()
