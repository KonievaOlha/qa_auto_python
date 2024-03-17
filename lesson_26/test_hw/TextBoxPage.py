from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.url = "https://rozetka.com.ua/ua/"
        self.driver = driver
        self.find_rozetka_1 = (By.XPATH, "//*[@name='search']")
        self.find_rozetka_css_2 = (By.CSS_SELECTOR, "input[name='search']")
        self.button_search_3 = (
        By.XPATH, "//button[@class='button button_color_green button_size_medium search-form__submit']")
        self.menu_button_css_4 = (By.CSS_SELECTOR, "button[aria-label='Відкрити меню']")
        self.menu_button_5 = (By.XPATH, "//button[@id='fat-menu']")
        self.menu_fat_css_6 = (By.CSS_SELECTOR, "button#fat-menu")
        self.button_basket_7 = (By.XPATH, "//rz-cart[.//button[@class='header__button']]")
        self.button_basket_css_8 = (By.CSS_SELECTOR, "button.header__button[_ngcontent-rz-client-c1870466485]")
        self.chat_rozetka_9 = (
        By.CSS_SELECTOR, "a.button.button--medium.button--with-icon.main-links__help.link--green")
        self.icon_rozetka_10 = (By.XPATH, "//picture[@class='ng-star-inserted']")

    def open(self) -> "TextBoxPage":
        self.driver.get(self.url)
        return self

    def name_field_1(self) -> None:
        self.driver.find_element(*self.find_rozetka_1).click()

    def name_field_2(self) -> None:
        self.driver.find_element(*self.find_rozetka_css_2).click()

    def name_field_3(self) -> None:
        self.driver.find_element(*self.button_search_3).click()

    def name_field_4(self) -> None:
        self.driver.find_element(*self.menu_button_css_4).click()

    def name_field_5(self) -> None:
        self.driver.find_element(*self.menu_button_5).click()

    def name_field_6(self) -> None:
        self.driver.find_element(*self.menu_fat_css_6).click()

    def name_field_7(self) -> None:
        self.driver.find_element(*self.button_basket_7).click()

    def name_field_8(self) -> None:
        self.driver.find_element(*self.button_basket_css_8).click()

    def name_field_9(self) -> None:
        self.driver.find_element(*self.chat_rozetka_9).click()

    def name_field_10(self) -> None:
        self.driver.find_element(*self.icon_rozetka_10).click()
