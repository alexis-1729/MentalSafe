from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.especiallity import profesionalSpResponse, profesionSpCreate
from app.models import profesionalScpeciallity, speciallityData
from app.schemas.especiallityData import speciallityResponse, speciallityCreate

def create_data(data: speciallityCreate, db: Session)-> speciallityResponse | None:
    new_data = speciallityData(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return speciallityResponse(
        id_speciallity = new_data.id_speciallity,
        name = new_data.name,
        description = new_data.description
    )

def create_speciallity(data: profesionSpCreate, db: Session):
    new_data = profesionalScpeciallity(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data


def get_speciallity(id_pro: UUID, db: Session)-> list[speciallityResponse] | None:
    result = db.query(profesionalScpeciallity).filter(profesionalScpeciallity.id_pro == id_pro).all()
    if not result:
        return None
    ids = [r.id_speciallity for r in result]
    speciallity = db.query(speciallityData).filter(speciallityData.id_speciallity.in_(ids)).all()
    
    
    return speciallity