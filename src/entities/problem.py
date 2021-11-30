
class Problem:

    def __init__(self, name, author, grade, location, descr, img_url) -> None:
        self._author = author
        self._name = name
        self._location = location
        self._descr = descr
        self._grade = grade
        self._img_url = img_url

    def get_author(self):
        return self._author

    def get_name(self):
        return self._name

    def get_location(self):
        return self._location

    def get_description(self):
        return self._descr

    def get_grade(self):
        return self._grade

    def get_img_url(self):
        return self._img_url

# problem = Problem()"
