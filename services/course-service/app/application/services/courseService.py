from app.domain.unit_of_work import AbstractUnitOfWork
from app.domain.exceptions import CourseNotFound
from app.domain.entities.course import Course
from uuid import UUID, uuid4

class CourseService:

    def __init__(self,
                 uow: AbstractUnitOfWork
                 ):
        self.uow = uow

    async def add_course(self,  title: str, description: str, tag: str, url_image: str)-> Course:
        async with self.uow as uow:
            course = Course(
                id_course= uuid4(),
                title=title,
                description= description,
                tag= tag,
                url_image=url_image
            )
            await uow.course.add(course)
            await uow.commit()
            return course

    async def get_course_id(self, course_id: UUID):

        async with self.uow as uow:
            course = await uow.course.get_by_id(course_id)

            if not course:
                raise CourseNotFound()
            return course
        
    async def get_course_tag(self, tag: str):
        async with self.uow as uow:
            course  = await uow.course.get_by_tag(tag)
            
            if not course:
                raise CourseNotFound()
            return course
        
        