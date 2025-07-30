from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import UUID4
import uuid
from app.schemas.test_user import test_user_response, test_user_create
from app.schemas.result_test import result_test_create, result_test_response
from app.schemas.tags_test import tags_test_response
from app.schemas.type_test import type_test_create, type_test_response
from app.services.test_user import *
from app.schemas.recomendation_test import RecomendationResponse
from app.models import type_test, result_test, test_user 


def recomendationTest(user_id: UUID4, db: Session)-> RecomendationResponse | None:
    testUser = get_test_user_by_id(user_id)

    if testUser is None:
        test = db.query(type_test).first()
        return RecomendationResponse(
        #regresar con formato 
            id_test = test.typeT_id,
            name = test.name_test
        )
    
    #obtener los resultados realizados
    results_id = [result.result_id for result in testUser.results]
   
    #obtengo valores de tabla results
    ans  = db.query(result_test).filter(result_test.result_id.in_(results_id)).all()
    
    #obtengo id_ test
    type_ids = [r.typeT_id for r in ans]

    #obtengo registros de type_id que no se han realizado
    test_dont_done = db.query(type_test).filter(~type_test.typeT_id.in_(type_ids)).all()

    #test realizados hacer el mas antiguo
    if not test_dont_done:
        first = test_dont_done[0]
        return RecomendationResponse(
            id_test = first.typeT_id,
            name = first.name_test
        )
    else:
        #Busacmos test antiguo
        oldest = (
            db.query(test_user)
            .filter(test_user.id_user == user_id)
            .order_by(test_user.created_at.desc())
            .first()
        )
        #obtener valores de result_id
        r_id = dq.query(result_test).filter(result_test.result_id == oldest.result_id).first()
        #obtener test
        test = db.qeury(type_test).filter(type_test.typeT_id == r_id.id_test).first()

        return RecomendationResponse(
            id_test = test.typeT_id,
            name = test.name_test
        )
    
    #test no realizados regresar el primero




    

