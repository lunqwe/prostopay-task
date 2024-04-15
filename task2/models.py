from sqlalchemy import Column, Integer, String, select
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base
from dto import CreateUserDTO, UserDTO

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True)

    @classmethod
    async def create_user(cls, db: Session, user_data: CreateUserDTO) -> UserDTO:
        try:
            user = cls(username=user_data.username, email=user_data.email)
            db.add(user)
            db.commit()
            return user
        except Exception as e:
            raise ValueError(str(e))

    @classmethod
    async def get_user(cls, user_id: int, db: Session) -> UserDTO:
        try:
            query = select(cls).filter(cls.id == user_id)
            result = db.execute(query)
            user = result.scalar()
            return user
        except Exception as e:
            raise ValueError(str(e))
        




