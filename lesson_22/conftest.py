import pytest
import requests
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def firefox(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.implicitly_wait(5)  # імплісіті вейт це вся реалізація
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def fixture_random(request):
    response = requests.request(method="GET", url="https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    name_txt = response.json()[2]
    rate = response.json()[3]
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
    yield response, status_code, name_txt, rate


@pytest.fixture()
def fixture_joke(request):
    response = requests.request(method="GET", url="https://api.chucknorris.io/jokes/search?query=Please")
    status_code = response.status_code
    request.cls.response = response
    request.cls.status_code = status_code
    yield response, status_code,
