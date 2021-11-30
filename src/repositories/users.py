from entities.user import User
from db_connect import get_connection


class Users:
    """Takes care of all user related database operations
    """

    def __init__(self, connection) -> None:
        """sets up database_connection

        Args:
            connection: Database collection entity (see db_connect class for creation)
        """
        self._connection = connection
        # self._users_list.append(User("testaaja", "0000")

    def add_user(self, user):
        if self.get_user(user.get_name()) == None:

            """adds user to database

            Args:
                user : User entity
            """
            name = user.get_name()
            password = user.get_password()
            cursor = self._connection.cursor()
            cursor.execute(" INSERT INTO users (name, pw) VALUES (?,?)",
                       (name, password)
                        )
            self._connection.commit()
            return True
        return False

    def get_users(self):
        all_users = []
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")

        rows = cursor.fetchall()
        for row in rows:
            all_users.append(User(row["name"], row["pw"]))

        return all_users

    def get_user(self, name):
        """Get user from database

        Args:
            name : Name of the user we are looking for

        Returns:
            User entity: or None if user not found
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE name= ?",
                       (name,)
                       )
        row = cursor.fetchone()
        return User(row["name"], row["pw"]) if row else None


users = Users(get_connection())
