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
When writing tests, it's not always necessary to mock database calls completely.
Use supplied example.sqlite file as database fixture file.
"""
import os
import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = os.path.join(os.path.dirname(__file__), database_name)
        with sqlite3.connect(self.database_name) as conn:
            query = "SELECT 1 FROM sqlite_master WHERE type='table' and name = ?"
            if conn.execute(query, (table_name,)).fetchone() is not None:
                self.table_name = table_name

    def database_connection(func):
        def wrapper(self, *args, **kwargs):
            with sqlite3.connect(self.database_name) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                result = func(self, cursor, *args, **kwargs)
                return result

        return wrapper

    @database_connection
    def __len__(self, cursor):
        cursor.execute(f"SELECT COUNT(*) from {self.table_name}")
        amount_of_rows = cursor.fetchone()[0]
        cursor.close()
        return amount_of_rows

    @database_connection
    def __getitem__(self, cursor, item):
        cursor.execute(f"SELECT * from {self.table_name} where name=?", (item,))
        row_item = tuple(cursor.fetchone())
        cursor.close()
        return row_item

    def __contains__(self, item):
        try:
            return bool(self.__getitem__(item))
        except TypeError:
            return False

    @database_connection
    def __iter__(self, cursor):
        yield from cursor.execute(f"SELECT * from {self.table_name}")
        cursor.close()
