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

    def add_user(self, user):
        """adds user to database

        Args:
            user : User entity
        Returns:
            Boolean: Knowledge if the database operation wass successfull
        """
        if self.get_user(user.name) is None:

            name = user.name
            password = user.password
            cursor = self._connection.cursor()
            cursor.execute(" INSERT INTO users (name, pw) VALUES (?,?)",
                           (name, password)
                           )
            self._connection.commit()
        else:
            raise ValueError    
        

    def get_users(self):
        """function to get all users from database

        Returns:
            list: List of user entities
        """
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
