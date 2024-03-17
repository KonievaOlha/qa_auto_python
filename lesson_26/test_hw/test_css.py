import pytest
from qa_auto_python.lesson_26.test_hw.TextBoxPage import TextBoxPage


@pytest.mark.usefixtures("chrome_class")
class TestTextBox:

    def test_1(self, chrome_class):
        page = TextBoxPage(chrome_class)
        page.open()
        page.name_field_1()

    def test_2(self, chrome_class):
        page = TextBoxPage(chrome_class)
        page.open()
        page.name_field_2()
        print("3")

    def test_3(self, chrome_class):
        page = TextBoxPage(chrome_class)
        page.open()
        page.name_field_3()
        print("3")

    def test_4(self, chrome_class):
        page = TextBoxPage(chrome_class)
        page.open()
        page.name_field_4()
        print("4")

    def test_5(self, chrome_class):
        page = TextBoxPage(chrome_class)
        page.open()
        page.name_field_5()
        print("5")

    def test_6(self, chrome_class):
        page = TextBoxPage(chrome_class)
        page.open()
        page.name_field_6()
        print("6")

    def test_7(self, chrome_class):
        page = TextBoxPage(chrome_class)
        page.open()
        page.name_field_7()
        print("7")

    def test_8(self, chrome_class):
        page = TextBoxPage(chrome_class)
        page.open()
        page.name_field_8()
        print("8")

    def test_9(self, chrome_class):
        page = TextBoxPage(chrome_class)
        page.open()
        page.name_field_9()
        print("9")

    def test_10(self, chrome_class):
        page = TextBoxPage(chrome_class)
        page.open()
        page.name_field_10()
        print("10")
