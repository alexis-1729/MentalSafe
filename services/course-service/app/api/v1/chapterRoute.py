from fastapi import APIRouter, HTTPException, Depends
from app.api.schemas.chapterSchemas import chapterCreate, chapterResponse
from app.application.services.chapterService import ChapterService
from app.application.dependencies import get_chapter_service
from app.domain.exceptions import ChapterNotFound
from uuid import UUID

router = APIRouter()


@router.post("/", response_model=chapterResponse)
async def create_chapter(
    data: chapterCreate,
    service: ChapterService = Depends(get_chapter_service)
):
    """Crear un nuevo capítulo"""
    try:
        chapter = await service.add_chapter(
            title=data.title,
            description=data.description,
            num_caps=data.num_caps,
            duration=data.duration,
            id_section=data.id_sect,
            numero=data.numero,
            url_image=data.url_image
        )

        return chapterResponse(
            id_chapter=chapter.id_chapter,
            title=chapter.title,
            description=chapter.description,
            duration=chapter.duration,
            numero=chapter.numero,
            complete=chapter.complete,
            url_image=chapter.url_image
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear capítulo: {str(e)}")


@router.get("/{chapter_id}", response_model=chapterResponse)
async def get_chapter_by_id(
    chapter_id: UUID,
    service: ChapterService = Depends(get_chapter_service)
):
    """Obtener un capítulo por ID"""
    try:
        chapter = await service.get_chapter_by_id(chapter_id)
        return chapterResponse(
            id_chapter=chapter.id_chapter,
            title=chapter.title,
            description=chapter.description,
            duration=chapter.duration,
            numero=chapter.numero,
            complete=chapter.complete,
            url_image=chapter.url_image
        )
    except ChapterNotFound:
        raise HTTPException(status_code=404, detail="Capítulo no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener capítulo: {str(e)}")


@router.get("/course/{course_id}")
async def get_chapters_by_course(
    course_id: UUID,
    service: ChapterService = Depends(get_chapter_service)
):
    """Obtener todos los capítulos de un curso"""
    try:
        chapters = await service.get_chapters_by_course(course_id)
        return [
            chapterResponse(
                id_chapter=chapter.id_chapter,
                title=chapter.title,
                description=chapter.description,
                duration=chapter.duration,
                numero=chapter.numero,
                complete=chapter.complete,
                url_image=chapter.url_image
            )
            for chapter in chapters
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener capítulos: {str(e)}")


@router.get("/")
async def get_all_chapters(
    service: ChapterService = Depends(get_chapter_service)
):
    """Obtener todos los capítulos"""
    try:
        chapters = await service.get_all_chapters()
        return [
            chapterResponse(
                id_chapter=chapter.id_chapter,
                title=chapter.title,
                description=chapter.description,
                duration=chapter.duration,
                numero=chapter.numero,
                complete=chapter.complete,
                url_image=chapter.url_image
            )
            for chapter in chapters
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener capítulos: {str(e)}")
