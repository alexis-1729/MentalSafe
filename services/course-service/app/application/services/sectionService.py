from app.domain.unit_of_work import AbstractUnitOfWork
from app.domain.entities.section import Section
from app.domain.exceptions import SectionNotFound
from uuid import UUID, uuid4

class SectionService:

    def __init__(self, uow: AbstractUnitOfWork):
        self.uow = uow

    async def add_section(self, id_course: UUID) -> Section:
        """Agregar una nueva sección"""
        async with self.uow as uow:
            section = Section(
                id_section=uuid4(),
                id_course=id_course
            )
            await uow.section.add(section)
            await uow.commit()
            return section

    async def get_section_by_id(self, section_id: UUID) -> Section:
        """Obtener una sección por ID"""
        async with self.uow as uow:
            section = await uow.section.get_by_id(section_id)
            
            if not section:
                raise SectionNotFound()
            return section

    async def get_sections_by_course(self, course_id: UUID) -> list[Section]:
        """Obtener todas las secciones de un curso"""
        async with self.uow as uow:
            sections = await uow.section.get_by_course(course_id)
            return sections

    async def get_all_sections(self) -> list[Section]:
        """Obtener todas las secciones"""
        async with self.uow as uow:
            sections = await uow.section.get_all()
            return sections