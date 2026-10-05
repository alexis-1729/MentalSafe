from app.domain.entities.section import Section
from app.infraestructure.db.models.sectionModel import SectionORM
from app.infraestructure.db.mappers.chapterMapper import ChapterMapper

class SectionMapper:
    @staticmethod
    def to_domain(orm: SectionORM) -> Section:
        return Section(
            id_section=orm.id_section,
            id_course=orm.id_course,
            chapters=[ChapterMapper.to_domain(ch) for ch in orm.chapters]
        )

    @staticmethod
    def to_orm(entity: Section) -> SectionORM:
        return SectionORM(
            id_section=entity.id_section,
            id_course=entity.id_course
        )