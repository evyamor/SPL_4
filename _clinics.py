import Clinic

class _clinics:

    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""
                INSERT INTO clinics (id, location, demand, logistic)
                VALUES (?,?,?,?)
        """, [clinic.id, clinic.location, clinic.demand, clinic.logistic])

    def find(self, clinic_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, location, demand, logistic FROM clinics WHERE clinic_id = ?
        """, [clinic_id])
        return Clinic(*c.fetchone())

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, location, demand, logistic FROM vaccines
        """).fetchall()
        return [Clinic(*row) for row in all]