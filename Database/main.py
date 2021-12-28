import sqlite3


class DatabaseManipulation():
    def __init__(self, database_path='cinema.db') -> None:
        self._filepath = database_path
        self.create_table(self._filepath)

    @staticmethod
    def create_table(database_path):
        connection = sqlite3.connect(database_path)
        connection.execute("""
            CREATE TABLE "Seat"(
                "seat_id" TEXT,
                "taken" INTEGER,
                "price" REAL
            );

            """)
        connection.commit()
        connection.close()
        return None

    def add_record(self, seat_id: str, tanken: bool | int, price: float):
        connection = sqlite3.connect(self._filepath)
        connection.execute("""
            INSERT INTO "Seat"("seat_id", "taken", "price") VALUES (?, ?, ?)
            """, [seat_id, int(tanken), price])
        connection.commit()
        connection.close()
        return None

    def select_all(self):
        connection = sqlite3.connect(self._filepath)
        cursor = connection.cursor()  # We use cursor in read operations
        cursor.execute("""
            SELECT * FROM "Seat"
            """)
        result = cursor.fetchall()
        connection.close
        return result

    def update_seat_taken(self, seat_id: str):
        connection = sqlite3.connect(self._filepath)
        connection.execute("""
            UPDATE "Seat" SET "taken" = 1 WHERE "seat_id" = ?
            """, [seat_id])
        connection.commit()
        connection.close()
        return None

    def delete_seat(self,  seat_id: str):
        connection = sqlite3.connect(self._filepath)
        connection.execute("""
            DELETE FROM "Seat" WHERE "seat_id" = ?
        """, [seat_id])
        connection.commit()
        connection.close()
        return None


if __name__ == '__main__':
    db = DatabaseManipulation()
    db.add_record("A1", True, 200)
    db.add_record("A2", False, 300)
    db.add_record("A3", False, 400)
    db.add_record("A4", True, 310)
    print(db.select_all())
    db.update_seat_taken("A2")
    db.delete_seat("A4")
