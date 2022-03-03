import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

# responseget = requests.get(url, params={'method': 'GET'})
# responsepost = requests.post(url, data={'method': 'POST'})
# responseput = requests.put(url, data={'method': 'PUT'})
# responsedel = requests.delete(url, data={'method': 'DELETE'})
# responsehead = requests.head(url, data={'method': 'HEAD'})

# print(responseget.text)
# print(responsepost.text)
# print(responseput.text)
# print(responsedel.text)
# print(responsehead.text)

# available_data = ['GET', 'POST', 'PUT', 'DELETE']
# available_methods = [requests.get, requests.post, requests.put, requests.delete]
#
# for i in available_methods:
#     for b in available_data:
#         name_function = str(i).split(" ")[1]
#         if name_function == 'get':
#             response = i(url, params={'method': b})
#             print("Method HTTP:", name_function.upper(), response.url, response.text)
#         else:
#             response = i(url, data={'method': b})
#             print("Method HTTP:", name_function.upper(), response.url, response.text)


available_data = ['ALEX', 'IVAN', 'SERGEY', 'ARTEM']
available_methods = [requests.get, requests.post, requests.put, requests.delete]

for i in available_methods:
    for b in available_data:
        name_function = str(i).split(" ")[1]
        if name_function == 'get':
            response = i(url, params={'name': b})
            print("Method HTTP:", name_function.upper(), response.url, response.text)
        else:
            response = i(url, data={'name': b})
            print("Method HTTP:", name_function.upper(), response.url, response.text)

# for i in available_data:
#     for b in available_methods:
#         response = b(url, params={'method': i})
#         name_function = str(b)
#         print(name_function.split(" ")[1], response.url, response.text)
