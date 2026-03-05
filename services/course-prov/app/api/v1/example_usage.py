"""
Ejemplo de cómo inyectar y usar el repositorio en un caso de uso o ruta

Este patrón sigue la inyección de dependencias para desacoplar la lógica de negocio
de la implementación específica del repositorio.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from app.infraestructure.database import get_db
from app.domain.repositories.courseRepository import CourseRepository
from app.infraestructure.db.courseRepositoryImpl import CourseRepositoryImpl
from app.schemas.course import CourseResponse


router = APIRouter(prefix="/courses", tags=["courses"])


async def get_course_repository(db: AsyncSession = Depends(get_db)) -> CourseRepository:
    """Dependencia que proporciona la implementación del repositorio"""
    return CourseRepositoryImpl(db)


@router.get("/{course_id}")
async def get_course(
    course_id: UUID,
    repository: CourseRepository = Depends(get_course_repository)
) -> CourseResponse:
    """Obtiene un curso por ID"""
    course = await repository.get_by_id(course_id)
    
    if course is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    return CourseResponse(
        id_course=course.id_course,
        title=course.title,
        description=course.description,
        tag=course.tag,
        url_image=course.url_image
    )


@router.get("/tag/{tag}")
async def get_course_by_tag(
    tag: str,
    repository: CourseRepository = Depends(get_course_repository)
) -> CourseResponse:
    """Obtiene un curso por etiqueta"""
    course = await repository.get_by_tag(tag)
    
    if course is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado")
    
    return CourseResponse(
        id_course=course.id_course,
        title=course.title,
        description=course.description,
        tag=course.tag,
        url_image=course.url_image
    )


@router.get("/")
async def get_all_courses(
    repository: CourseRepository = Depends(get_course_repository)
) -> list[CourseResponse]:
    """Obtiene todos los cursos"""
    courses = await repository.get_all()
    
    return [
        CourseResponse(
            id_course=course.id_course,
            title=course.title,
            description=course.description,
            tag=course.tag,
            url_image=course.url_image
        )
        for course in courses
    ]
