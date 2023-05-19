import requests
import bs4

url = "https://www.amazon.com/s?k=python&i=stripbooks-intl-ship&ref=nb_sb_noss"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'DNT': '1'}
responce = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(responce.text)
print(soup.find_all("div"))