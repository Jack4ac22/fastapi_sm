from sqlalchemy import Column, Integer, String
from .database import Base


class DBUser(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)
