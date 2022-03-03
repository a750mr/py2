import json

import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url)

response2 = requests.get(url,params={"token": "gNwozMwozMxAyMw0yMw0iMyAjM"}).text

json_in = json.loads(response2)

json_status = json_in["status"]

print(response2)

