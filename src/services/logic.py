#Here be the logick or Sovelluslogiikka as we say in Finland

from repositories.problems import problems as default_problems
from repositories.users import users as default_users
from entities.problem import Problem
from entities.user import User

class Logic:

    def __init__(self, problems=default_problems, users=default_users) -> None:
        self._problems = problems
        self._users = users
        self._current_user = None        
    
    def new_user(self, name, pw):
        if not self.check_user_exists(name):
            self._users.add_user(User(name, pw))
            
        else:
            print("Here we will do something if the name exists already")
            return False

    def login(self, name, pw):
        if self.check_user_exists(name):
            user = self._users.get_user(name)
            if self.check_pw(user, pw):
                self._current_user = user
                return True
            else:
                print("check password error handling goes here")
                return False
        else:
            print("user not found error handling goes here")
            return False        

    def check_pw(self, user, pw):
       # print ("pw given", pw)
        print (user.get_password() == pw)
        return user.get_password() == pw
                

    def check_user_exists(self, name):
        
        return self._users.find_user(name)

    def get_user(self):
        return self._current_user
    #Dummy funktion for testing, due to be deleted
    def get_problems_temp(self):
        return self._problems.get_problems_temp()
logic =Logic()