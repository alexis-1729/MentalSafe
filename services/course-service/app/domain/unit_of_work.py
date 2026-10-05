from abc import abstractmethod, ABC
from app.domain.repositories.courseRepository import CourseRepository
from app.domain.repositories.sectionRepository import SectionRepository
from app.domain.repositories.chapterRepository import ChapterRepository
from app.domain.repositories.contentRepository import ContentRepository


class AbstractUnitOfWork(ABC):

    course: CourseRepository
    section: SectionRepository
    chapter: ChapterRepository
    content: ContentRepository

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *args):
        await self.rollback()

    @abstractmethod
    async def commit(self):
        pass
    
    @abstractmethod
    async def rollback(self):
        pass