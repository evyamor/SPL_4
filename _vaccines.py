import Vaccine

class _vaccines:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, vaccine):
        self._conn.execute("""
                INSERT INTO vaccines (id, date, supplier, quantity)
                VALUES (?,?,?,?)
        """, [vaccine.id, vaccine.date, vaccine.supplier, vaccine.quantity])

    def find(self, vacc_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, date, supplier, quantity FROM vaccines WHERE vacc_id = ?
        """, [vacc_id])
        return Vaccine(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, date, supplier, quantity FROM vaccines
        """).fetchall()
        return [Vaccine(*row) for row in all]