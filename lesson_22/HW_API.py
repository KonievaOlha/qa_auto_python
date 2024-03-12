# Завдання.
#
# Підключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ), отримайте курс валют і запишіть його в текстовий файл такому форматі (список):
# "[дата створення запиту]"
#
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
#
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
#
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
#
# ...
#
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
import datetime
import json

import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("fixture_random")
class TestApi:
    def test_1(self):
        self.URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        response = requests.request(method="GET", url=self.URL)
        content_json = response.json()
        write_text = ""
        current_date = datetime.datetime.now()
        query_date = f"===============Дата створення запиту===============\n"
        query_date += f"==============={str(current_date)}===============\n\n"
        with open("10.txt", "w", encoding="utf-8" ) as file:

            for i in range(len(content_json)):
                write_text += f"Назва валюти: {content_json[i]['txt']} to UAH: {content_json[i]['rate']}\n"
            file.write(query_date)
            file.write(write_text)
    #     for i in response:
    #         print(response[i].get('txt'))
    #         print(response[i].get('rate'))
    #         i += 1
    #
    # with open("1.txt", "w") as file:
    #     text = ""
    #     for i in range(9):
    #         text += str(i)
    #     file.write(text)

# def dec_write(add_numbers):
#     def write_def(num_1, num_2, num_3):
#         with open("log.txt", "a") as file:
#             file.write("\n")
#             file.write(f"var_1 = {num_1}, var_2 = {num_2}, var_3 = {num_3}")
#
#         result = add_numbers(num_1, num_2, num_3)
#         with open("log.txt", "a") as file:
#             file.write(f" result = {result}")
#
#         return result
#
#     return write_def
