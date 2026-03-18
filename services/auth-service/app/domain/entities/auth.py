from uuid import UUID

class Auth:
    def __init__(self, id: UUID, email: str, password_h: str, role: str) -> None:
        self.id = id
        self.email = email
        self.password_h = password_h
        self.role = role

    