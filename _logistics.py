import Logistic

class _logistics:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, logistic):
        self._conn.execute("""
                INSERT INTO logistics (id, name, count_sent, count_received)
                VALUES (?,?,?,?)
        """, [logistic.id, logistic.name, logistic.count_sent, logistic.count_received])

    def find(self, log_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name, count_sent, count_received FROM logistics WHERE log_id = ?
        """, [log_id])
        return Logistic(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, name, count_sent, count_received FROM logistics
        """).fetchall()
        return [Logistic(*row) for row in all]
