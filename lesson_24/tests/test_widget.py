from qa_auto_python.lesson_23.widgets.components import ExpandableTreeElement, Button


class TestWidgets:
    def test_1(self):
        x = ExpandableTreeElement()
        y = Button()
        # y.
        assert x.type_of() == "ExpandableTreeElement"
        assert y.type_of() == "Button"