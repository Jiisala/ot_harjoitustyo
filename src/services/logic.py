# Here be the logick or Sovelluslogiikka as we say in Finland

from repositories.problems import problems as default_problems
from repositories.users import users as default_users
from entities.problem import Problem
from entities.user import User


class Logic:

    def __init__(self, problems=default_problems, users=default_users) -> None:
        self._problems = problems
        self._users = users
        self._current_user = None

    def new_user(self, name, password):
        
        return self._users.add_user(User(name, password))
            
        

    def new_problem(self, name, grade, location, description, img_url=None):
        author = self._current_user
        self._problems.add_problem(
            Problem(name, author, grade, location, description, img_url))

    def login(self, name, password):

        user = self._users.get_user(name)
        if user:
            if self.check_pw(user, password):
                self._current_user = user
                return True
            else:
                print("check password error handling goes here")
                return False
        
        print("user not found error handling goes here")
        return False

    def check_pw(self, user, password):
        print(user.get_password() == password)
        return user.get_password() == password

    def check_user_exists(self, name):
        user = self._users.get_user(name)
        return True if user else False

    def get_user(self):
        return self._current_user

    def get_all_problems(self):
        return self._problems.get_problems()

    # def get_problems_cur_user(self):
     #   return self._problems.get_problems_user(self._current_user)

    def temp_for_test(self):
        return self._users.get_users()


logic = Logic()
