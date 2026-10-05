from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.workExperience import workExperienceResponse, workExperienceCreate
from app.models import workExperience, experienceData
from app.schemas.experienceData import experienceDataCreate, experienceDataResponse


def create_data(data: experienceDataCreate, db: Session)-> experienceDataResponse:
    new_result = experienceData(**data.dict())

    db.add(new_result)
    db.commit()
    db.refresh(new_result)

    return experienceDataResponse(
        id_data = new_result.id_data,
        companyInst = new_result.companyInst,
        position = new_result.position,
        sector = new_result.position,
        description = new_result.description,
        start_date = new_result.start_date,
        finish_date = new_result.finish_date
    )

def create_experience(data: workExperienceCreate, db: Session):
    try:
        new_result = workExperience(**data.dict())

        db.add(new_result)
        db.commit()
        db.refresh(new_result)
        return new_result
    except Exception as e:
        return {"msg":"Error en la creacion de la exp{e}", "detail": None}


def get_experience(id_pro, db: Session)-> list[experienceDataResponse] | None:
    result = db.query(workExperience).filter(workExperience.id_pro == id_pro).all()
    if not result :
        return None
    
    ids = [r.id_experience_data for r in result]

    experience = db.query(experienceData).filter(experienceData.id_data.in_(ids)).all()
    

    return experience

