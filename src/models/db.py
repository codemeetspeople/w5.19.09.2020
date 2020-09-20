import os
import pathlib
import sqlite3


PROJECT_ROOT = pathlib.Path(__file__).parent.absolute()
DB_PATH = os.path.join(PROJECT_ROOT, 'database.db')

CREATE_TABLE = (
    'CREATE TABLE IF NOT EXISTS book ('
    '    id INTEGER PRIMARY KEY AUTOINCREMENT,'
    '    author TEXT NOT NULL,'
    '    title TEXT NOT NULL'
    ');'
)
INSERT_STATEMENT = 'INSERT INTO book (author, title) VALUES (?,?)'
UPDATE_STATEMENT = 'UPDATE book SET author = ?, title = ? WHERE id = ?'
SELECT_STATEMENT = 'SELECT * FROM book WHERE id = ?'

connection = None


def get_connection():
    global connection
    if not connection:
        connection = sqlite3.connect(DB_PATH)
    return connection


def create_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CREATE_TABLE)
    conn.commit()


create_database()
