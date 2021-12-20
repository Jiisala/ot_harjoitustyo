class User:
    """User entity
    Attributes:
        name(Str): username
        password(Str): password
    """

    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password
