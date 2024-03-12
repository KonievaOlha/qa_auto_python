from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Component:
    def __init__(self, driver: WebDriver = None, locator: tuple = None) -> None:
        if driver:
            self.driver: WebDriver = driver
            if locator:
                self.locator = locator
                self.element: WebElement = self.driver.find_element(*self.locator)
        self._actions = ActionChains(driver=driver)

    def type_of(self) -> str:
        """визначаємо який тип віджета в нас є"""
        return self.__class__.__name__

    def scroll_to(self) -> None:
        """проскролюємо до елемента 1-й випадок. якщо він наприклад внизу сторінки,
        то скролить вверх і коли бачить елемент зупиняється"""
        self._actions.scroll_to_element(self.element)

    def scroll_into_view(self) -> None:
        """проскролюємо до елемента за допомогою джаваскріпт коду на сторінці.
        Скролить з запасом і дає нам більшу імовірність що ми достукаємось до елементу якщо він перекритий"""
        self.driver.execute_script("arguments[0].scrollIntoView();", self.element)


class Button(Component):
    def __init__(self, driver: WebDriver = None, locator: tuple = None):
        super().__init__(driver=driver, locator=locator)

    def hover(self):
        self._actions.move_to_element(self.element).perform()

    def click(self):
        self.element.click()

    def doubleclick(self):
        self._actions.double_click(self.element).perform()

    def right_click(self):
        self._actions.context_click(self.element).perform()

    def get_attribute(self, attr):
        return self.element.get_attribute(attr)
