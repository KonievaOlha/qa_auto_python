import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from qa_auto_python.lesson_28.test_hw.RadiobuttonPage import RadioButton


@pytest.mark.usefixtures("chrome_class")
class TestRadioButton:
    # def setup_method(self, driver, locator, name):
    #     self.driver: WebDriver = driver
    #     self.locator = locator
    #     self.name = name
    #     self.page = RadioButton(driver=self.driver, locator=self.locator, name=self.name)

    def test_radio(self, chrome_class):
        self.driver: WebDriver = chrome_class
        self.locator = (By.XPATH, "//label[.='{}']//ancestor::div[contains(@class, 'radio')]")
        self.name = "Impressive"
        self.open()
        self.ra_yes = RadioButton(driver=self.driver, locator=(By.XPATH, "//label[.='{}']//ancestor::div[contains(@class, 'radio')]"), name="Impressive")
        self.ra_yes.select(self.locator, self.name)

    # def test_activate_yes_radio(self):
    #     self.driver.get("https://demoqa.com/radio-button")
    #     self.ra_yes = RadioButton(driver=driver,
    #                               locator=(By.XPATH, "//label[.='{}']//ancestor::div[contains(@class, 'radio')]"),
    #                               name="Yes")
    #     self.ra_yes.select()
    #
    #
    # def test_get_radio_buttons_info(self):
    #     self.chrome.get("https://demoqa.com/radio-button")
