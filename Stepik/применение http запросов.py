import requests
import re

flag = True
url_a = input()
url_b = input()
try:
    res_a = requests.get(url_a)
    result_a = re.findall("href=\"(.*)\"", res_a.text)

    last_urls = list()
    for new_url in result_a:
        try:
            new_res = requests.get(new_url)
        except Exception:
            flag = False
        last_urls.extend(re.findall("href=\"(.*)\"", new_res.text))
except Exception:
    flag = False
if "//stepic." in url_b:
    url_b = url_b.replace("//stepic.", "//stepik.")
for i in range(len(last_urls)):
    if "//stepic." in last_urls[i]:
        last_urls[i] = last_urls[i].replace("//stepic.", "//stepik.")

if url_b in last_urls and flag:
    print("Yes")
else:
    print("No")
