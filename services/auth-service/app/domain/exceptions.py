class DomainError(Exception):
    pass

class UserAlredyExists(DomainError):
    pass

class InvalidPassword(DomainError):
    pass

class RegisterNotExist(DomainError):
    pass

class InvalidCredentials(DomainError):
    pass