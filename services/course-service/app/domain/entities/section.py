from uuid import UUID
from typing import List, Optional

class Section:
    def __init__(self, 
                 id_section: UUID,
                 id_course: UUID,
                 chapters: Optional[List] = None):
                self.id_section = id_section
                self.id_course = id_course
                self.chapters = chapters or []
        