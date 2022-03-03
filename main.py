import requests

query = {"name": "Alex"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=query)
print(response.text)
