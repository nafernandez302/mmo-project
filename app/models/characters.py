from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import Base

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    level = Column(Integer, default=1)
    user_id = Column(Integer, ForeignKey("users.id"))
