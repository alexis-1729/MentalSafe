class DomainError(Exception):
    pass

class InvalidPassword(DomainError):
    pass

class InvalidCredentials(DomainError):
    pass

class CourseNotFound(DomainError):
    pass

class SectionNotFound(DomainError):
    pass

class ChapterNotFound(DomainError):
    pass

class ContentNotFound(DomainError):
    pass