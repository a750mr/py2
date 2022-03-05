import random

# We could use ASCII tables.
# lower = list("abcdefghijklmnopqrstuvwxyz")
# upper = list("abcdefghijklmnopqrstuvwxyz".upper())
# numbers = list("1234567890")
# symbols = list("!#$%&'()*+,-./:;<=>?@[]^_`{|}~")


def password(sym, len):
    password = "".join(random.sample(sym, len))
    print(password)


all2 = list(map(chr, range(33, 126)))


len_password = int(input("Введите количество символов: "))

password(all2, len_password)
