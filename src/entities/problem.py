
class Problem:

    def __init__(self, name, author, grade, location, descr, img_url) -> None:
        self.author = author
        self.name = name
        self.location = location
        self.description = descr
        self.grade = grade
        self.img_url = img_url
