# перевірити поля "icon_url" чи він не пусти + чи це картинка,  - 2 теста
# перевірити чи є ключ "value"  і перевірити його значення - 2 теста
# Зробити окремий клас
# пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
# зробити класому фікстуру
# тест на статус код
# тест на кількість жартів
# тест на сам жарт
# + 3 тести

import pytest
import requests


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    def test_check_year(self):
        assert int(self.response.json()["created_at"][:4]) > 1990, "All our jokes were created until 1990"

    def test_status_code(self):
        assert self.status_code == 200

    def test_icon_url(self):
        assert len(self.response.json()["icon_url"]) > 0

    def test_icon_url_image(self):
        # assert ".png" in self.response.json()["icon_url"]
        assert str(self.response.json()["icon_url"][-3:]) == "png"

    def test_value(self):
        try:
            self.response.json()["value"]
        except KeyError:
            print("the Key value is missing ")

    def test_key_value(self):
        assert len(self.response.json()["value"]) > 10
        print(self.response.json()["value"])


def test_category():
    URL = "https://api.chucknorris.io/jokes/categories"
    response = requests.request(method="GET", url=URL)
    print(response.json())


@pytest.mark.parametrize("category",
                         requests.request(method="GET", url="https://api.chucknorris.io/jokes/categories").json())
def test_categories(category):
    URL = f"https://api.chucknorris.io/jokes/random?category={category}"
    response = requests.request(method="GET", url=URL)
    assert len(response.json()["id"]) == 22


@pytest.mark.usefixtures("fixture_joke")
class TestHomeWork:
    def test_word(self):
        self.URL = "https://api.chucknorris.io/jokes/search?query=please"
        response = requests.request(method="GET", url=self.URL)
        print(response.json())

    def test_status_code_2(self):
        assert self.status_code == 200
        # print(self.status_code == 200)

    def test_count_joke(self):
        value_string = str(self.response.json())
        assert value_string.count('value') == 25

    def test_joke(self):
        assert len(self.response.json()["result"][0]["value"]) > 10
        print(self.response.json()["result"][0]["value"])

    def test_created(self):
        assert int(self.response.json()["result"][1]["created_at"][:4]) > 2000

    def test_id(self):
        assert len(self.response.json()["result"][1]["id"]) > 10
        print(self.response.json()["result"][1]["id"])

    def test_count_joke_total(self):
        assert self.response.json()['total'] == 25
