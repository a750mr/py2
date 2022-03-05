import requests

url = "https://playground.learnqa.ru/api/hello"
name = "alex"
data = {"name": name}
response = requests.get(url, params=data)

print(response.text)