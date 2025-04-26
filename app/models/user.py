from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'sqlite_autoincrement': True}


    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, unique=True, index=True)
