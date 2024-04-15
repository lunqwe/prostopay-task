from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from dto import CreateUserDTO, UserDTO

Base = declarative_base()

class User(Base):

    """ The user class has 2 @classmethods, which are responsible for creating and getting the user.

        The output of the method meets the requirements of the task 
        get(user_id) → UserDTO
        add(user: UserDTO) → User)
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True)

    @classmethod
    async def create_user(cls, db: AsyncSession, user_data: CreateUserDTO) -> "User":
        try:
            user = cls(username=user_data.username, email=user_data.email)
            db.add(user)
            await db.commit()
            return user
        
        except Exception as e: # Could be specific caught errors 
            raise ValueError(str(e))

    @classmethod
    async def get_user(cls, user_id: int, db: AsyncSession) -> UserDTO:
        try:
            async with db:
                result = await db.execute(select(User).where(User.id == user_id))
                user = result.scalars().first()
                result_data = UserDTO(id=user.id, username=user.username, email=user.email)
                return result_data
         
        except Exception as e: # Could be specific caught errors 
            raise ValueError(str(e))
        




