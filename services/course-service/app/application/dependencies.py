from fastapi import Depends
from app.application.services.courseService import CourseService
from app.application.services.sectionService import SectionService
from app.application.services.chapterService import ChapterService
from app.application.services.contentService import ContentService
from app.domain.unit_of_work import AbstractUnitOfWork
from app.infraestructure.db.dependencies import get_uow

def get_course_service(
        uow: AbstractUnitOfWork = Depends(get_uow)
):
    return CourseService(uow)

def get_section_service(
        uow: AbstractUnitOfWork = Depends(get_uow)
):
    return SectionService(uow)

def get_chapter_service(
        uow: AbstractUnitOfWork = Depends(get_uow)
):
    return ChapterService(uow)

def get_content_service(
        uow: AbstractUnitOfWork = Depends(get_uow)
):
    return ContentService(uow)