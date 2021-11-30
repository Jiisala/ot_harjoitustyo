import sqlite3
from config import DB_PATH

connection = sqlite3.connect(DB_PATH)
connection.isolation_level = None

connection.row_factory = sqlite3.Row


def get_connection():
    return connection
