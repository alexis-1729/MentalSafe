from fastapi import APIRouter
from app.api.v1.courseRoute import router as course_router
from app.api.v1.sectionRoute import router as section_router
from app.api.v1.chapterRoute import router as chapter_router
from app.api.v1.contentRoute import router as content_router

api_router_v1 = APIRouter(prefix="/api/v1")

api_router_v1.include_router(
    course_router,
    prefix="/course",
    tags=["Course"]
)

api_router_v1.include_router(
    section_router,
    prefix="/section",
    tags=["Section"]
)

api_router_v1.include_router(
    chapter_router,
    prefix="/chapter",
    tags=["Chapter"]
)

api_router_v1.include_router(
    content_router,
    prefix="/content",
    tags=["Content"]
)

router = APIRouter()

router.include_router(api_router_v1)