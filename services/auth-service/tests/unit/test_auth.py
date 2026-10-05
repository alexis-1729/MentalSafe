import pytest
from unittest.mock import AsyncMock, Mock
from tests.unit.use_cases.test_auth_use_cases import RegisterUserUseCase, LoginUserUseCase
from app.domain.entities.auth import Auth
import uuid

@pytest.mark.asyncio
async def test_register_user_success():
    # Mock repo
    mock_repo = AsyncMock()
    mock_repo.get_by_email.return_value = None

    # Mock UoW
    mock_uow = AsyncMock()
    mock_uow.__aenter__.return_value = mock_uow
    mock_uow.users = mock_repo

    # Mock hasher
    mock_hasher = Mock()
    mock_hasher.hash.return_value = "hashed_password"

    use_case = RegisterUserUseCase(mock_uow, mock_hasher)

    user_id = await use_case.execute("test@test.com", "1234")

    assert user_id is not None
    mock_repo.add.assert_called_once()
    mock_uow.commit.assert_called_once()

@pytest.mark.asyncio
async def test_register_user_already_exists():
    mock_repo = AsyncMock()
    mock_repo.get_by_email.return_value = Auth(id = uuid.uuid4(),
                                               email="test@test.com",
                                               password_h= "1c6dsvfas",
                                               role="admin")

    mock_uow = AsyncMock()
    mock_uow.__aenter__.return_value = mock_uow
    mock_uow.users = mock_repo

    mock_hasher = Mock()

    use_case = RegisterUserUseCase(mock_uow, mock_hasher)

    with pytest.raises(Exception):
        await use_case.execute("test@test.com", "1234")

@pytest.mark.asyncio
async def test_login_success():
    user = Auth(
        id=uuid.uuid4(),
        email="test@test.com", 
        password_h="hashed",
        role="admin")

    mock_repo = AsyncMock()
    mock_repo.get_by_email.return_value = user

    mock_uow = AsyncMock()
    mock_uow.__aenter__.return_value = mock_uow
    mock_uow.users = mock_repo

    mock_hasher = Mock()
    mock_hasher.verify.return_value = True

    mock_jwt = Mock()
    mock_jwt.generate.return_value = "token123"

    use_case = LoginUserUseCase(mock_uow, mock_hasher, mock_jwt)

    token = await use_case.execute("test@test.com", "1234")

    assert token == "token123"