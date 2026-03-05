from app.domain.unit_of_work import AbstractUnitOfWork
from app.domain.entities.chapter import Chapter
from app.domain.exceptions import ChapterNotFound
from uuid import UUID, uuid4
from typing import Optional


class ChapterService:

    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def add_chapter(
        self,
        title: str,
        description: str,
        num_caps: str,
        duration: str,
        id_section: UUID,
        numero: Optional[int] = None,
        url_image: Optional[str] = None
    ) -> Chapter:
        """Agregar un nuevo capítulo"""
        async with self.uow as uow:
            chapter = Chapter(
                id_chapter=uuid4(),
                title=title,
                description=description,
                num_caps=num_caps,
                duration=duration,
                id_section=id_section,
                numero=numero,
                url_image=url_image
            )
            await uow.chapter.add(chapter)
            await uow.commit()
            return chapter

    async def get_chapter_by_id(self, chapter_id: UUID) -> Chapter:
        """Obtener un capítulo por ID"""
        async with self.uow as uow:
            chapter = await uow.chapter.get_by_id(chapter_id)
            
            if not chapter:
                raise ChapterNotFound()
            return chapter

    async def get_chapters_by_course(self, course_id: UUID) -> list[Chapter]:
        """Obtener lista de capítulos por id course"""
        async with self.uow as uow:
            chapters = await uow.chapter.get_list_chapter(course_id)
            return chapters

    async def get_all_chapters(self) -> list[Chapter]:
        """Obtener todos los capítulos"""
        async with self.uow as uow:
            chapters = await uow.chapter.get_all()
            return chapters
