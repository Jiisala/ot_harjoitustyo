# Here be the logick or Sovelluslogiikka as we say in Finland

from repositories.problems import problems as default_problems
from repositories.users import users as default_users
from entities.problem import Problem
from entities.user import User


class Logic:

    def __init__(self, problems=default_problems, users=default_users) -> None:
        self._problems = problems
        self._users = users
        self.current_user = None

    def new_user(self, name, password):

        return self._users.add_user(User(name, password))

    def new_problem(self, name, grade, location, description, img_url=None):
        author = self.current_user
        self._problems.add_problem(
            Problem(name, author, grade, location, description, img_url))

    def add_problem_to_uxp(self, problem):
        self._problems.add_to_uxp(problem, self.current_user)

    def remove_problem_from_uxp(self, problem):
        self._problems.remove_problem_from_uxp(problem, self.current_user)

    def login(self, name, password):

        user = self._users.get_user(name)
        if user:
            if self.check_pw(user, password):
                self.current_user = user
                return True
            else:
                print("check password error handling goes here")
                return False

        print("user not found error handling goes here")
        return False

    def check_pw(self, user, password):
        #print(user.password == password)
        return user.password == password

    def check_user_exists(self, name):
        user = self._users.get_user(name)
        return True if user else False

    def get_all_problems(self):
        return self._problems.get_problems()

    def get_problems_for_user(self):
        return self._problems.get_problems_for_user(self.current_user)

    def mark_solved(self, value, problem):
        self._problems.mark_solved(value, problem, self.current_user)


logic = Logic()
