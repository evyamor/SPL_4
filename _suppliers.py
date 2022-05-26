import Supplier

class _suppliers:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO suppliers (id, name, logistic)
                VALUES (?,?,?)
        """, [supplier.id, supplier.name, supplier.logistic])

    def find(self, supp_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name, logistic FROM suppliers WHERE supp_id = ?
        """, [supp_id])
        return Supplier(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, name, logistic FROM vaccines
        """).fetchall()
        return [Supplier(*row) for row in all]