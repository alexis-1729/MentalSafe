from app.domain.unit_of_work import AbstractUnitOfWork
from app.domain.entities.content import Content
from app.domain.exceptions import ContentNotFound
from uuid import UUID, uuid4


class ContentService:

    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def add_content(
        self,
        content: str,
        url_video: str | None,
        complete: bool,
        id_chapter: UUID
    ) -> Content:
        """Agregar un nuevo contenido"""
        async with self.uow as uow:
            new_content = Content(
                id_content=uuid4(),
                content=content,
                url_video=url_video,
                complete=complete,
                id_chapter=id_chapter
            )
            await uow.content.add(new_content)
            await uow.commit()
            return new_content

    async def get_content_by_id(self, content_id: UUID) -> Content:
        """Obtener un contenido por ID"""
        async with self.uow as uow:
            content = await uow.content.get_by_id(content_id)
            
            if not content:
                raise ContentNotFound()
            return content

    async def get_content_by_chapter(self, chapter_id: UUID) -> list[Content]:
        """Obtener todos los contenidos de un capítulo"""
        async with self.uow as uow:
            contents = await uow.content.get_by_chapter(chapter_id)
            return contents

    async def get_all_contents(self) -> list[Content]:
        """Obtener todos los contenidos"""
        async with self.uow as uow:
            contents = await uow.content.get_all()
            return contents
