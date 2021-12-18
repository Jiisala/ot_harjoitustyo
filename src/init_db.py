from db_connect import get_connection


def clear_database(connection):
    """drops tables if database exists already
    """
    cursor = connection.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS users 
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS problems 
    """)
    cursor.execute("""
        DROP TABLE IF EXISTS uXp 
    """)

    connection.commit()


def create_database(connection):

    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY, 
            name TEXT,
            pw TEXT 
        )
    """)  # Reference primary keay users breaks the test, find out why
    cursor.execute("""
        CREATE TABLE problems (
            id INTEGER PRIMARY KEY,
            name TEXT,
            author_id TEXT,
            grade TEXT,
            location TEXT,
            description TEXT,
            img_url, TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE uxp (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            problem_id INTEGER,
            solved INTEGER
        )
    """)
    connection.commit()


def create_default_user(connection):
    """Creates default user for development time purposes,
       most propably will get deleted from the final version

    Args:
        connection : Database connection
    """
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, pw) VALUES (?,?)",
                   ("testi", "0000"))
    connection.commit()


def init_db():
    """Creates new database by establishing connection and calling helper functions.
    """
    connection = get_connection()

    clear_database(connection)
    create_database(connection)
    create_default_user(connection)


if __name__ == "__main__":
    init_db()
