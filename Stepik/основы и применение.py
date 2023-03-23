import requests
import re

first = input()
second = input()
res = requests.get(first)
urls = list()
result_first = re.findall("href=\"(.*)\"", res.text)
for new_url in result_first:
    responce = requests.get(new_url)
    urls.extend(re.findall("href=\"(.*)\"", responce.text))
if second in urls or second.replace("stepik", "stepic") in urls:
    print("Yes")
else:
    print("No")
