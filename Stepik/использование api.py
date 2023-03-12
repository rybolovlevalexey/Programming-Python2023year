import requests
import sys
import json

CLIENT_ID = "d5fcb8afca74d9ad16db"
CLIENT_SECRET = "f4734718a6740f303482dbb4b4172085"
XAPP_TOKEN = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                           data={"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET})
token = json.loads(XAPP_TOKEN.text)["token"]
HEADERS = {"X-Xapp-Token": token}

url = "https://api.artsy.net/api/artists/"
answer = dict()
for identif in sys.stdin:
    identif = identif.strip()
    if identif != " " or identif != "":
        res = requests.get(url + identif, headers=HEADERS)
        data = res.json()
        # sortable_name, birthday
        if "total_count" in data:
            continue
        name = data["sortable_name"]
        bday = data["birthday"]
        if bday not in answer:
            answer[bday] = list()
        answer[bday].append(name)

for key in sorted(answer.keys()):
    for name in sorted(answer[key]):
        print(name)
