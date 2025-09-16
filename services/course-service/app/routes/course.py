from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.services.course import get_list_course, get_course_id, get_course_tag, get_chapter, get_content
from app.services.security import verify_access_token
from app.schemas.security import TokenData
from app.schemas.content  import contentResponse, contentCreate
from app.schemas.course import courseCreate, courseResponse
from app.data.course_data import CourseData
from app.schemas.section import sectionCreate
from app.schemas.chapter import chapterCreate,chapterResponse
from uuid import UUID


router = APIRouter(
    prefix = "/course",
    tags = ["Course"]
)


@router.post("/")
def create_course(data: courseCreate, db: Session = Depends(get_db)):
     try:
        course_data = CourseData(db)
        new = course_data.createCourse(data)
        if new is None:
            raise HTTPException(status_code = 404, detail = "No se pudo crear el curso")
        return new
     except Exception as e:
         raise HTTPException(status_code = 500, detail = "Error en el servidor")


@router.post("/section")
def create_section(data: sectionCreate, db: Session = Depends(get_db)):
     try:
        course_data = CourseData(db)
        new = course_data.createSection(data)
        if new is None:
            raise HTTPException(status_code = 404, detail = "No se pudo crear la section")
        return new
     except Exception as e:
         raise HTTPException(status_code = 500, detail = "Error en el servidor")

@router.post("/chapter")
def create_chapter(data: chapterCreate, db: Session = Depends(get_db)):
     try:
        course_data = CourseData(db)
        new = course_data.createChapter(data)
        if new is None:
            raise HTTPException(status_code = 404, detail = "No se pudo crear el chapter")
        return new
     except Exception as e:
         raise HTTPException(status_code = 500, detail = "Error en el servidor")
     
@router.post("/content")
def create_content(data: contentCreate, db: Session = Depends(get_db)):
     try:
        course_data = CourseData(db)
        new = course_data.createContent(data)
        if new is None:
            raise HTTPException(status_code = 404, detail = "No se pudo crear el content")
        return new
     except Exception as e:
         raise HTTPException(status_code = 500, detail = "Error en el servidor")

# ------------------------------------------------------------------------------------------------
@router.get("/", response_model = list[courseResponse])
def list_course(db:Session = Depends(get_db)):
    result = get_list_course(db)
    if not result:
        raise HTTPException(status_code = 404, detail="No se pudo obtner los cursos")
    return result

@router.get("/list_course", response_model= courseResponse)
def course_id(id_course: UUID, db: Session = Depends(get_db)):
    result= get_course_id(id_course, db)
    if result == None:
       raise HTTPException(status_code = 404, detail= "No se encontro un curso con el id")
    return result

@router.get("/course_tag", response_model= courseResponse)
def course_tag(tag: str, 
               db: Session= Depends(get_db)
               ,token_data: TokenData = Depends(verify_access_token)):
    result = get_course_tag(tag, db)
    if result is None:
        raise HTTPException(status_code = 404, detail= "No se encontro un curso con el tag")
    return result

@router.get("/list_chapter", response_model = list[chapterResponse]) 
def get_list_Chapter(id_course: UUID, db: Session = Depends(get_db),token_data: TokenData = Depends(get_db)):
    ans = get_chapter(id_course, db)
    if ans is None:
         raise HTTPException(status_code = 404, detail = "No se econtraron capitulos")
    return ans

@router.get("/get_content",response_model = contentResponse)
def get_content_route(id_chapter: UUID, db: Session = Depends(get_db)):
        ans = get_content(id_chapter, db)
        if ans is None:
            raise HTTPException(status_code = 404, detail = "No se encontro contenido")
        return ans
   
   
    