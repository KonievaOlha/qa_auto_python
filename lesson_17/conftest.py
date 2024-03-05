import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="C:\Works\Study_qa_auto\qa_auto_python\lesson_17\chromedriver.exe")
    yield driver
    driver.quit()