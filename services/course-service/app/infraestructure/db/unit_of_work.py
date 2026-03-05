from domain.unit_of_work import AbstractUnitOfWork
from app.infraestructure.db.repositories.courseRepository import SQLAlchemyCourseRepository
from app.infraestructure.db.repositories.sectionRepository import SQLAlchemySectionRepository
from app.infraestructure.db.repositories.chapterRepository import SQLAlchemyChapterRepository
from app.infraestructure.db.repositories.contentRepository import SQLAlchemyContentRepository


class SQLAlchemyUnitOfWork(AbstractUnitOfWork):

    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory
        self.course = SQLAlchemyCourseRepository(self.session)
        self.section = SQLAlchemySectionRepository(self.session)
        self.chapter = SQLAlchemyChapterRepository(self.session)
        self.content = SQLAlchemyContentRepository(self.session)
        return await super().__aenter__()
    
    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self.session.close()

    async def commit(self):
        await self.session.commit()
    
    async def rollback(self):
        await self.session.rollback()