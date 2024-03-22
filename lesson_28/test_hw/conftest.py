import pytest
import requests
from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()
