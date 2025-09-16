from sqlalchemy.orm import Session,joinedload
from uuid import UUID
from app.schemas.profesional import profesionalCompleteResponse, profesionalResponse, profesionalCreate, startPointResponse
from app.schemas.experienceData import experienceDataResponse
from app.schemas.especiallity import speciallityResponse
from app.models import profesionalData, profesionalScpeciallity, workExperience, stars


def create_perfil(data: profesionalCreate, db: Session):
    try:
        new_result = profesionalData(**data.dict())
        db.add(new_result)
        db.commit()
        db.refresh(new_result)
        return {"status": "success", "msg": new_result.id_profesional}
   
    except Exception as e:
        db.rollback()
        raise RuntimeError(f"Error en la base de datos: {e}")



def get_perfil(id_pro: UUID, db: Session)-> profesionalCompleteResponse | None:
    result = db.query(profesionalData).options(
        joinedload(profesionalData.workExp)
            .joinedload(workExperience.expData),
        joinedload(profesionalData.speciallity)
            .joinedload(profesionalScpeciallity.espName),
        joinedload(profesionalData.star)
            .joinedload(stars.pro)
    ).filter(profesionalData.id_profesional == id_pro).first()

    if not result:
        return None
    
    return profesionalCompleteResponse(
        perfil = profesionalResponse(
            name = result.name,
            apellido_pa = result.apellido_pa,
            apellido_ma = result.apellido_ma,
            email = result.email,
            country = result.country,
            city= result.country,
            certification = result.certification
        ),
        workExperience = [
            experienceDataResponse.model_validate(p.expData) 
            for p in result.workExp if p.expData
            ] if result.workExp else [],
        speciallity = [
            speciallityResponse.model_validate(p.espName) 
            for p in result.speciallity if p.espName
            ] if result.speciallity else [],
        calification = startPointResponse(
            five = result.star[0].five if result.star else 0,
            four = result.star[0].four if result.star else 0,
            three = result.star[0].three if result.star else 0,
            two = result.star[0].two if result.star else 0,
            one = result.star[0].one if result.star else 0,
            media = result.star[0].media if result.star else 0.0,
        )
    )
