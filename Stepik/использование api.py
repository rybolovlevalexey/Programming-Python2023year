import requests
import sys

url = "http://numbersapi.com/"  # + number/type
for num in sys.stdin:
    num = num.strip()
    if num.isalnum():
        res = requests.get(url + num + "/math?json")
        data = res.json()
        if data["found"]:
            print("Interesting")
        else:
            print("Boring")
