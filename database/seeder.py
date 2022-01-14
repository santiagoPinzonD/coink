import sqlite3 as sql
""" File that create the database,
the path of DB_PATH will be a path abosulte since your root
"""
DB_PATH = "YourPath/coink/database/user.db"


def create_db():
    """Method that create a db"""
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE user (
        name text,
        email text,
        city text
    )""")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    """ Main Function """

    create_db()
