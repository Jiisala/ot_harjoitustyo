#Here be the logick or Sovelluslogiikka as we say in Finland

from repositories.problems import problems as default_problems
from repositories.users import users as default_users
from entities.problem import Problem
from entities.user import User

class Logic:

    def __init__(self, problems=default_problems, users=default_users) -> None:
        self._problems = problems
        self._users = users
        
    
    def new_user(self, name, pw):
        
        self._users.add_user(User(name, pw))

logic =Logic()