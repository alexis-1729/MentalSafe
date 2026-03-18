from uuid import UUID

class Course:
    def __init__(
            self, id_course: UUID, 
            title: str, 
            description: str,
            tag: str,
            url_image: str) -> None:
        self.id_course = id_course
        self.title = title
        self.description = description
        self.tag = tag
        self.url_image = url_image

        