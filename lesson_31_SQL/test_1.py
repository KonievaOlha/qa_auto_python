# import pprint
# import pytest
# import sqlite3
# #
# # connection = sqlite3.connect("C:\Works\Study_qa_auto\qa_auto_python\lesson_31_SQL\homework_base.db",
# #                              isolation_level=None)
# # cursor = connection.cursor()
#
# # cursor.execute("CREATE TABLE IF NOT EXISTS Phone(phone_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, model TEXT, price REAL, shop TEXT);")
# # cursor.execute("INSERT INTO Phone(name, model, price, shop) VALUES (('iphone'), (13), (2000), ('ALLO'));")
# # cursor.execute("INSERT INTO Phone(name, model, price, shop) VALUES (('xiaomi'), ('A50'), (200), ('ROZETKA'));")
# # cursor.execute("INSERT INTO Phone(name, model, price, shop) VALUES (('samsung'), ('A20'), (500), ('CITRUS'));")
# #
#
#
# # @pytest.mark.usefixtures("base_fixtures")
# class MobilePhone:
#
#     def __init__(self, name, model, price, breakage):
#         self.name = name
#         self.model = model
#         self.price = price
#         self.breakage = breakage
#
#     def __repr__(self):
#         return f"Phone_service(name={self.name}, item={self.model}, deal={self.price}, price={self.breakage})"
#
#     def get_phone_attributes(self):
#         return self.name, self.model, self.price, self.breakage
#
#
#
# # @pytest.mark.usefixtures("base_fixtures")
# class AbstractRepository:
#     def __init__(self, base111):
#         self._connection = sqlite3.connect(base111, isolation_level=None)
#         self._cursor = self._connection.cursor()
#
#     def __del__(self):
#         if self._cursor:
#             self._cursor.close()
#         if self._connection:
#             self._connection.close()
#         print("exit")
#
# # @pytest.mark.usefixtures("base_fixtures")
# class ReposMobPh(AbstractRepository):
#     def __init__(self, base111):
#         super(ReposMobPh, self).__init__(base111)
#         self._cursor.execute("CREATE TABLE IF NOT EXISTS Phone_service(phones_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, model TEXT, price REAL, breakage TEXT);")
#
#     def add_new_model(self, phone: MobilePhone):
#         self._cursor.execute("INSERT INTO Phone_service(name, model, price, breakage) VALUES ((?), (?), (?), (?));", phone.get_phone_attributes())
#
#
#
# #     def rowww(self):
# #         self.rows = cursor.fetchall()
# #         for row in self.rows:
# #             print(row)
# #
# #
#
# b = ReposMobPh("C:\Works\Study_qa_auto\qa_auto_python\lesson_31_SQL\homework_base.db")
#
# a = MobilePhone('gfhdg', 545, 454, 'fgdz')
# b.add_new_model(a)
#
# # vendor_repo = VendorsRepository('orders_new2.db')
# # print(vendor_repo.get_all_vendors())
# # vendor = Vendor('Anna', 'Train', 3, 343434.5)
# # vendor_repo.add_vendor(vendor)
# # print(vendor_repo.get_all_vendors())
#
#
#
# # def add_vendors(self, vendors):
# #     self._cursor.executemany("INSERT INTO Vendors(name, item, deal, price) VALUES ((?), (?), (?), (?));",
# #                              [vendor.get_vendor_attributes() for vendor in vendors])
# #
# # def get_all_vendors(self):
# #     data = self._cursor.execute('SELECT * from Vendors;')
# #     return self.rows2objects(data)
# #
# # def get_vendors_by_deal(self, deal):
# #     data = self._cursor.execute('SELECT * from Vendors WHERE deal=(?)', (deal,))
# #     return self.rows2objects(data)
# #
# # def row2object(self, row):
# #     return Vendor(*row[1:])
# #
# # def rows2objects(self, rows):
# #     return [self.row2object(row) for row in rows]
#
#
# # vendor_repo = VendorsRepository('orders_new2.db')
# # print(vendor_repo.get_all_vendors())
# # vendor = Vendor('Anna', 'Train', 3, 343434.5)
# # vendor_repo.add_vendor(vendor)
# # print(vendor_repo.get_all_vendors())
# #
# # vendors = [Vendor('John', 'Tram', 5, 34.5), Vendor('James', 'Avion', 2, 10900000)]
# # vendor_repo.add_vendors(vendors)
# # print(vendor_repo.get_all_vendors())
# # print(vendor_repo.get_vendors_by_deal(2))
#
