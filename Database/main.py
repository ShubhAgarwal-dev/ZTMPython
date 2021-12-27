import sqlite3


def create_table():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
        CREATE TABLE "Seat"(
            "seat_id" TEXT,
            "taken" INTEGER,
            "price" REAL
        );

        """)
    connection.commit()
    connection.close()


def add_record(seat_id: str, tanken: bool | int, price: float):
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
        INSERT INTO "Seat"("seat_id", "taken", "price") VALUES (?, ?, ?)
        """, [seat_id, int(tanken), price])
    connection.commit()
    connection.close()


def select_all():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM "Seat"
        """)
    result = cursor.fetchall()
    connection.close
    return result


print(select_all())
