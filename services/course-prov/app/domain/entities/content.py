from uuid import UUID
from typing import Optional
class Content:

    def __init__(
            self,
            id_content: UUID,
            content: str,
            url_video: Optional[str],
            complete: bool,
            id_chapter: UUID) -> None:

            self.id_content = id_content
            self.content = content
            self.url_video = url_video
            self.complete = complete
            self.id_chapter = id_chapter