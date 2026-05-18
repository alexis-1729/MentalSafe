from app.infrastructure.db.unit_of_work import SQLAlchemyUnitOfWork
from app.domain.entities.auth import Auth
import pytest
import uuid

@pytest.fixture
def uow(session_factory):
    return SQLAlchemyUnitOfWork(session_factory)


@pytest.mark.asyncio
async def test_uow_commit(uow):
    async with uow:
        user = Auth(
            id=uuid.uuid4(), 
            email= "ibaa59733@gmail.com",
            password_h= "vuib1515123",
            role="admin")
        await uow.auth.add(user)
        await uow.commit()

    async with uow:
        result = await uow.auth.get("ibaa59733@gmail.com")
        assert result is not None