from selenium import webdriver

''' тестирование selenium webdriver
url = "https://stepik.org/"
browser = webdriver.Chrome()
browser.get(url)
'''
''' открытие браузера с расширениями
options_chrome = webdriver.ChromeOptions()
options_chrome.add_extension("coordinates.crx")
with webdriver.Chrome(options=options_chrome) as browser:
    url = "https://yandex.ru/"
    browser.get(url)
'''
