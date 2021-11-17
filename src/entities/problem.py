
class Problem:

    def __init__(self, auth, name, grade, location, descr ) -> None:
        self._auth = auth
        self._name = name 
        self._location = location
        self._descr = descr 
        self._grade = grade

    def get_auth(self):
        return self._auth