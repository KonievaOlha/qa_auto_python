from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


# : tuple
class RadioButton:
    _instance = None
    URL = "https://demoqa.com/buttons"


    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.button_doubleclick_loc = (By.ID, "#yesRadio")
        self.button_right_click_loc = (By.ID, "rightClickBtn")
        self.button_dynamic_id_loc = (By.XPATH, '//button[.="Click Me"]')
        self.button_doubleclick_message_loc = (By.ID, "doubleClickMessage")
        self.button_right_click_message_loc = (By.ID, "rightClickMessage")
        self.button_dynamic_id_click_message_loc = (By.ID, "dynamicClickMessage")







    # _instance = None
    # URL = "https://demoqa.com/radio-button"


    #
    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance
    #
    # def __init__(self, driver:WebDriver, locator: tuple, name: str):
    #     self.driver = driver
    #     self.locator = locator
    #     self.by, self.loc = self.locator
    #     if name:
    #         self.name: str = name
    #         self.loc = self.loc.format(self.name)
    #     # self.button_yes = (By.XPATH, "//label[.='{}']//ancestor::div[contains(@class, 'radio')]")
    #
    #     #     def __init__(self, driver:WebDriver):
    #     #         self.driver = driver
    #     #         self.button_doubleclick_loc = (By.ID, "doubleClickBtn")
    #     #         self.button_right_click_loc = (By.ID, "rightClickBtn")
    #     #         self.button_dynamic_id_loc = (By.XPATH, '//button[.="Click Me"]')
    #     #         self.button_doubleclick_message_loc = (By.ID, "doubleClickMessage")
    #     #         self.button_right_click_message_loc = (By.ID, "rightClickMessage")
    #     #         self.button_dynamic_id_click_message_loc = (By.ID, "dynamicClickMessage")
    # #
    # # def __init__(self, driver: WebDriver, locator: tuple, name: str):
    # #     self.driver = driver
    # #     self.locator = locator
    # #     self.by, self.loc = self.locator
    # #     if name:
    # #         self.name: str = name
    # #         self.loc = self.loc.format(self.name)
    #
    # def open(self):
    #     self.driver.get(self.URL)
    #     return self
    #
    # def select(self, name, locator):
    #     if self.name:
    #         self.driver.find_element(self.by, self.loc).click()
    #     else:
    #         self.driver.find_element(*self.locator).click()
    #


# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver
#
# from Hillel_october_23.lesson_24.widgets.components import Button
#
# class PageButtons:
#     _instance = None
#     URL = "https://demoqa.com/buttons"
#
#     # Singleton pattern
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#
#     def __init__(self, driver:WebDriver):
#         self.driver = driver
#         self.button_doubleclick_loc = (By.ID, "doubleClickBtn")
#         self.button_right_click_loc = (By.ID, "rightClickBtn")
#         self.button_dynamic_id_loc = (By.XPATH, '//button[.="Click Me"]')
#         self.button_doubleclick_message_loc = (By.ID, "doubleClickMessage")
#         self.button_right_click_message_loc = (By.ID, "rightClickMessage")
#         self.button_dynamic_id_click_message_loc = (By.ID, "dynamicClickMessage")
#
#
#     def open(self):
#         self.driver.get(self.URL)
#         return self
#
#     def button_doubleclick(self):
#         return Button(self.driver, self.button_doubleclick_loc)
#
#     def get_button_doubleclick_message(self) -> str:
#         return self.driver.find_element(*self.button_doubleclick_message_loc).text
#
#     def get_button_right_click_message(self) -> str:
#         return self.driver.find_element(*self.button_right_click_message_loc).text
#
#     def get_button_dynamic_id_click_message(self) -> str:
#         return self.driver.find_element(*self.button_dynamic_id_click_message_loc).text