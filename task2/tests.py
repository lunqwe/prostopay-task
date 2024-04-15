import pytest
from models import User, Base
from dto import CreateUserDTO
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import pytest_asyncio

# Creating test db
DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(DATABASE_URL)
SessionTesting = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)

# function for models initialization
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

# db fixture 
@pytest_asyncio.fixture
async def db():
    await init_models() # initializing models
    async with SessionTesting(bind=engine) as session:
        yield session

# Create user test function
@pytest.mark.asyncio
async def test_create_user(db):
    user_data = CreateUserDTO(username='test_user', email="test@gmail.com")
    user = await User.create_user(db=db, user_data=user_data)

    assert user.username == "test_user"
    assert user.email == "test@gmail.com"

# Create and then get user function
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



