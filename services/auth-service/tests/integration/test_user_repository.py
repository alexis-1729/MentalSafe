import pytest
from app.infrastructure.db.repositories.auth_repository import SQLAlchemyAuthRepository
from app.domain.entities.auth import Auth
import uuid

@pytest.mark.asyncio
async def test_create_user(db_session):
    repo = SQLAlchemyAuthRepository(db_session)

    user = Auth(
        id= uuid.uuid4(), 
        email= "ibaa59733@gmail.com", 
        password_h= "118651cvsd",
        role = "admin")
    
    await repo.add(user)
    await db_session.commit()

    result = await repo.get("ibaa59733@gmail.com")

    assert result is not None
    assert result.email == "ibaa59733@gmail.com"