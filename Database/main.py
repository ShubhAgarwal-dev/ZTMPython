import sqlite3


class DatabaseManipulation():
    def __init__(self, database_path='cinema.db') -> None:
        self._filepath = database_path
        self.create_table()

    def create_table(self):
        connection = sqlite3.connect(self._filepath)
        connection.execute("""
            CREATE TABLE "Seat"(
                "seat_id" TEXT,
                "taken" INTEGER,
                "price" REAL
            );

            """)
        connection.commit()
        connection.close()

    def add_record(self, seat_id: str, tanken: bool | int, price: float):
        connection = sqlite3.connect(self._filepath)
        connection.execute("""
            INSERT INTO "Seat"("seat_id", "taken", "price") VALUES (?, ?, ?)
            """, [seat_id, int(tanken), price])
        connection.commit()
        connection.close()

    def select_all(self):
        connection = sqlite3.connect(self._filepath)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM "Seat"
            """)
        result = cursor.fetchall()
        connection.close
        return result
