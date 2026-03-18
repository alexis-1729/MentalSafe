from fastapi import APIRouter, HTTPException, Depends
from app.application.services.sectionService import SectionService
from app.api.schemas.sectionSchemas import sectionResponse, sectionCreate
from app.application.dependencies import get_section_service
from app.domain.exceptions import SectionNotFound
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=sectionResponse)
async def add_section(
    data: sectionCreate,
    service: SectionService = Depends(get_section_service)
):
    """Crear una nueva sección"""
    try:
        section = await service.add_section(data.id_cours)

        return sectionResponse(
            id_section=section.id_section,
            id_cours=section.id_course
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear sección: {str(e)}")


@router.get("/{section_id}", response_model=sectionResponse)
async def get_section_by_id(
    section_id: UUID,
    service: SectionService = Depends(get_section_service)
):
    """Obtener una sección por ID"""
    try:
        section = await service.get_section_by_id(section_id)
        return sectionResponse(
            id_section=section.id_section,
            id_cours=section.id_course
        )
    except SectionNotFound:
        raise HTTPException(status_code=404, detail="Sección no encontrada")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener sección: {str(e)}")


@router.get("/course/{course_id}")
async def get_sections_by_course(
    course_id: UUID,
    service: SectionService = Depends(get_section_service)
):
    """Obtener todas las secciones de un curso"""
    try:
        sections = await service.get_sections_by_course(course_id)
        return [
            sectionResponse(
                id_section=section.id_section,
                id_cours=section.id_course
            )
            for section in sections
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener secciones: {str(e)}")


@router.get("/")
async def get_all_sections(
    service: SectionService = Depends(get_section_service)
):
    """Obtener todas las secciones"""
    try:
        sections = await service.get_all_sections()
        return [
            sectionResponse(
                id_section=section.id_section,
                id_cours=section.id_course
            )
            for section in sections
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener secciones: {str(e)}")