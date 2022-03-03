import requests

url = 'https://playground.learnqa.ru/api/long_redirect'

response_url = requests.get(url)
response_last = response_url.history[-1].url

abc = 1

for i in response_url.history:
    print(f'{abc} redirect. Status code: {i}, and url {i.url}')
    abc += 1
print(f'Last url: {response_last}')

