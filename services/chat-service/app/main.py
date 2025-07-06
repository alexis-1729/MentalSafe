from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .database import Base, engine
from .routes import tags_test, test_result, test_user, type_test
import os


Base.metadata.create_all(bind = engine)

app = FastAPI()


app.include_router(tags_test.router)
app.include_router(test_user.router)
app.include_router(test_result.router)
app.include_router(type_test.router)
