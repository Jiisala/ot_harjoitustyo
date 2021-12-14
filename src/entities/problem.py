
class Problem:
    """Problem entity
    Attributes:
        name (String): name
        grade (String): grade, preferably in basic european boulder
            grading system (not enforced)
        location (String): Location of the problem
        description (String): A short description of the problem
        img_url (String): Image goes here when the implementation is ready.
    """

    def __init__(self, name, author, grade, location, descr, img_url) -> None:
        self.author = author
        self.name = name
        self.location = location
        self.description = descr
        self.grade = grade
        self.img_url = img_url
