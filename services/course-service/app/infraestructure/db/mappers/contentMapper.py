from app.domain.entities.content import Content
from app.infraestructure.db.models.contentModel import ContentORM


class ContentMapper:


    @staticmethod
    def to_domain(orm: ContentORM)-> Content:
        return Content(
            id_content= orm.id_content,
            content= orm.content,
            url_video= orm.url_video,
            complete= orm.complete,
            id_chapter= orm.id_chapter
        )
    
    @staticmethod
    def to_orm(entity: Content)-> ContentORM:
        return ContentORM(
            id_content = entity.id_content,
            content = entity.content,
            url_video = entity.url_video,
            complete = entity.content,
            id_chapter = entity.id_chapter
        )