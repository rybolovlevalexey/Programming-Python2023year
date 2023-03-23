import requests
import lxml
import bs4
import re

url = input()
res = requests.get(url)
res.encoding = "utf-8"
links = list(elem.get("href")
           for elem in bs4.BeautifulSoup(res.text, "lxml").find_all("a"))
links = filter(lambda x: x is not None, links)
ans = set()
for line in links:
    if "://" not in line:
        continue
    result = line[line.index("://") + 3:]
    while "/" in result or ":" in result:
        result = result[:-1]
    ans.add(result.strip())
print(*sorted(ans), sep="\n")
