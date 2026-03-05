from fastapi import APIRouter, HTTPException, Depends
from app.api.schemas.courseSchemas import courseCreate, courseResponse
from app.application.services.courseService import CourseService
from app.application.dependencies import get_course_service
from uuid import UUID

router = APIRouter()


@router.post("/", response_model = courseResponse)
async def createCourse(
    data:courseCreate,
    service: CourseService = Depends(get_course_service)
):
    try:
        course = await service.add_course(
            title= data.title,
            description= data.description,
            tag= data.tag,
            url_image= data.url_image
        )

        return courseResponse(
            id_course= course.id_course,
            title = course.title,
            description = course.description,
            tag = course.tag,
            url_image = course.url_image
        )
    except Exception as e:
        raise HTTPException(status_code = 404, detail = "Error: {e}")

@router.get("/{course_id}", response_model = courseResponse)
async def get_course_id(
    id: UUID,
    service: CourseService = Depends(get_course_service)
):
        course = await service.get_course_id(id)
        if not course:
             raise HTTPException(status_code = 409, detail = "Not found")
        return course        

@router.get("/{tag}", response_model = courseResponse)
async def get_course_tag(
    tag: str,
    service: CourseService = Depends(get_course_service)
):
        course = await service.get_course_tag(tag)
        if not course:
             raise HTTPException(status_code = 409, detail = "Not found")
        return course    
