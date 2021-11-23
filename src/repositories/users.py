from entities.user import User

class Users:

    def __init__(self) -> None:
        self._users_list = []
        self._users_list.append(User("testaaja", "0000"))

    def add_user(self,user):
        self._users_list.append(user)

    def get_users(self):
        return self._users_list    
    
    def find_user(self, name):
        
        for user in self._users_list:
            if user.get_name() == name:
                
                return True
        return False

    def get_user(self, name):
        for user in self._users_list:
            if user.get_name() == name:
                return user

users = Users()