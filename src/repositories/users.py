from entities.user import User

class Users:

    def __init__(self) -> None:
        self._users_list = []

    def add_user(self,user):
        self._users_list.append(user)

    def get_users(self):
        return self._users_list    

users = Users()