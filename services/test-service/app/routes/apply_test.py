from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import get_db
from pydantic import BaseModel, UUID4
from app.services.type_test import get_type_test_by_name
from app.services.result_test import result_test_create, create_result_test
from app.services.test_user import create_test_user, test_user_create
from app.services.apply_test import process_input
from app.services.security import verify_access_token
from app.schemas.security import TokenData

router = APIRouter(
    prefix = "/apply_test",
    tags = ["Test"]

)
class Message(BaseModel):
    message: str


#Endpoint para enviar mensaje
@router.post("/{user_id}/{name}")
async def apply_test(
    name: str, 
    user_id: UUID4, 
    payload: Message, 
    db: Session = Depends(get_db),
    token_data: TokenData = Depends(verify_access_token)):
    
    
    message = payload.message
    response = process_input(user_id,message, name)

    if response.status == "success":
        idTest = get_type_test_by_name(name, db)
        
        #guardamos score

        resultado=create_result_test(
            result_test_create(score=response.score, id_test=idTest), db)
        #guardamos test
        create_test_user(
            test_user_create(id_user=user_id, result_id= resultado.result_id), db
            )

    return {"response": response}
