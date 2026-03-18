from fastapi import FastAP
from app.database import Base, engine
from app.routes import tags_test, test_result, test_user, type_test,recomendation_test, apply_test



from app.models import *
#Inicializar clave de API de Google
#Crear las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(tags_test.router)
app.include_router(apply_test.router)
app.include_router(test_user.router)
app.include_router(test_result.router)
app.include_router(type_test.router)
app.include_router(recomendation_test.router)
