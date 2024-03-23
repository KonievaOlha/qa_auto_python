import pytest
from qa_auto_python.lesson_28.test_hw.CheckboxPage import CheckboxPage


@pytest.mark.usefixtures("chrome_class")
class TestCheckboxPage:
    def setup_method(self):
        self.page = CheckboxPage(self.driver)

    def test_page(self):
        self.page.open()
        self.page.collapse_folder("home")
        self.page.collapse_folder("desktop")
        self.page.mark_folder("commands")
        self.page.collapse_folder("documents")
        self.page.collapse_folder("workspace")
        self.page.scroll_down()
        self.page.collapse_folder("office")
        self.page.mark_folder("general")
        audit_text = self.page.result_selected()
        assert audit_text.replace("You have selected :", "") == "\ncommands\ngeneral"
