import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
