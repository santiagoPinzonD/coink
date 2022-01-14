import sqlite3 as sql

DB_PATH = "/home/estudio/interviews/coink/database/user.db"


def create_db():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE user (
        name text,
        email text,
        city text
    )""")
    conn.commit()
    conn.close()


def add_values():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        ("santiago", "test@gmail.com", "cali"),
    ]
    cursor.executemany("""INSERT INTO user VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db()
    add_values()
