
import shutil
from PIL import UnidentifiedImageError
from PIL import Image
from repositories.problems import problems as default_problems
from repositories.users import users as default_users
from entities.problem import Problem
from entities.user import User


class Logic:
    """Main program logic

    Attributes: problems: entity for handling problems
        Users: entity for handling users
        current user: current user
    """

    def __init__(self, problems=default_problems, users=default_users) -> None:
        self._problems = problems
        self._users = users
        self.current_user = None

    def new_user(self, name, password):
        """Creates new user by sending username and password to the Class handling
           communication with user database

        Args:
            name (String): username
            password (String): password

        """

        return self._users.add_user(User(name, password))

    def new_problem(self, name, grade, location, description, img_url):
        """Creates new problem by sending necessary info to the class handling
           communication with problems database

        Args:
            name (String): name
            grade (String): grade, preferably in basic european boulder
                grading system (not enforced)
            location (String): Location of the problem
            description (String): A short description of the problem
            img_url (String, optional):.
        """
        author = self.current_user
        self._problems.add_problem(
            Problem(name, author, grade, location, description, img_url))

    def add_problem_to_uxp(self, problem):
        """Adds problem and current user to uxp database by sending necessary
           information to the class handling communication with the uxp database.

        Args:
            problem (problem): problem entity to add
        """
        self._problems.add_to_uxp(problem, self.current_user)

    def remove_problem_from_uxp(self, problem):
        """Removes problem and current user from the uxp database by sending
        necessary information to class handling communication with the database.

        Args:
            problem (problem): problem entity to add
        """
        self._problems.remove_problem_from_uxp(problem, self.current_user)

    def login(self, name, password):
        """Handles login and adds user as the current user

        Args:
            name (String): Username
            password (String): Password

        Raises:
            ValueError if not succesfull
        """

        user = self._users.get_user(name)
        if user:
            if self.check_pw(user, password):
                self.current_user = user
            else:
                raise ValueError
        else:
            raise ValueError

    def log_out(self):
        """Changes value of self.current_user to None
        """
        self.current_user = None

    def check_pw(self, user, password):
        """Checks if the password given matches the given users password

        Args:
            user (User): User entity
            password (String): Pasword

        Returns:
            Boolean: Knowledge if the password was a match or not
        """
        return user.password == password

    def check_user_exists(self, name):
        """Checks if the user of given username exists in the database

        Args:
            name (String): Username

        Returns:
            user if user exists
        """
        user = self._users.get_user(name)
        return user

    def get_all_problems(self):
        """call to fetch all problems from the database

        Returns:
            List: List of problem entities
        """
        return self._problems.get_problems()

    def get_problems_for_user(self):
        """call to fetch current users problems from the database

        Returns:
            List: List of problem entities
        """
        return self._problems.get_problems_for_user(self.current_user)

    def mark_solved(self, value, problem):
        """marks problem solved or unsolved for current user

        Args:
            value (Int): Value 1 for solved, 0 for unsolved
            problem (problem): problem entity
        """
        self._problems.mark_solved(value, problem, self.current_user)

    def handle_img_path(self, img_path):
        """shortens path to image to image name and calls copy_image function,
        and create_thumbnail function

        Args:
            img_url (Str): Path to image in file

        Raises:
            UnidentifiedImageError: unsupported image type
        """
        img_name = img_path.split("/")[-1]

        if img_name.split(".")[-1] not in ["jpg", "jpeg", "png", "gif", "bmp"]:
            raise UnidentifiedImageError
        self.create_thumbnail(img_path)
        self.copy_image(img_path)

        return img_name

    def copy_image(self, img_path):
        """Copies image to programs img folder
        """
        try:
            shutil.copy(img_path, "./data/img/")
        except shutil.SameFileError:
            pass

    def create_thumbnail(self, img_path):
        """creates thumbnnail from image in given path

        Args:
            img_url (Str): path to image file

        """

        with Image.open(img_path) as pic:
            name_and_ext = img_path.split("/")[-1]
            name = name_and_ext.split(".")[0]
            ext = name_and_ext.split(".")[-1]
            pic.thumbnail((200, 200))
            pic.save(f"./data/img/{name}_thumbnail.{ext}", ext)

    def get_path_to_thumbnail(self, img_path):
        """Function to get path to thumbnail of given image

        Args:
            img_path (Str): Path to a image

        Returns:
            Str: Path to thumbnail
        """
        name_and_ext = img_path.split("/")[-1]
        name = name_and_ext.split(".")[0]
        ext = name_and_ext.split(".")[-1]

        return f"./data/img/{name}_thumbnail.{ext}"


logic = Logic()
