"""
Write a wrapper class TableData for database table, that when initialized with database
name and table acts as collection object (implements Collection protocol).
Assume all data has unique values in 'name' column.
So, if presidents = TableData(database_name='example.sqlite', table_name='presidents'), then:
    - len(presidents) will give current amount of rows in presidents table in database
    - presidents['Yeltsin'] should return single data row for president with name Yeltsin
    - 'Yeltsin' in presidents should return if president with same name exists in table
    - object implements iteration protocol. i.e. you could use it in for loops:
        for president in presidents:
            print(president['name'])

All above mentioned calls should reflect most recent data.
If data in table changed after you created collection instance, your calls should return updated data.

Avoid reading entire table into memory. When iterating through records, start reading the first record,
then go to the next one, until records are exhausted.
When writing tests, it's not always neccessary to mock database calls completely.
Use supplied example.sqlite file as database fixture file.
"""
import os
import sqlite3
from datetime import time
from time import sleep


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = os.path.join(os.path.dirname(__file__), database_name)
        self.table_name = table_name
        self._index = -1
        self.cursor = None

    def get_cursor(self):
        with sqlite3.connect(f"{self.database_name}") as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            return cursor

    def __len__(self):
        cursor = self.get_cursor()
        cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        amount_of_rows = cursor.fetchone()[0]
        return amount_of_rows

    def __getitem__(self, item):
        cursor = self.get_cursor()
        cursor.execute(f"SELECT * from {self.table_name} where name=?", (item,))
        row_item = tuple(cursor.fetchone())
        return row_item

    def __contains__(self, item):
        cursor = self.get_cursor()
        cursor.execute(f"SELECT * from {self.table_name} where name=?", (item,))
        row = cursor.fetchone()
        return bool(row)

    def __iter__(self):
        cursor = self.get_cursor()
        cursor.execute(f"SELECT * from {self.table_name}")
        # data = cursor.fetchone()
        return (cursor.fetchone() for _ in range(self.__len__()))

    # def __next__(self):
    #     cursor = self.get_cursor()
    #     cursor.execute(f'SELECT * from {self.table_name}')
    #     data = cursor.fetchone()
    #     amount_of_rows = self.__len__()
    #     self._index += 1
    #     if self._index >= amount_of_rows:
    #         self._index -= 1
    #         raise StopIteration
    #     else:
    #         return data

    # cursor.execute(f'SELECT * from {table_name}')
    # data = cursor.fetchall()
    # print(data)
    # print(cursor.fetchone())
    # row = cursor.fetchone()
    # while row:
    #     print(row)
    #     pass

    # row = cursor.fetchone()


presidents = TableData(database_name="example.sqlite", table_name="presidents")
print(len(presidents))
print(presidents["Trump"])
print("Trump" in presidents)
for president in presidents:
    print(president["age"])

# database_name = os.path.join(os.path.dirname(__file__), 'example.sqlite')
# with sqlite3.connect(f'{database_name}') as conn:
#     conn.row_factory = sqlite3.Row
#     cursor = conn.cursor()
#
#     cursor.execute(f"SELECT * from presidents")
#     ind = 3
#     # print(list(row))
#     while ind:
#         row = cursor.fetchone()
#         ind -= 1
#         print(row['name'])
