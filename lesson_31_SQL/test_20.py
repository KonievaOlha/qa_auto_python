# import pytest
# import sqlite3
#
#
# @pytest.fixture(scope="class")
# def qqq_fixture():
#     print("setup")
#     connection = sqlite3.connect("C:\Works\Study_qa_auto\qa_auto_python\lesson_31_SQL\homework_base.db",
#                                  isolation_level=None)
#     cursor = connection.cursor()
#     yield cursor, connection
#     print("teardown")
#     cursor.close()
#     connection.close()
#
#
#
# class Test_12345():
#     def __init__(self,a):
#         self.a = a
#
#     def create_command(self):
#         print(self.a)
#         connection = sqlite3.connect("C:\Works\Study_qa_auto\qa_auto_python\lesson_31_SQL\homework_base.db",
#                                      isolation_level=None)
#         cursor = connection.cursor()
#
#     def test1(self):
#         self.create_command()
#         assert True == True
#
#     def test2(self):
#         self.create_command()
#         assert True == True
#
#     def test3(self):
#         self.create_command()
#         assert True == True
#
#
# c = Test_12345(1)
# c.create_command()