import pytest
from models import User, Base
from dto import CreateUserDTO, UserDTO
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import asyncio


@pytest.fixture(scope="session")
def db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(bind=engine)
    yield session
    session.close()


@pytest.mark.asyncio
async def test_create_user(db):
    user_data = CreateUserDTO(username='test_user', email="test@gmail.com")
    user = await User.create_user(db=db, user_data=user_data)

    assert user.username == "test_user"
    assert user.email == "test@gmail.com"

    db.delete(user)
    db.commit()


@pytest.mark.asyncio
async def test_get_user(db):
    user_data = CreateUserDTO(username='test_user', email="test1@gmail.com")
    user = await User.create_user(db=db, user_data=user_data)

    assert user.username == "test_user"
    assert user.email == "test1@gmail.com"

    found_user = await User.get_user(user_id=user.id, db=db)

    assert user.id == found_user.id
    assert user.username == found_user.username
    assert user.email == found_user.email

    db.delete(user)
    db.commit()


