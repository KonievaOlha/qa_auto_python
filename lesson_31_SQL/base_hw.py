# import pprint
# import pytest
# import sqlite3
#
#
# @pytest.mark.usefixtures("base_fixture")
# class MobilePhone:
#
#     def __init__(self, name, model, price, shops):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.shops = shops
#
#     def connect_base(self, base):
#         self.base = base
#
#     def __repr__(self):
#         return f"Phone_22(name={self.name}, item={self.model}, deal={self.price}, price={self.shops})"
#
#     def get_phone_attributes(self):
#         return self.name, self.model, self.price, self.shops
#
#     def create_table(self):
#         self._cursor.execute("CREATE TABLE IF NOT EXISTS Phones_22(phones_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, model TEXT, price REAL, shops TEXT);", self.get_phone_attributes())
#
#     def add_new_model(self):
#         self._cursor.execute("INSERT INTO Phones_22(name, model, price, shops) VALUES (('?'), ('?'), (25), ('?'));", self.get_phone_attributes())
#
#
#
# # class AbstractRepository:
# #     def __init__(self, base111):
# #         self._connection = sqlite3.connect(base111, isolation_level=None)
# #         self._cursor = self._connection.cursor()
# #
# #     def __del__(self):
# #         if self._cursor:
# #             self._cursor.close()
# #         if self._connection:
# #             self._connection.close()
# #         print("exit")
#
#
# # class ReposMobPh(AbstractRepository):
# #     # def __init__(self, base111):
# #     #     super(ReposMobPh, self).__init__(base111)
# #     #     self._cursor.execute("CREATE TABLE IF NOT EXISTS Phones(phones_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, model TEXT, price REAL, shops TEXT);")
# #
# #     def add_new_model(self, phone: MobilePhone):
# #         self._cursor.execute("INSERT INTO Phones(name, model, price, shops) VALUES ((?), (?), (?), (?));", phone.get_phone_attributes())
# #
# #     def add_new_models(self, phones):
# #         self._cursor.executemany("INSERT INTO Phones(name, model, price, shops) VALUES ((?), (?), (?), (?));", [phones.get_phone_attributes() for phones in phones])
# #
# #     def get_all_phone_models(self):
# #         ph_mod = self._cursor.execute("SELECT * from Phone")
# #         return self.rows2objects(ph_mod)
# #
# #     def get_phones_by_breakage(self):
# #         breakage_name = self._cursor.execute('SELECT * from Phone WHERE name = (?)', (name, ))
# #         return self.rows2objects(breakage_name)
# #
# #     def row2object(self, row):
# #         return MobilePhone(*row[1:])
# #
# #     def rows2objects(self, rows):
# #         return [self.row2object(row) for row in rows]
# #
# #
# # Mobile_repos = ReposMobPh("C:\Works\Study_qa_auto\qa_auto_python\lesson_31_SQL\homework_base.db")
# # print(Mobile_repos.get_all_phone_models())
# # mobile = MobilePhone('first12', 10, 20, 'one')
# # # Mobile_repos.add_new_models(mobile)
# # phones = [MobilePhone('first12', 10, 20, 'one'), MobilePhone('second22', 30, 40, 'two'), MobilePhone('third32', 50, 60, 'three')]
# # Mobile_repos.add_new_models(phones)
# # print(Mobile_repos.get_all_phone_models())
# # print(Mobile_repos.get_all_phone_models())
# # # print(Mobile_repos.get_phones_by_breakage(2)) переписати
