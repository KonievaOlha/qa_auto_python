import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from qa_auto_python.lesson_24.test_hw.page_buttons import PageButtons


@pytest.mark.usefixtures("chrome_class")
class TestButtons:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageButtons(driver=self.driver)

    def test_doubleclick_button(self):
        self.page.open()
        self.page.button_doubleclick().doubleclick()
        assert self.page.get_button_doubleclick_message() == 'You have done a double click'

    def test_right_click_button(self):
        self.page.open()
        self.page.button_right_click().right_click()
        assert self.page.get_button_right_click_message() == 'You have done a right click'

    def test_dynamic_click_button(self):
        self.page.open()
        self.page.button_dynamic_click().click()
        assert self.page.get_button_dynamic_id_click_message() == 'You have done a dynamic click'
