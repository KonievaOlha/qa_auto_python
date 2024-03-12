import pytest
from qa_auto_python.lesson_31_SQL.base import ReposMobPh, MobilePhone


@pytest.mark.usefixtures("base_fixture")
class TestBaseHomeWork:
    def test_1(self):
        ReposMobPh("C:\Works\Study_qa_auto\qa_auto_python\lesson_31_SQL\homework_base.db")
        ReposMobPh.__init__()
        print('ok')

