from fastapi import APIRouter, HTTPException, Depends
from app.api.schemas.contentSchemas import contentCreate, contentResponse
from app.application.services.contentService import ContentService
from app.application.dependencies import get_content_service
from app.domain.exceptions import ContentNotFound
from uuid import UUID

router = APIRouter()


@router.post("/", response_model=contentResponse)
async def create_content(
    data: contentCreate,
    service: ContentService = Depends(get_content_service)
):
    """Crear un nuevo contenido"""
    try:
        content = await service.add_content(
            content=data.content,
            url_video=data.url_video,
            complete=False,
            id_chapter=data.id_chap
        )

        return contentResponse(
            id_content=content.id_content,
            content=content.content,
            url_video=content.url_video,
            complete=content.complete
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear contenido: {str(e)}")


@router.get("/{content_id}", response_model=contentResponse)
async def get_content_by_id(
    content_id: UUID,
    service: ContentService = Depends(get_content_service)
):
    """Obtener un contenido por ID"""
    try:
        content = await service.get_content_by_id(content_id)
        return contentResponse(
            id_content=content.id_content,
            content=content.content,
            url_video=content.url_video,
            complete=content.complete
        )
    except ContentNotFound:
        raise HTTPException(status_code=404, detail="Contenido no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener contenido: {str(e)}")


@router.get("/chapter/{chapter_id}")
async def get_content_by_chapter(
    chapter_id: UUID,
    service: ContentService = Depends(get_content_service)
):
    """Obtener todos los contenidos de un capítulo"""
    try:
        contents = await service.get_content_by_chapter(chapter_id)
        return [
            contentResponse(
                id_content=content.id_content,
                content=content.content,
                url_video=content.url_video,
                complete=content.complete
            )
            for content in contents
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener contenidos: {str(e)}")


@router.get("/")
async def get_all_contents(
    service: ContentService = Depends(get_content_service)
):
    """Obtener todos los contenidos"""
    try:
        contents = await service.get_all_contents()
        return [
            contentResponse(
                id_content=content.id_content,
                content=content.content,
                url_video=content.url_video,
                complete=content.complete
            )
            for content in contents
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener contenidos: {str(e)}")
