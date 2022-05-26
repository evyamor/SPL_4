import sqlite3
import _vaccines
import _suppliers
import _clinics
import _logistics
import Vaccine
import Supplier
import Clinic
import Logistic
import atexit

class _Repository:
        def __init__(self):
            self._conn = sqlite3.connect('database.db')
            self.vaccines = _vaccines(self._conn)
            self.suppliers = _suppliers(self._conn)
            self.clinics = _clinics(self._conn)
            self.logistics = _logistics(self._conn)

        def _close(self):
            self._conn.commit()
            self._conn.close()

        def create_tables(self):
            self.connection.executescript("""
                CREATE TABLE vaccines (
                    id      INT     PRIMARY KEY,
                    date    DATE    NOT NULL,
                    supplier    INTEGER     REFERENCES Supplier(id),
                    quantity    INTEGER     NOT NULL
                            );   
                CREATE TABLE suppliers (
                    id      INT     PRIMARY KEY,
                    name    DATE    NOT NULL,
                    logistic INTEGER REFERENCES Logistic(id)
                            );            
                CREATE TABLE clinics (
                    id      INT     PRIMARY KEY,
                    location    STRING    NOT NULL,
                    demand    INTEGER     NOT NULL,
                    logistic  INTEGER     REFERENCES Logistic(id)
                            );            
                CREATE TABLE logistics (
                    id      INT     PRIMARY KEY,
                    name    STRING    NOT NULL,
                    count_sent    INTEGER     NOT NULL,
                    count_received  INTEGER     NOT NULL
                            );            
                            """)

        def get_vaccines(self): #returns ALL vaccines
            c = self._conn.cursor()
            all = c.execute("""
                SELECT id, date, supplier, quantity FROM vaccines
            """).fetchall()
            return [Vaccine(*row) for row in all]

        def get_supplier_by_id(self):
            c = self._conn.cursor()


        def get_suppliers(self): #returns ALL suppliers
            c = self._conn.cursor()
            all = c.execute("""
                SELECT id, name, logistic FROM suppliers
            """).fetchall()
            return [Supplier(*row) for row in all]

        def get_clinics(self): #returns ALL clinics
            c = self._conn.cursor()
            all = c.execute("""
                SELECT id, location, demand, logistic FROM clinics
            """).fetchall()
            return [Clinic(*row) for row in all]


        def get_logistics(self): #returns ALL logistics
            c = self._conn.cursor()
            all = c.execute("""
                SELECT id, name, count_sent, count_received FROM vaccines
            """).fetchall()
            return [Logistic(*row) for row in all]


rpstry = _Repository()
atexit.register(rpstry._close_db) # the singleton implementation