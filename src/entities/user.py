class User:

    def __init__(self, name, password) -> None:
        self._name = name
        self._pw = password

    def get_name(self):
        return self._name
    
    def get_password(self):
        print ("pw", self._pw)
        return self._pw

#user = User()