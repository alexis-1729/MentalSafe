from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import get_db

from app.services.message import *
from app.services.test_user import *
from app.services.apply_test import *
from app.schemas.message import *

router = APIRouter(
    prefix = "/apply_test",
    tags = ["Test"]

)

#Guardamos el resultado
def create_result_test_route(data:result_test_create, db:Session = Depends(get_db)):
    return create_result_test(data, db)

#Guardamos el test
def create_test_user_route(data: test_user_create, db:Session = Depends(get_db)):
   return create_test_user(data, db)

#Endpoint para enviar mensaje
@router.post("/{user_id}/{name}")
async def apply_test(name: str, user_id: UUID4, request: Request):
    body = await request.json()
    message = body.get("message")
    response = process_input(user_id,message, name)
    if response.status == "success":
        #guardamos score
        create_result_test()
        #guardamos test
        create_test_user_route()
    return {"response": response}
