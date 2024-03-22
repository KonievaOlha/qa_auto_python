# import pytest
# from qa_auto_python.lesson_28.test_hw.CheckboxPage import CheckboxPage
# from qa_auto_python.lesson_28.widgets.components import CheckBox, ExpandableTreeElement
# from selenium.webdriver.remote.webdriver import WebDriver
#
#
# @pytest.mark.usefixtures("chrome_class")
# class TestCheckboxPage:
#     def setup_method(self):
#         self.driver: WebDriver = self.driver
#         self.page = CheckboxPage(self.driver)
#
#     def test_page(self):
#         self.page.open()
#         self.CheckBox.is_selected("home")
#         return self.page.("home")
#         # self.page.collapse_folder("desktop")
#         # self.page.mark_folder("commands")
#         # self.page.collapse_folder("documents")
#         # self.page.collapse_folder("workspace")
#         # self.page.collapse_folder("office")
#         # self.page.mark_folder("general")
#         # audit_text = self.page.result_selected()
#         # assert audit_text.replace("You have selected :", "") == "\ncommands\ngeneral"
