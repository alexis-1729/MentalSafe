from uuid import UUID
from typing import Optional, List

class Chapter:
    def __init__(
        self,
        id_chapter: UUID,
        title: str,
        description: str,
        num_caps: str,
        duration: str,
        id_section: UUID,
        complete: bool = False,
        numero: Optional[int] = None,
        url_image: Optional[str] = None,
        contents: Optional[List] = None
    ) -> None:
        self.id_chapter = id_chapter
        self.title = title
        self.description = description
        self.num_caps = num_caps
        self.duration = duration
        self.numero = numero
        self.id_section = id_section
        self.complete = complete
        self.url_image = url_image
        self.contents = contents or []
