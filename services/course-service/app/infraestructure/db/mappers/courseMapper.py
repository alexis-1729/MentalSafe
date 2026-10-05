from app.domain.entities.course import Course
from app.infraestructure.db.models.courseModel import CourseORM

class CourseMapper:

    @staticmethod
    def to_domain(orm: CourseORM)-> Course:
        return Course(
            id_course= orm.id_course,
            title = orm.title,
            description= orm.description,
            tag= orm.tag,
            url_image= orm.url_image
        )

    @staticmethod
    def to_orm(entity: Course)-> CourseORM:
        return CourseORM(
            id_course = entity.id_course,
            title = entity.title,
            descritpion = entity.description,
            tag = entity.tag,
            url_image = entity.url_image
        )