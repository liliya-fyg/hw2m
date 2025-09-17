# from my_pachege.module_1 import add, test
#
# print(add(23, 32))
# print(test)

# print("Some text")

import requests

response = requests.get("https://api.github.com")

if response.status_code == 200:
    print("Успешный запрос!")
    print(response.json())
else:
    print("Ошибка:", response.status_code)