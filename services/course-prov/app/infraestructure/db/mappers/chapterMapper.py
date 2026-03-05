from app.domain.entities.chapter import Chapter
from app.infraestructure.db.models.chapterModel import ChapterORM
from app.infraestructure.db.mappers.contentMapper import ContentMapper

class ChapterMapper:

    @staticmethod
    def to_domain(orm: ChapterORM) -> Chapter:
        return Chapter(
            id_chapter=orm.id_chapter,
            title=orm.title,
            description=orm.description,
            num_caps=orm.num_caps,
            duration=orm.duration,
            numero=orm.numero,
            id_section=orm.id_section,
            complete=orm.complete,
            url_image=orm.url_image,
            contents=[ContentMapper.to_domain(c) for c in orm.contents] if orm.contents else []
        )

    @staticmethod
    def to_orm(entity: Chapter) -> ChapterORM:
        return ChapterORM(
            id_chapter=entity.id_chapter,
            title=entity.title,
            description=entity.description,
            num_caps=entity.num_caps,
            duration=entity.duration,
            numero=entity.numero,
            id_section=entity.id_section,
            complete=entity.complete,
            url_image=entity.url_image
        )
