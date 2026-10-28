class User:
    def __init__(
        self,
        id: int,
        username: str,
        email: str,
        password: str,
        name: str,
        lastname: str,
        role: str,
    ):
        self.id = id
        self.username = username
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.role = role
