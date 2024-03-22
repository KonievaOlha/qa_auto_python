import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

URL = "https://demoqa.com/checkbox"
# 1)
#
# Написати тест test_checkboxes: на сторінці https://demoqa.com/checkbox
# обрати (поставити галочку) 2 елемента: Commands (Home-Desktop) та
# General (Home-Documents-Office). Обирати елементи потрібно однією функцією, по імені елеемнта.


class CheckboxPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(URL)
        return self

    def expand_folder(self, name) -> None:
        versatile_checkbox_button = self.driver.find_element(By.XPATH,
                                                             f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        try:
            expand = versatile_checkbox_button.find_element(By.XPATH, "//*[contains(@class, 'expand-open')]")
            if expand.is_displayed():
                expand.click()
        except NoSuchElementException:
            pass
        # try:
        #     expand = versatile_checkbox_button.find_element(By.XPATH, "//*[contains(@class, 'expand-close')]")
        #     if expand.find_element():
        #         expand.click()
        # except NoSuchElementException:
        #     pass
        versatile_checkbox_button.click()

    def collapse_folder(self, name) -> None:
        versatile_checkbox_button = self.driver.find_element(By.XPATH,
                                                             f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        try:
            expand = versatile_checkbox_button.find_element(By.XPATH, "//*[contains(@class, 'expand-close')]")
            if expand.is_displayed():
                expand.click()
        except NoSuchElementException:
            pass
        # versatile_checkbox_button.click()


    def mark_folder(self, name):
        versatile_checkbox_button = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]")
        input_field = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]/input")
        if not input_field.is_selected():
            versatile_checkbox_button.click()


    def unmark_folder(self, name):
        versatile_checkbox_button = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]")
        # input_field = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]/input")
        versatile_checkbox_button.click()


    def result_selected(self):
        result_selected_1 = (By.XPATH, "//div[@class='display-result mt-4']")
        return self.driver.find_element(*result_selected_1).text

        # assert name_field.replace("Name:", "") == "Olya"




        # //*[contains(@class, "expand-open")] - відкрито
        # //*[@class="rct-icon rct-icon-expand-close"]