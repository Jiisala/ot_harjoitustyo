class User:
    """User entity
    Attributes:
        name(string): username
        password(string): password
    """

    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password
