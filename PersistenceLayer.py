import sqlite3
import os
import imp
import atexit

class _PersistenceLayer:

    def __init__(self): # constructor
        self._connection = sqlite3.connect('database.db')

    def _close_db(self):
       self._connection.commit()
       self._connection.close()

    def insert_vaccines(self,id,date,supplier,quantity,dir):
        self.connection.execute("""
            INSERT INTO vaccines (id,date,supplier,quantity)
            VALUES (?,?,?,?)""", [id,date,supplier,quantity]
        )

    def insert_vaccines(self,id,date,supplier,quantity,dir):
        self.connection.execute("""
            INSERT INTO vaccines (id,date,supplier,quantity)
            VALUES (?,?,?,?)""", [id,date,supplier,quantity]
        )

    def insert_vaccines(self,id,date,supplier,quantity,dir):
        self.connection.execute("""
            INSERT INTO vaccines (id,date,supplier,quantity)
            VALUES (?,?,?,?)""", [id,date,supplier,quantity]
        )

    def insert_vaccines(self,id,date,supplier,quantity,dir):
        self.connection.execute("""
            INSERT INTO vaccines (id,date,supplier,quantity)
            VALUES (?,?,?,?)""", [id,date,supplier,quantity]
        )

psl = _PersistenceLayer()
atexit.register(psl._close_db)