from sqlalchemy.orm import Session
from uuid import UUID
from app.schemas.profesional import startPoint
from app.models import stars

def star(data: startPoint, db: Session):
    profesional = db.query(stars).filter(stars.id_prof == data.id_pro).first()
    if not profesional:
        new = stars(id_prof = data.id_pro)
        db.add(new)
        db.commit()
        db.refresh(new)
        profesional = new
    
    match data.level:
        case "five":
            profesional.five += 1
            profesional.media =(
                profesional.five * 5 + profesional.four * 4 +
                profesional.three * 3 + profesional.two * 2+ 
                profesional.one) / (
                profesional.five + profesional.four +
                profesional.three + profesional.two + 
                profesional.one
                )
            db.commit()
            db.refresh(profesional)
            return profesional
        case "four":
            profesional.four += 1
            profesional.media =(
                    profesional.five * 5 + profesional.four * 4 +
                    profesional.three * 3 + profesional.two * 2+ 
                    profesional.one) / (
                    profesional.five + profesional.four +
                    profesional.three + profesional.two + 
                    profesional.one
                    )
            db.commit()
            db.refresh(profesional)
            return profesional
        case "three":
            profesional.three += 1
            profesional.media =(
                profesional.five * 5 + profesional.four * 4 +
                profesional.three * 3 + profesional.two * 2+ 
                profesional.one) / (
                profesional.five + profesional.four +
                profesional.three + profesional.two + 
                profesional.one
                )
            db.commit()
            db.refresh(profesional)
            return profesional
        case "two":
            profesional.two += 1
            profesional.media = (
                profesional.five * 5 + profesional.four * 4 +
                profesional.three * 3 + profesional.two * 2+ 
                profesional.one) / (
                profesional.five + profesional.four +
                profesional.three + profesional.two + 
                profesional.one
                )
            db.commit()
            db.refresh(profesional)
            return profesional
        case "one":
            profesional.one += 1
            profesional.media =(
                profesional.five * 5 + profesional.four * 4 +
                profesional.three * 3 + profesional.two * 2 + 
                profesional.one) / (
                profesional.five + profesional.four +
                profesional.three + profesional.two + 
                profesional.one
                )
            db.commit()
            db.refresh(profesional)
            return profesional
        case _:
            return None
            
        