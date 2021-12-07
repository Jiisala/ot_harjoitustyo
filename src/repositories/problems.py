
from entities.problem import Problem
from db_connect import get_connection


class Problems:
    """Takes care of all problem related database operations
    """

    def __init__(self, connection) -> None:
        """sets up database_connection

        Args:
            connection: Database collection entity (see db_connect class for creation)
        """
        self._connection = connection

    def add_problem(self, problem):
        """adds problem to database

        Args:
            problem : Problem entity
        """
        name = problem.name
        author_name = problem.author.name
        grade = problem.grade
        location = problem.location
        description = problem.description
        img_url = problem.img_url

        if self.get_problem(name) is None:
            cursor = self._connection.cursor()

            cursor.execute(""" INSERT INTO problems (name, author_id, grade, location, description, img_url)
                           VALUES (?,?,?,?,?,?)""",
                           (name, author_name, grade,
                            location, description, img_url)
                           )
            self._connection.commit()

            author = problem.author
            self.add_to_uxp(problem, author)

    def add_to_uxp(self, problem, user):

        cursor = self._connection.cursor()
        cursor.execute(
            f"SELECT id FROM problems WHERE name='{problem.name}'")
        row = cursor.fetchone()
        problem_id = row["id"]
        cursor.execute(f"SELECT id FROM users WHERE name='{user.name}'")
        row = cursor.fetchone()
        user_id = row["id"]
        cursor.execute(" INSERT INTO uxp (user_id, problem_id, solved) Values (?,?,?)",
                       (user_id, problem_id, 0))
        self._connection.commit()

    def remove_problem_from_uxp(self, problem, user):
        cursor = self._connection.cursor()
        cursor.execute(
            f"SELECT id FROM problems WHERE name='{problem.name}'")
        row = cursor.fetchone()
        problem_id = row["id"]
        cursor.execute(f"SELECT id FROM users WHERE name='{user.name}'")
        row = cursor.fetchone()
        user_id = row["id"]
        cursor.execute(
            f" DELETE FROM uxp WHERE user_id = {user_id} AND problem_id = {problem_id}")
        self._connection.commit()

    def get_problems(self):
        """Get all problems from database

        Args: none

        Returns:
            List of problems
        """
        all_problems = []
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM problems")

        rows = cursor.fetchall()
        for row in rows:

            all_problems.append(Problem(
                row["name"],
                row["author_id"],
                row["grade"],
                row["location"],
                row["description"],
                row["img_url"]))

        return all_problems

    def get_problem(self, name):
        """Get problem from database

        Args:
            name : Name of the problem we are looking for

        Returns:
            Problem entity: or None if user not found
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM problems WHERE name= ?",
                       (name,)
                       )
        row = cursor.fetchone()

        return Problem(
            row["name"],
            row["author_id"],
            row["grade"],
            row["location"],
            row["description"],
            row["img_url"]
        ) if row else None

    def get_problems_for_user(self, user):

        cursor = self._connection.cursor()
        cursor.execute(
            f"""SELECT P.*, UP.solved
            FROM problems P, uxp UP, users U
            WHERE U.id = UP.user_id
            AND P.id = UP.problem_id
            AND U.name = '{user.name}'""")
        rows = cursor.fetchall()
        user_problems = []
        for row in rows:
            user_problems.append((Problem(
                row["name"],
                row["author_id"],
                row["grade"],
                row["location"],
                row["description"],
                row["img_url"]
            ), row["solved"]))
        return user_problems

    def mark_solved(self, value, problem, user):

        cursor = self._connection.cursor()
        cursor.execute(
            f"SELECT id FROM problems WHERE name='{problem.name}'")
        row = cursor.fetchone()
        problem_id = row["id"]
        cursor.execute(f"SELECT id FROM users WHERE name='{user.name}'")
        row = cursor.fetchone()
        user_id = row["id"]
        cursor.execute(
            f""" UPDATE uxp SET solved = {value}
            WHERE user_id = {user_id}
            AND problem_id = {problem_id}""")
        self._connection.commit()


problems = Problems(get_connection())
