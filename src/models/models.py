from models.db import (
    get_connection,
    INSERT_STATEMENT,
    UPDATE_STATEMENT,
    SELECT_STATEMENT
)


class Book:
    conn = get_connection()

    def __init__(self, _id=None):
        self._id = None
        self._author = None
        self._title = None
        self._changed = False

        if _id is not None:
            self._load(_id)

    @property
    def id(self):
        return self._id

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @author.setter
    def author(self, value):
        self._author = value
        self._changed = True

    @title.setter
    def title(self, value):
        self._title = value
        self._changed = True

    def _load(self, _id):
        cursor = self.conn.cursor()
        cursor.execute(SELECT_STATEMENT, (_id,))
        book = cursor.fetchone()
        self._id, self._title, self._author = book

    def save(self):
        if not self._changed:
            return

        cursor = self.conn.cursor()
        if not self.id:
            cursor.execute(INSERT_STATEMENT, (self.author, self.title))
            self._id = cursor.lastrowid
        else:
            cursor.execute(UPDATE_STATEMENT, (self.author, self.title, self.id))
        self.conn.commit()
        self._changed = False
